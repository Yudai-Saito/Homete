from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#from firebase_admin import credentials, initialize_app

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#接続先DBMS
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@mysql/{}?charset=utf8mb4"\
                .format(environ["MYSQL_USER"], environ["MYSQL_PASSWORD"], environ["MYSQL_DATABASE"]) #sqlalchemyのDBMSのURL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

#cred = credentials.Certificate("firebase_account_key.json")
#firebase_app = initialize_app(cred)

from routes.error import error
from routes.login import login
from routes.posts import posts

app.register_blueprint(error)
app.register_blueprint(login)
app.register_blueprint(posts)
