from os import environ
from datetime import timedelta

from redis import Redis

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_jwt_extended import JWTManager
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

#メールクライアント設定
app.config["MAIL_SERVER"] = environ["MAIL_SERVER"] #メールサーバー
app.config["MAIL_PORT"] = 587 #メールサーバーのポート
app.config["MAIL_USE_TLS"] = True #TLSの使用
app.config["MAIL_USE_SSL"] = False #SSLの使用
app.config["MAIL_USERNAME"] = environ["MAIL_USERNAME"] #メールアドレス
app.config["MAIL_PASSWORD"] = environ["MAIL_PASSWORD"] #メールパスワード
app.config["MAIL_DEFAULT_SENDER"] = environ["MAIL_DEFAULT_SENDER"] #送信元メールアドレス

mail = Mail(app)

#JWT設定
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=180) #token有効期限
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=15) #refresh_token有効期限
app.config["JWT_ALGORITHM"] = "HS256" #署名アルゴリズム
app.config["JWT_SECRET_KEY"] = environ["JWT_SECRET_KEY"] #署名キー
app.config["JWT_DECODE_LEEWAY"] = timedelta(seconds=30) #署名検証時の誤差

jwt = JWTManager(app)

#Redisに接続
redis = Redis(host="redis", port=6379, password=environ["REDIS_PASSWORD"], decode_responses=True)

#各種APIをappに登録
from route.user import user
from route.token import token
from route.post import post

app.register_blueprint(user)
app.register_blueprint(token)
app.register_blueprint(post)