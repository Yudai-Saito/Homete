import re
from flask import Blueprint, request, jsonify
from app.app import mail

from flask_mail import Message

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/signup/mail", methods=["POST"])
def login():
	user_email = request.json["user_email"]

	#メールバリデーション
	if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_email):

		msg = Message("Hometeメール認証", recipients=[user_email])
		msg.body = ""
		mail.send(msg)

		return jsonify({"status": "success"}), 200
	else:
		return jsonify({"status": "error"}), 400