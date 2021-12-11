import os
import datetime

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}@postgres:5432/{}".format(os.environ["POSTGRES_USER"], os.environ["POSTGRES_PASSWORD"], os.environ["POSTGRES_DB"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)

from models.models import *