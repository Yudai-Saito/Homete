from functools import wraps
from traceback import format_exc

from flask import request, jsonify

from google.oauth2 import id_token
from google.auth.transport import requests

from app import app

def auth_required(func):
	@wraps(func)
	def decorated(*args, **kwargs):
		try:
			session = request.cookies.get("__session")

			token_request = requests.Request()
			CERTS_URL = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/publicKeys"
			id_token.verify_token(id_token=session, request=token_request, certs_url=CERTS_URL, clock_skew_in_seconds=10)

			#JWTとの時差でエラーになるため使用できない、修正PRがマージされるのを待つ	
			#auth.verify_session_cookie(session, check_revoked=True)

			return func(*args, **kwargs)
		except:
			app.logger.error(format_exc())
			return jsonify({"status": "auth error"}), 401

	return decorated
