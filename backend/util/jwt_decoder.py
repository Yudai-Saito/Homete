import json
import base64

def get_email_from_cookie(jwt):
	jwt = jwt.split(".")

	jwt_optimize = jwt[1] + "=" * (len(jwt[1]) % 4)

	jwt_json = json.loads(base64.urlsafe_b64decode(jwt_optimize))

	return jwt_json["email"]
