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
            try:
              if token_type == "header":
                token = request.headers.get("Authorization")
              elif token_type == "cookie":
                token = request.cookies.get("__session")
              
              user_email = get_email_from_cookie(token)
              user = db.session.query(User).filter(User.email == user_email).first()

              if db.session.query(BanAccount).filter(BanAccount.user_id == user.id).first():
                raise Exception()

              return func(*args, **kwargs)
            except:
                app.logger.error(format_exc())
                return jsonify({"status": "your account stoped"}), 402

        return decorated
    return _ban_check
