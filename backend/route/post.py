from flask import Blueprint, request, jsonify

from app.app import db, redis
from models.models import Homete_post, Post_reaction
from route.token import auth_required

post = Blueprint("post", __name__, url_prefix="/post")

@post.route("", methods=["POST"])
@auth_required
def post_receive():
	"""投稿を受け取り、DBに保存する
	jwtからuser_idを取得する
	jsonから投稿内容を取得する
	"""
	try:	
		user_id = redis.get(request.cookies.get("token"))
		post_content = request.json["post_content"]

		db.session.add(Homete_post(user_id = user_id, post_content = post_content))
		db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@post.route("/reaction", methods=["PUT"])
@auth_required
def reaction_count_up():
	"""投稿のリアクションをインクリメントする
	jsonからpost_id, reactionを取得する
	リアクションがある場合は、インクリメントし、ない場合は新規に作成する
	"""
	try:
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]

		#投稿に既にリアクションがあるか確認
		if db.session.query(Post_reaction.query.filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).exists()).scalar() == True:
			#増加するリアクションを取得して、インクリメントする
			post = db.session.query(Post_reaction).filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).first()
			post.reaction_count += 1
			db.session.commit()
		else:
			#リアクションがない場合は新規に、post_idとreactionを追加する
			db.session.add(Post_reaction(post_id = post_id, reaction = reaction, reaction_count = 1))
			db.session.commit()

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400

@post.route("/reaction", methods=["DELETE"])
@auth_required
def reaction_count_down():
	"""投稿のリアクションをデクリメントする
	jsonからpost_id, reactionを取得する
	リアクションがある場合は、デクリメントし、ない場合は400を返す
	"""
	try:
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]

		#投稿に既にリアクションがあるか確認 
		if db.session.query(Post_reaction.query.filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).exists()).scalar() == True:
			#減少するリアクションを習得して、デクリメントする
			post = db.session.query(Post_reaction).filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).first()
			post.reaction_count -= 1

			#リアクションが0以下になった場合、レコードを削除
			if post.reaction_count <= 0:
				db.session.delete(post)

			db.session.commit()
		else:
			#リアクションが無い場合は400を返す
			raise("not exist reaction")

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400
