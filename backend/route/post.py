from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.app import db
from models.models import Homete_post

post = Blueprint("post", __name__, url_prefix="/post")

@post.route("", methods=["POST"])
@jwt_required()
def post_receive():
	"""投稿を受け取り、DBに保存する
	jwtからuser_idを取得する
	jsonから投稿内容を取得する
	"""
	try:	
		user_id = get_jwt_identity()
		post_content = request.json["post_content"]

		db.session.add(Homete_post(user_id = user_id, post_content = post_content))
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400