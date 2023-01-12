import os
import datetime

from flask import Blueprint, render_template, request, jsonify, make_response, redirect

from firebase_admin import auth

from google.oauth2 import id_token
from google.auth.transport import requests

from util.auth_decorator import auth_required

login = Blueprint("login", __name__, url_prefix="/")

@login.route("/")
def index():
  return render_template("login.html")

@login.route("/auth")
def account_auth():
  try:
    token = request.headers.get("Authorization")

    jwt_request = requests.Request()
    id_token.verify_firebase_token(token, jwt_request, clock_skew_in_seconds=10)

    expires_session = datetime.timedelta(hours=8)
    # cookie有効期限を設定
    expires_cookie = datetime.datetime.now() + expires_session
    # セッションを作成
    session = auth.create_session_cookie(token, expires_in=expires_session)

    response = make_response(jsonify({"status": "success"}), 200)

    # cookieを設定
    response.set_cookie("__session", value=session, expires=expires_cookie, httponly=True, samesite="None", secure=True, domain=os.environ["DOMAIN"])
    return response
  except:
    raise Exception("Auth Error!")

@login.route("/logout")
@auth_required
def accout_logout():
  response = make_response(redirect("/"))
  response.set_cookie("__session", value="", expires=0, httponly=True, samesite="None", secure=True, domain=os.environ["DOMAIN"])

  return response
