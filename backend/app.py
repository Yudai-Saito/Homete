from os import environ
from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO

from firebase_admin import credentials, initialize_app

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SECRET_KEY"] = environ["SECRET_KEY"]

#CORSに対応
CORS(app, supports_credentials=True)

#接続先DBMS
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@mysql/{}?charset=utf8mb4"\
                .format(environ["MYSQL_USER"], environ["MYSQL_PASSWORD"], environ["MYSQL_DATABASE"]) #sqlalchemyのDBMSのURL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #警告の無効化

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)

cred = credentials.Certificate("firebase_account_key.json")
firebase_app = initialize_app(cred)

#各種APIをappに登録
from route.posts import posts
from route.account import account

app.register_blueprint(posts)
app.register_blueprint(account)
