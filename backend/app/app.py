import os
import datetime

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)

#接続先DBMS
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}@postgres:5432/{}".format(os.environ["POSTGRES_USER"], os.environ["POSTGRES_PASSWORD"], os.environ["POSTGRES_DB"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)

#メールクライアント設定
app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]

mail = Mail(app)

#各種APIをappに登録
from route.user import user
app.register_blueprint(user)