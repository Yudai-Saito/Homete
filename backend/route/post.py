from flask import Blueprint, request, jsonify

from app.app import db, redis
from models.models import Homete_post, Post_reaction, Post_schema, UserReaction
from route.token import auth_required

post = Blueprint("post", __name__, url_prefix="/post")

POST_SCHEMA = Post_schema(many=True)

@post.route("", methods=["POST"])
@auth_required
def post_receive():
	"""投稿を受け取り、DBに保存する
	redisからuser_idを取得する
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

@post.route("", methods=["GET"])
def post_get():
	"""投稿取得
	フロントに表示されている最後の投稿の作成時刻を取得
	"""
	try:
		#表示されている最後の投稿の作成時刻を取得
		created_at = request.args.get("created_at")

		if created_at:
			posts = db.session.query(Homete_post).filter(Homete_post.created_at < created_at).order_by(Homete_post.created_at.desc()).limit(30).all()
		else:
			posts = db.session.query(Homete_post).order_by(Homete_post.created_at.desc()).limit(30).all()

		#返す投稿内容をDICTに変換
		content_json = POST_SCHEMA.dump(posts)

		#返す投稿内容に含まれている全てのpost_idを取得	
		post_ids = [post["post_id"] for post in content_json]
		#全てのpost_idに対してのreactionを取得
		reactions = db.session.query(Post_reaction).filter(Post_reaction.post_id.in_(post_ids)).all()

		post_reactions = {}
		content_index = 0
		for post in posts:
			for reaction in reactions:
				if post.post_id == reaction.post_id:
					#付与されているリアクションをDICTにまとめる
					post_reactions.update({reaction.reaction: reaction.reaction_count})
				#投稿内容DICTにリアクションを付与する	
				content_json[content_index].update({"reactions": post_reactions})
			post_reactions = {}
			content_index += 1

		return jsonify({"contents":content_json}), 200
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
		user_id = redis.get(request.cookies.get("token"))
		post_id = request.json["post_id"]
		reaction = request.json["reaction"]

		#投稿に既にリアクションがあるか確認
		if db.session.query(Post_reaction.query.filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).exists()).scalar() == True:
			#増加するリアクションを取得して、インクリメントする
			post = db.session.query(Post_reaction).filter(Post_reaction.post_id == post_id, Post_reaction.reaction == reaction).first()
			post.reaction_count += 1
		else:
			#リアクションがない場合は新規に、post_idとreactionを追加する
			db.session.add(Post_reaction(post_id = post_id, reaction = reaction, reaction_count = 1))
		
		#ユーザごとのリアクション情報を追加
		db.session.add(UserReaction(post_id = post_id, user_id = user_id, reaction = reaction))

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
		user_id = redis.get(request.cookies.get("token"))
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

			#ユーザごとのリアクション情報を削除
			db.session.delete(UserReaction.query.filter(UserReaction.post_id == post_id, UserReaction.user_id == user_id, UserReaction.reaction == reaction).first())

			db.session.commit()
		else:
			#リアクションが無い場合は400を返す
			raise("not exist reaction")

		return jsonify({"status": "success"}), 200
	except:
		return jsonify({"status": "error"}), 400
