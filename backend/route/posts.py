
import datetime
from traceback import format_exc

from flask import Blueprint, request, jsonify

from sqlalchemy import func, desc, case, and_, JSON

from app import app, db

from validator.post_reaction_validator import posts_reaction_count_validate

from models.models import User, Posts, PostReactions, Reactions

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

		user_email = get_email_from_cookie(jwt)

		# TODO_名前DBから取得するようにする
		name = "TEST_NAME"

		icon = open_peeps_icon()

		user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]
		db.session.add(Posts(user_id = user_id, private = private, contents = contents, name = name,
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

		user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]

		delete_posts = db.session.query(Posts).filter(Posts.id == post_id, Posts.user_id == user_id, Posts.deleted_at == None).first()
		delete_posts.deleted_at = datetime.datetime.now()
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

@posts.route("", methods=["GET"])
def post_get():
	try:
		user_id = None

		if request.cookies.get("__session"):
			jwt = request.cookies.get("__session")
			user_email = get_email_from_cookie(jwt)
			user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]

		created_at = request.args.get("created_at")
		update = request.args.get("update")
		channel = request.args.get("channel")

		filters = []
		if update == "new":
			filters.append(created_at < Posts.created_at)
		elif update == "old":
			filters.append(created_at > Posts.created_at)
		else:
			filters.append("2000-01-01" < Posts.created_at)

		if channel == "history":
			filters.append(Posts.user_id == user_id)

		reaction_subquery = db.session.query(Reactions.reaction).filter(Reactions.id == PostReactions.reaction_id).label("post_reactions")
  
		post_reaction_subquery = db.session.query(PostReactions.post_id, reaction_subquery, func.count(PostReactions.reaction_id).label("reaction_count"))\
															.group_by(PostReactions.post_id, PostReactions.reaction_id).subquery()

		reaction_subquery = db.session.query(Reactions.reaction).filter(Reactions.id == PostReactions.reaction_id, PostReactions.user_id == user_id)

		user_reaction_subquery = db.session.query(PostReactions.post_id, func.json_arrayagg(reaction_subquery, type_=JSON)\
															.label("user_reactions")).filter(PostReactions.user_id == user_id).group_by(PostReactions.post_id).subquery()

		posts = db.session.query(func.json_object("post_id", Posts.id, \
							"icon", func.json_object("head", Posts.head, "face", Posts.face, "facial_hair", Posts.facialhair, "accessories", Posts.accessories,\
																					"skin_color", Posts.skincolor, "clothing_color", Posts.clothingcolor, "hair_color", Posts.haircolor, type_=JSON),\
								"name", Posts.name, "created_at", Posts.created_at, "contents", Posts.contents, 
									"private", case([(Posts.user_id == user_id, False)], else_=Posts.private),\
										"user_post", case([(Posts.user_id == user_id, True)], else_=False),\
											"post_reactions", func.json_arrayagg(func.json_object("reaction", post_reaction_subquery.c.post_reactions,\
												"count", case([(Posts.user_id == user_id, post_reaction_subquery.c.reaction_count),\
													(Posts.private == True, None)], else_=post_reaction_subquery.c.reaction_count)), type_=JSON),\
														"user_reaction", user_reaction_subquery.c.user_reactions, type_=JSON))\
															.outerjoin(post_reaction_subquery, post_reaction_subquery.c.post_id == Posts.id)\
															.outerjoin(user_reaction_subquery, user_reaction_subquery.c.post_id == post_reaction_subquery.c.post_id)\
																.filter(and_(*filters, Posts.deleted_at == None))\
																	.group_by(Posts.id, post_reaction_subquery.c.post_id, user_reaction_subquery.c.post_id, user_reaction_subquery.c.user_reactions)\
																		.order_by(desc(Posts.created_at)).limit(30).all()
  
		return jsonify({"posts": [row[0] for row in posts]}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

@posts.route("/reaction", methods=["PUT"])
@auth_required
def reaction():
	try:
		jwt = request.cookies.get("__session")

		post_id = request.json["post_id"]
		reaction = request.json["reaction"]
		
		user_email = get_email_from_cookie(jwt)
		
		if db.session.query(Posts.query.filter(Posts.id == post_id, Posts.deleted_at == None).exists()).scalar() == True:
			user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]
			reaction_id = db.session.query(Reactions.id).filter(Reactions.reaction == reaction).first()[0]

			db.session.add(PostReactions(post_id = post_id, user_id = user_id, reaction_id = reaction_id))

			db.session.commit()
		else:
			raise("deleted posts")
		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

@posts.route("/reaction", methods=["DELETE"])
@auth_required
def reaction_delete():
	try:
		jwt = request.cookies.get("__session")

		post_id = request.args.get("post_id")
		reaction = request.args.get("reaction")
		
		user_email = get_email_from_cookie(jwt)

		user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]
		reaction_id = db.session.query(Reactions.id).filter(Reactions.reaction == reaction).first()[0]

		db.session.query(PostReactions).filter(PostReactions.post_id == post_id, PostReactions.user_id == user_id, PostReactions.reaction_id == reaction_id).delete()

		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400
