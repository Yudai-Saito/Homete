from os import environ
from traceback import format_exc
from datetime import datetime, timedelta

from flask import Blueprint, request, jsonify, make_response

from google.oauth2 import id_token
from google.auth.transport import requests

from firebase_admin import auth

from app import app, db

from models.models import User, Posts, PostReactions

from util.auth_decorator import auth_required
from util.jwt_decoder import get_email_from_cookie

account = Blueprint("accout", __name__, url_prefix="/account")

@account.route("/login", methods=["GET"])
def login():
	try:
		jwt = request.headers.get("Authorization")

		jwt_request = requests.Request()
		id_token.verify_firebase_token(jwt, jwt_request, clock_skew_in_seconds=10)

		#JWTとの時差でエラーになるため使用できない、修正PRがマージされるのを待つ
		#auth.verify_id_token(token)

		user_email = get_email_from_cookie(jwt)

		deleted_user = db.session.query(User.query.filter(User.email == user_email, User.deleted_at != None).exists()).scalar()
		exists_user =	db.session.query(User.query.filter(User.email == user_email).exists()).scalar()

		if deleted_user == True:
			user = db.session.query(User).filter(User.email == user_email).first()
			user.deleted_at = None
		elif exists_user == False:
			db.session.add(User(email = user_email))

		db.session.commit()

		expires_session = timedelta(days=5)
		expires_cookie = datetime.now() + expires_session

		session = auth.create_session_cookie(jwt, expires_in=expires_session)

		response = make_response(jsonify({"status": "success"}), 200)
		response.set_cookie("__session", value=session, expires=expires_cookie, httponly=True, samesite="None", secure=True, domain=environ["DOMAIN"])
		return response
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "auth error"}), 401

@account.route("/logout", methods=["GET"])
def logout():
	try:
		response = make_response(jsonify({"status": "success"}), 200)
		response.set_cookie("__session", value="", expires=0, httponly=True, samesite="None", secure=True, domain=environ["DOMAIN"])

		return response	
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 401

@account.route("/delete", methods=["DELETE"])
@auth_required
def delete():
	try:
		jwt = request.cookies.get("__session")

		user_email = get_email_from_cookie(jwt)

		user_id = db.session.query(User.id).filter(User.email == user_email).first()[0]

		user = db.session.query(User).filter(User.id == user_id).first()
		user.deleted_at = datetime.now() 
  
		posts_query = db.session.query(Posts.id).filter(Posts.user_id == user_id)
		delete_query = db.session.query(PostReactions).filter(PostReactions.post_id.in_(posts_query))
		delete_query.delete(synchronize_session=False)

		posts = db.session.query(Posts).filter(Posts.user_id == user_id).all()

		# N+1になっていそう
		for post in posts:
			post.deleted_at = datetime.now()

		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		app.logger.error(format_exc())
		return jsonify({"status": "error"}), 400
