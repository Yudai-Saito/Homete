from functools import wraps
from traceback import format_exc

from flask import Blueprint, request, jsonify

from app import app, redis

token = Blueprint("token", __name__, url_prefix="/token")

def auth_required(func):
	"""
	認証が必要なAPIのデコレータ
	"""
	@wraps(func)
	def decorated(*args, **kwargs):
		try:
			user_id = request.cookies.get("user_id")
			token = request.cookies.get("token")
			if redis.get(user_id) == token:
				return func(*args, **kwargs)
			else:
				return jsonify({"status": "error"}), 401
		except:
			app.logger.error(format_exc())
			return jsonify({"status": "error"}), 401
	return decorated
