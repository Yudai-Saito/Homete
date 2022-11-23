from json import dumps
from traceback import format_exc

from flask import Blueprint, request, jsonify

from sqlalchemy import func, desc, JSON

from app import app, db

from validator.post_reaction_validator import posts_reaction_count_validate

from models.models import Posts, PostReactions, UserReactions

from util.auth_decorator import auth_required
from util.jwt_decoder import get_email_from_cookie
from util.icon_generator import open_peeps_icon

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("", methods=["POST"])
@auth_required
def post_receive():
	try:	
		jwt = request.cookies.get("__session")
		contents = request.json["contents"]
		private = request.json["private"]

		email = get_email_from_cookie(jwt)

		# TODO_名前DBから取得するようにする
		name = "TEST_NAME"

		icon = open_peeps_icon()

		db.session.add(Posts(user_email = email, private = private, contents = contents, name = name,
													head = icon["head"], face = icon["face"], facialhair = icon["facial_hair"], accessories = icon["accessories"],
														skincolor = icon["skin_color"], clothingcolor = icon["clothing_color"], haircolor = icon["hair_color"]))
		db.session.commit()

		return jsonify({"status": "success", "icon":icon, "name":name}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400


@posts.route("", methods=["GET"])
def post_get():
	try:
		#posts.privateついてるものは、reactionの種類は返すがカウントはNullでかえす
		#自分の投稿のカウントは返してあげる
		if request.cookies.get("token"):
			user_id = request.cookies.get("user_id")
			sub_query = db.session.query(UserReaction.post_id, func.json_arrayagg(UserReaction.reaction, type_=JSON)\
							.label("reactions")).filter(UserReaction.user_id == user_id).group_by(UserReaction.post_id).subquery()
		#ここって何もかえってこないんなんじゃないの？
		#未ログインユーザの場合user_idをNoneで代用
		else: 
			sub_query = db.session.query(UserReaction.post_id, func.json_arrayagg(UserReaction.reaction, type_=JSON)\
							.label("reactions")).filter(UserReaction.user_id == None).group_by(UserReaction.post_id).subquery()
		
		#表示されている最後の投稿の作成時刻を取得
		created_at = request.args.get("created_at")

		jwt = request.cookies.get("__session")
		email = get_email_from_cookie(jwt)

		""" SQL
		select
			post.id,
			json_arrayagg(
				json_object(
					"head", post.head,
					"face", post.face,
					"facialhair", post.facialhair,
					"accessories", post.accessories,
					"skincolor", post.skincolor,
					"clothingcolor", post.clothingcolor,
					"haircolor", post.haircolor
				)
			) as icon,
			post.name, post.created_at, post.contents,
			json_arrayagg(
				json_object(
					"reaction", pr.reaction,
					"count",
					case
						post.private
						when post.user_email = 'test_mail' then pr.reaction_count
						when post.private = 1 then null
						else pr.reaction_count
					end
				)
			) as post_reactions,
			ur.user_reaction
		from
			posts as post
			left join post_reactions as pr on post.id = pr.post_id
			left join (
				select
					post_id, json_arrayagg(reaction) as user_reaction
				from
					user_reactions
				where
					user_email = 'test_mail'
				group by
					post_id
			) as ur on pr.post_id = ur.post_id
		group by
			id, ur.user_reaction;
		"""

		#新規取得か追記取得か判定
		#created_atがクエリパラメータにあるかで判定変えてるっぽい
		#deleted_atが設定されてるものは返さない
		if created_at:
			user_reac = db.session.query(func.json_object("post_id", Homete_post.post_id, "created_at", Homete_post.created_at, "post_content", Homete_post.post_content, "post_reaction",\
							func.json_arrayagg(func.json_object("reaction", Post_reaction.reaction, "count", Post_reaction.reaction_count), type_=JSON),\
								"user_reaction", sub_query.c.reactions, type_=JSON))\
									.outerjoin(Post_reaction, Homete_post.post_id == Post_reaction.post_id)\
									.outerjoin(sub_query, sub_query.c.post_id == Homete_post.post_id)\
										.filter(Homete_post.created_at < created_at)\
											.group_by(Homete_post.post_id, sub_query.c.reactions)\
												.order_by(desc(Homete_post.created_at)).limit(30).all()
		else:
			user_reac = db.session.query(func.json_object("post_id", Homete_post.post_id, "created_at", Homete_post.created_at, "post_content", Homete_post.post_content, "post_reaction",\
							func.json_arrayagg(func.json_object("reaction", Post_reaction.reaction, "count", Post_reaction.reaction_count), type_=JSON),\
								"user_reaction", sub_query.c.reactions, type_=JSON))\
									.outerjoin(Post_reaction, Homete_post.post_id == Post_reaction.post_id)\
									.outerjoin(sub_query, sub_query.c.post_id == Homete_post.post_id)\
										.group_by(Homete_post.post_id, sub_query.c.reactions)\
											.order_by(desc(Homete_post.created_at)).limit(30).all()

		return dumps([row[0] for row in user_reac], ensure_ascii=False, default=str), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400


@posts.route("/reaction", methods=["PUT"])
@auth_required
def reaction_count_up():
	try:
		jwt = request.cookies.get("__session")
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]
		
		email = get_email_from_cookie(jwt)

		# TODO_upsertにリファクタすると"存在しなかったら絵文字追加、存在したらインクリメント"の条件分岐不用になるはず
		if db.session.query(PostReactions.query.filter(PostReactions.post_id == post_id, PostReactions.reaction == reaction).exists()).scalar() == True:

			posts_reaction_count_validate(post_id)

			post_reactions = db.session.query(PostReactions).filter(PostReactions.post_id == post_id, PostReactions.reaction == reaction).first()
			post_reactions.reaction_count += 1
		else:
			db.session.add(PostReactions(post_id = post_id, reaction = reaction, reaction_count = 1))

		db.session.add(UserReactions(user_email = email, reaction = reaction, post_id = post_id))
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

'''
@post.route("/reaction", methods=["POST"])
@auth_required
def reaction_count_down():
	"""投稿のリアクションをデクリメントする
	jsonからpost_id, reactionを取得する
	リアクションがある場合は、デクリメントし、ない場合は400を返す
	"""
	try:
		user_id = request.cookies.get("user_id")
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]

		#投稿に既にリアクションがあるか確認 
		if db.session.query(Post_reaction.query.filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).exists()).scalar() == True:
			#減少するリアクションを習得して、デクリメントする
			post = db.session.query(Post_reaction).filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).first()
			post.reaction_count -= 1

			#リアクションが0以下になった場合、レコードを削除
			if post.reaction_count <= 0:
				db.session.delete(post)

			#ユーザごとのリアクション情報を削除
			db.session.delete(UserReaction.query.filter(UserReaction.post_id == post_id, UserReaction.user_id == user_id, UserReaction.reaction == reaction).first())

			db.session.commit()
		else:
			#リアクションが無い場合は400を返す
			raise("not exist reaction")

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400
'''

