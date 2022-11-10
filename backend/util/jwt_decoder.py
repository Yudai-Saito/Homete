import json
import base64

def get_email_from_cookie(session):
	session = session.split(".")

	session_optimize = token[1] + "=" * (len(session[1]) % 4)

	session_json = json.loads(base64.urlsafe_b64decode(session_optimize))

	return session_json["email"]
