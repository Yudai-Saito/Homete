from functools import wraps
from traceback import format_exc

from flask import request, jsonify

from app import app, db

from models.models import User, BanAccount 

from util.jwt_decoder import get_email_from_cookie

def ban_check(token_type):
    def _ban_check(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            user_email = None
            if token_type == "header":
                user_email = get_email_from_cookie(request.headers.get("Authorization"))
            elif token_type == "cookie":
                user_email = get_email_from_cookie(request.cookies.get("__session"))

            if user_email:
                user_id = db.session.query(User.id).filter(User.email == user_email).first()
                if user_id and db.session.query(BanAccount).filter(BanAccount.user_id == user_id[0]).first():
                    return jsonify({"status": "your account stopped"}), 402

            return func(*args, **kwargs)
        return decorated
    return _ban_check
