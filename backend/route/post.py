from flask import Blueprint, request, jsonify

from sqlalchemy import func, JSON

from app.app import db, redis
from models.models import Homete_post, Post_reaction, Post_schema, UserReaction
from route.token import auth_required

post = Blueprint("post", __name__, url_prefix="/post")

POST_SCHEMA = Post_schema(many=True)

@post.route("", methods=["POST"])
@auth_required
def post_receive():
	"""投稿を受け取り、DBに保存する
	redisからuser_idを取得する
	jsonから投稿内容を取得する
	"""
	try:	
		user_id = redis.get(request.cookies.get("token"))
		post_content = request.json["post_content"]

		db.session.add(Homete_post(user_id = user_id, post_content = post_content))
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@post.route("", methods=["GET"])
def post_get():
	"""投稿取得
	フロントに表示されている最後の投稿の作成時刻を取得
	"""
	try:
		#ログインユーザか判定
		if request.cookies.get("token"):
			user_id = redis.get(request.cookies.get("token"))
			sub_query = db.session.query(UserReaction.post_id, func.json_arrayagg(UserReaction.reaction, type_=JSON)\
							.label("reactions")).filter(UserReaction.user_id == user_id).group_by(UserReaction.post_id).subquery()
		else: #未ログインユーザの場合user_idをNoneで代用
			sub_query = db.session.query(UserReaction.post_id, func.json_arrayagg(UserReaction.reaction, type_=JSON)\
							.label("reactions")).filter(UserReaction.user_id == None).group_by(UserReaction.post_id).subquery()
		
		#表示されている最後の投稿の作成時刻を取得
		created_at = request.args.get("created_at")

		"""	SQL
		select p.post_id, p.created_at, 
		json_arrayagg(json_object("reaction", pr.reaction, "count", pr.reaction_count)) as post_reaction, ur.user_reaciton
		from homete_posts as p
		left join post_reactions as pr on p.post_id = pr.post_id
		left join 
		(select post_id, json_arrayagg(reaction) as user_reaciton 
			from user_reactions 
			where user_id = %user_id 
			group by post_id) as ur
		on pr.post_id = ur.post_id
		where p.created_at < %created_at
		group by post_id, ur.user_reaciton;
		"""

		#新規取得か追記取得か判定
		if created_at:
			user_reac = db.session.query(func.json_object("post_id", Homete_post.post_id, "created_at", Homete_post.created_at, "post_reaction",\
							func.json_arrayagg(func.json_object("reaction", Post_reaction.reaction, "count", Post_reaction.reaction_count), type_=JSON),\
								"user_reaction", sub_query.c.reactions, type_=JSON))\
									.outerjoin(Post_reaction, Homete_post.post_id == Post_reaction.post_id)\
									.outerjoin(sub_query, sub_query.c.post_id == Homete_post.post_id)\
										.filter(Homete_post.created_at < created_at)\
											.group_by(Homete_post.post_id, sub_query.c.reactions).limit(30).all()
		else:
			user_reac = db.session.query(func.json_object("post_id", Homete_post.post_id, "created_at", Homete_post.created_at, "post_reaction",\
							func.json_arrayagg(func.json_object("reaction", Post_reaction.reaction, "count", Post_reaction.reaction_count), type_=JSON),\
								"user_reaction", sub_query.c.reactions, type_=JSON))\
									.outerjoin(Post_reaction, Homete_post.post_id == Post_reaction.post_id)\
									.outerjoin(sub_query, sub_query.c.post_id == Homete_post.post_id)\
										.group_by(Homete_post.post_id, sub_query.c.reactions).limit(30).all()

		return jsonify({"posts": [row[0] for row in user_reac]}), 200
	except:
		return jsonify({"status": "error"}), 400
	
@post.route("/reaction", methods=["PUT"])
@auth_required
def reaction_count_up():
	"""投稿のリアクションをインクリメントする
	jsonからpost_id, reactionを取得する
	リアクションがある場合は、インクリメントし、ない場合は新規に作成する
	"""
	try:
		user_id = redis.get(request.cookies.get("token"))
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]

		#投稿に既にリアクションがあるか確認
		if db.session.query(Post_reaction.query.filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).exists()).scalar() == True:
			#増加するリアクションを取得して、インクリメントする
			post = db.session.query(Post_reaction).filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).first()
			post.reaction_count += 1
		else:
			#リアクションがない場合は新規に、post_idとreactionを追加する
			db.session.add(Post_reaction(post_id = post_id, reaction = reaction, reaction_count = 1))
		
		#ユーザごとのリアクション情報を追加
		db.session.add(UserReaction(post_id = post_id, user_id = user_id, reaction = reaction))

		db.session.commit()
		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@post.route("/reaction", methods=["DELETE"])
@auth_required
def reaction_count_down():
	"""投稿のリアクションをデクリメントする
	jsonからpost_id, reactionを取得する
	リアクションがある場合は、デクリメントし、ない場合は400を返す
	"""
	try:
		user_id = redis.get(request.cookies.get("token"))
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
		return jsonify({"status": "error"}), 400
