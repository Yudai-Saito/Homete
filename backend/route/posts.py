
import datetime
from traceback import format_exc

from flask import Blueprint, request, jsonify

from sqlalchemy import func, desc, case, and_, JSON

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

@posts.route("", methods=["DELETE"])
@auth_required
def posts_delete():
	try:
		jwt = request.cookies.get("__session")
		post_id = request.json["post_id"]

		user_email = get_email_from_cookie(jwt)

		delete_posts = db.session.query(Posts).filter(Posts.id == post_id, Posts.user_email == user_email).first()
		delete_posts.deleted_at = datetime.datetime.now()
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

@posts.route("", methods=["GET"])
def post_get():
	try:
		user_email = None

		if request.cookies.get("__session"):
			jwt = request.cookies.get("__session")
			user_email = get_email_from_cookie(jwt)
		
		created_at = request.args.get("created_at")
		update = request.args.get("update")

		filters = []
		if update == "new":
			filters.append(created_at < Posts.created_at)
		elif update == "old":
			filters.append(created_at > Posts.created_at)
		else:
			filters.append("2000-01-01" < Posts.created_at)

		sub_query = db.session.query(UserReactions.post_id, func.json_arrayagg(UserReactions.reaction, type_=JSON)\
						.label("reactions")).filter(UserReactions.user_email == user_email).group_by(UserReactions.post_id).subquery()

		posts = db.session.query(func.json_object("post_id", Posts.id, \
						"icon", func.json_object("head", Posts.head, "face", Posts.face, "facial_hair", Posts.facialhair, "accessories", Posts.accessories,\
																				"skin_color", Posts.skincolor, "clothing_color", Posts.clothingcolor, "hair_color", Posts.haircolor, type_=JSON),\
							"name", Posts.name, "created_at", Posts.created_at, "contents", Posts.contents,\
								"post_reactions", func.json_arrayagg(func.json_object("reaction", PostReactions.reaction,\
									"count", case([(Posts.user_email == user_email, PostReactions.reaction_count),\
										(Posts.private == True, None)], else_=PostReactions.reaction_count)), type_=JSON),\
											"user_reaction", sub_query.c.reactions, type_=JSON))\
												.outerjoin(PostReactions, Posts.id == PostReactions.post_id)\
												.outerjoin(sub_query, sub_query.c.post_id == Posts.id)\
													.filter(and_(*filters, Posts.deleted_at == None))\
														.group_by(Posts.id, sub_query.c.reactions)\
															.order_by(desc(Posts.created_at)).limit(30).all()
  
		return jsonify({"posts": [row[0] for row in posts]}), 200
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

@posts.route("/reaction", methods=["DELETE"])
@auth_required
def reaction_count_down():
	try:
		jwt = request.cookies.get("__session")
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]

		user_email = get_email_from_cookie(jwt)

		post = db.session.query(PostReactions).filter(PostReactions.post_id == post_id, PostReactions.reaction == reaction).first()

		post.reaction_count -= 1

		if post.reaction_count <= 0:
			db.session.delete(post)

		db.session.delete(UserReactions.query.filter(UserReactions.post_id == post_id, UserReactions.user_email == user_email, UserReactions.reaction == reaction).first())

		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400
