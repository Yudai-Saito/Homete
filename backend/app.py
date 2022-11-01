from os import environ
from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

#CORSに対応
CORS(app,supports_credentials=True)

#接続先DBMS
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@mysql/{}?charset=utf8mb4"\
                .format(environ["MYSQL_USER"], environ["MYSQL_PASSWORD"], environ["MYSQL_DATABASE"]) #sqlalchemyのDBMSのURL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #警告の無効化

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)

#各種APIをappに登録
from route.user import user
from route.token import token
from route.post import post

app.register_blueprint(user)
app.register_blueprint(token)
app.register_blueprint(post)
