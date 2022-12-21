from os import environ

from flask import Flask, render_template
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

from models.models import Posts

@app.route('/')
def index():
  posts = db.session.query(Posts).all()
  return render_template("index.html", posts=posts)
