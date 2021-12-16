import datetime
from app.app import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.String(15), primary_key=True)
    user_name = db.Column(db.String(15))
    user_email = db.Column(db.String, unique=True)
    hashed_password = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime)
    delete_at = db.Column(db.DateTime)

class Homete_post(db.Model):
    __tablename__ = "homete_posts"

    post_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String(15))
    post_content = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime)
    delete_at = db.Column(db.DateTime)

class Post_reaction(db.Model):
    __tablename__ = "post_reactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String)
    reaction = db.Column(db.String)
    reaction_count = db.Column(db.Integer)