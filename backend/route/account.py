from os import environ
from traceback import format_exc
from datetime import datetime, timedelta

from flask import Blueprint, request, jsonify, make_response

from google.oauth2 import id_token
from google.auth.transport import requests

from firebase_admin import auth

from app import app

account = Blueprint("accout", __name__, url_prefix="/account")

@account.route("/login", methods=["POST"])
def login():
	try:
		token = request.headers.get("Authorization")
		email = request.json["email"]

		token_request = requests.Request()
		id_token.verify_firebase_token(token, token_request, clock_skew_in_seconds=10)

		#JWTとの時差でエラーになるため使用できない、修正PRがマージされるのを待つ
		#auth.verify_id_token(token)

		#ここでemailがDBになかったら新規登録としてUserに登録する

		expires_session = timedelta(days=5)
		expires_cookie = datetime.now() + expires_session

		session = auth.create_session_cookie(token, expires_in=expires_session)

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
