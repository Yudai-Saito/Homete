import datetime
from app import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.String(15), primary_key=True)
    user_name = db.Column(db.String(15))
    user_email = db.Column(db.String(256), unique=True)
    hashed_password = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

class Homete_post(db.Model):
    __tablename__ = "homete_posts"

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(15))
    post_content = db.Column(db.String(100))
    anonymous = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

class Post_reaction(db.Model):
    __tablename__ = "post_reactions"

    reaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer)
    reaction = db.Column(db.String(10))
    reaction_count = db.Column(db.Integer)

class UserReaction(db.Model):
    __tablename__ = "user_reactions"

    user_reaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.String(15))
    reaction = db.Column(db.String(10))