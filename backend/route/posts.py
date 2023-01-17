
import datetime
from traceback import format_exc

from flask import Blueprint, request, jsonify

from sqlalchemy import func, desc, case, and_, JSON
from sqlalchemy.exc import IntegrityError

from app import app, db

from validator.post_reaction_validator import posts_reaction_count_validate

from models.models import User, Posts, PostReactions, Reactions, ReportPosts

from util.auth_decorator import auth_required
from util.jwt_decoder import get_email_from_cookie
from util.icon_generator import open_peeps_icon
from util.get_posts import get_posts
from util.posts_template import user_posts_template
from util.ban_check import ban_check

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("", methods=["POST"])
@ban_check("cookie")
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

		added_posts_id = db.session.query(Posts.id).filter(Posts.user_id == user_id).order_by(desc(Posts.id)).first()[0]
		added_posts = db.session.query(Posts).filter(Posts.id == added_posts_id).first()

		user_posts = user_posts_template

		user_posts["contents"] = added_posts.contents
		user_posts["created_at"] = added_posts.created_at.strftime('%Y-%m-%d %H:%M:%S')
		user_posts["icon"] = icon
		user_posts["name"] = name
		user_posts["post_id"] = added_posts.id

		return jsonify({"status": "success", "user_posts":user_posts}), 200

	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

@posts.route("", methods=["DELETE"])
@ban_check("cookie")
@auth_required
def posts_delete():
	try:
			jwt = request.cookies.get("__session")
			post_id = request.args.get("post_id")

			user_email = get_email_from_cookie(jwt)

			user = db.session.query(User).filter(User.email == user_email).first()

			db.session.query(PostReactions).filter(PostReactions.post_id == post_id, PostReactions.user_id == user.id).delete()

			post = db.session.query(Posts).filter(Posts.id == post_id, Posts.user_id == user.id, Posts.deleted_at == None).first()
			post.deleted_at = datetime.datetime.now()

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

		update = request.args.get("update")
		created_at = request.args.get("created_at")
		channel = request.args.get("channel")

		posts = get_posts(user_id, update, created_at, channel)
  
		return jsonify({"posts": [row[0] for row in posts]}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400

@posts.route("/report", methods=["POST"])
@ban_check("cookie")
@auth_required
def port_report():
	try:
		jwt = request.cookies.get("__session")

		user_email = get_email_from_cookie(jwt)
		user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]

		post_id = request.json["post_id"]

		if(db.session.query(Posts).filter(Posts.id == post_id, Posts.approved == None).first()):
			db.session.add(ReportPosts(user_id = user_id, post_id = post_id))
			db.session.commit()

		return jsonify({"status":"success"}), 200
	#主キーかぶりでエラー吐いた場合でも200番返してあげる
	except IntegrityError:
		return jsonify({"status":"success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status":"error"}), 400

@posts.route("/reaction", methods=["PUT"])
@ban_check("cookie")
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
@ban_check("cookie")
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
