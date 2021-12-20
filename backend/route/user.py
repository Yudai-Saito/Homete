from re import match
from os import environ
from hashlib import sha256
from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_mail import Message
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from sqlalchemy import or_, exists

from app.app import mail, db
from models.models import User

user = Blueprint("user", __name__, url_prefix="/user")

SIGNUP_MESSAGE = "Hometeへようこそ!\n5分以内に以下のURLから登録を済ませてください!\n" + "{}/signup?jwt=".format(environ["FRONTEND_URL"]) 
PASS_RESET_MESSAGE = "Hometeのパスワード再設定メールです。\n5分以内に以下のURLからパスワードの再設定を行ってください。\n" + "{}/passreset?jwt=".format(environ["FRONTEND_URL"])

def mail_sender(user_email, title, message):
	"""メール送信
	タイトル、送信タイプ、メッセージを受け取り、メール送信を行う。
	"""
	#メールバリデーション
	if match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_email):
		#TOKEN生成
		access_token = create_access_token(expires_delta=timedelta(seconds=300), identity=user_email)
		
		#メール生成・送信
		msg = Message(title, recipients=[user_email])
		msg.body = message + access_token
		mail.send(msg)
	else:
		raise Exception("mail format error")

@user.route("/signup/mail", methods=["POST"])
def signup_mail():
	"""新規登録用のメールを送信
	新規登録時にメールアドレスを受け取り、認証URLを送信する
	"""
	try:
		user_email = request.json["user_email"]

		#ユーザ登録チェック、Trueで登録済み
		if db.session.query(User.query.filter(User.user_email == user_email).exists()).scalar() == True:
			raise Exception("user_email already exists")

		mail_sender(user_email, "Hometeメール認証", SIGNUP_MESSAGE)
		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@user.route("/passreset/mail", methods=["POST"])
def passreset_mail():
	"""パスワード再設定用メールを送信
	パスワード再設定時にメールアドレスを受け取り、再設定URLを送信する
	"""
	try:
		user_email = request.json["user_email"]

		#未登録ユーザのチェック, Falseで未登録
		if db.session.query(User.query.filter(User.user_email == user_email).exists()).scalar() == False:
			raise Exception("user_email not exists")

		mail_sender(user_email, "Hometeパスワード再設定", PASS_RESET_MESSAGE)
		return jsonify({"status": "success"}), 200
	except: 
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
		hashed_password = sha256((hashed_password + user_email + environ["SALT"]).encode("utf-8")).hexdigest()

		#DBにユーザ登録
		db.session.add(User(user_email=user_email, user_name=user_name, user_id=user_id, hashed_password=hashed_password))
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@user.route("/password/reset", methods=["POST"])
@jwt_required()
def password_reset():
	"""パスワード再設定
	"""
	try:
		#JWTからメール取り出し
		user_email = get_jwt_identity()

		#JSONからパスワード情報取り出し
		reset_hashed_password = request.json["reset_hashed_password"]

		#パスワードのハッシュ化
		reset_hashed_password = sha256((reset_hashed_password + user_email + environ["SALT"]).encode("utf-8")).hexdigest()

		#DBにユーザ登録
		db.session.query(User).filter(User.user_email == user_email).update({"hashed_password": reset_hashed_password})

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
		hashed_password = sha256((hashed_password + user.user_email + environ["SALT"]).encode("utf-8")).hexdigest()

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