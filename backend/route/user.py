from re import match
from os import environ
from hashlib import sha256
from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_mail import Message
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from sqlalchemy import or_

from app.app import mail, db
from models.models import User

user = Blueprint("user", __name__, url_prefix="/user")

SIGNUP_URL = "{}/user/signup".format(environ["FRONTEND_URL"])

@user.route("/signup/mail", methods=["POST"])
def signup_mail():
	"""新規登録用のメールを送信
	新規登録時にメールアドレスを受け取り、認証URLを送信する
	"""
	user_email = request.json["user_email"]

	#メールバリデーション
	if match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_email):

		#TOKEN生成
		access_token = create_access_token(expires_delta=timedelta(seconds=300), identity=user_email)

		msg = Message("Hometeメール認証", recipients=[user_email])
		msg.body = "Hometeへようこそ!\n5分以内にこのURLから登録を済ませてください!\n" \
										+ SIGNUP_URL + "?jwt=" + access_token
		mail.send(msg)

		return jsonify({"status": "success"}), 200
	else:
		return jsonify({"status": "error"}), 400

@user.route("/signup", methods=["POST"])
@jwt_required()
def verify():
	"""新規登録ユーザ登録情報受け取り
	新規登録時にメールアドレスを受け取り、ユーザ登録情報をDBに保存する
	"""
	try:
		#JSONからユーザー情報取り出し
		user_email = request.json["user_email"]
		user_name = request.json["user_name"]
		user_id = request.json["user_id"]
		hashed_password = request.json["hashed_password"]

		#パスワードのハッシュ化
		hashed_password = sha256((hashed_password + user_id + environ["SALT"]).encode("utf-8")).hexdigest()

		#DBにユーザ登録
		db.session.add(User(user_email=user_email, user_name=user_name, user_id=user_id, hashed_password=hashed_password))
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@user.route("/login", methods=["POST"])
def login():
	"""ユーザログイン
	ユーザIDとパスワードを受け取り、認証を行う
	"""
	try:
		#JSONからユーザー情報取り出し
		user_info = request.json["user_info"]
		hashed_password = request.json["hashed_password"]

		#DBからユーザ登録情報取得
		user = User.query.filter(or_(User.user_id==user_info, User.user_email==user_info)).first()

		#パスワードのハッシュ化
		hashed_password = sha256((hashed_password + user.user_id + environ["SALT"]).encode("utf-8")).hexdigest()

		#パスワードが一致しているか確認
		if user.hashed_password == hashed_password:
			#Token生成
			access_token = create_access_token(identity=user.user_id)
			refresh_token = create_refresh_token(identity=user.user_id)
			return jsonify({"status": "success", "access_token": access_token, "refresh_token": refresh_token}), 200
		else:
			raise Exception("password error")	
	except:
		return jsonify({"status": "error"}), 400