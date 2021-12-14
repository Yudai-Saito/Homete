from datetime import timedelta
from flask import Blueprint
from flask_jwt_extended import create_access_token

token = Blueprint("token", __name__, url_prefix="/token")


def create_mail_token(user_email):
	"""新規登録・パスワードリセット用のトークンを生成
	受け取ったメールアドレスでトークンを生成して返す
	トークンの有効期限は300秒-5分
	"""
	access_token = create_access_token(expires_delta=timedelta(seconds=300), identity=user_email)

	return access_token