from re import match
from os import environ
from flask import Blueprint, request, jsonify
from app.app import mail

from flask_mail import Message
from flask_jwt_extended import jwt_required

from route.token import create_mail_token

user = Blueprint("user", __name__, url_prefix="/user")

SIGNUP_URL = "{}/user/signup".format(environ["FRONTEND_URL"])

@user.route("/signup/mail", methods=["POST"])
def login():
	"""新規登録用のメールを送信
	新規登録時にメールアドレスを受け取り、認証URLを送信する
	"""
	user_email = request.json["user_email"]

	#メールバリデーション
	if match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_email):

		msg = Message("Hometeメール認証", recipients=[user_email])
		msg.body = "Hometeへようこそ!\n5分以内にこのURLから登録を済ませてください!\n" \
										+ SIGNUP_URL + "?jwt=" + create_mail_token(user_email)
		mail.send(msg)

		return jsonify({"status": "success"}), 200
	else:
		return jsonify({"status": "error"}), 400

@user.route("/signup/", methods=["POST"])
@jwt_required()
def verify():
	"""新規登録ユーザ登録情報受け取り

	"""

	return jsonify({"status": "success"}), 200