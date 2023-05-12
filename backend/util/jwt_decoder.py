import json
import base64


def decode_jwt(jwt):
	jwt = jwt.split(".")

	jwt_optimize = jwt[1] + "=" * (len(jwt[1]) % 4)

	jwt_json = json.loads(base64.urlsafe_b64decode(jwt_optimize))

	return jwt_json

def get_email_from_cookie(jwt):
	user_email = decode_jwt(jwt)

	return user_email["email"]

def get_id_from_cookie(jwt):
	user_id = decode_jwt(jwt)

	return user_id["user_id"]
