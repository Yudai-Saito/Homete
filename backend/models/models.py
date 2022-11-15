import datetime
from app import db

class User(db.Model):
    __tablename__ = "users"

    email = db.Column(db.String(256), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime)

class Posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(256))
    private = db.Column(db.Boolean, default=True)
    contents = db.Column(db.String(400))
    name = db.Column(db.String(15))
    head = db.Column(db.String(15))
    face = db.Column(db.String(15))
    facialhair = db.Column(db.String(15))
    accessories = db.Column(db.String(15))
    skincolor = db.Column(db.String(15))
    clothingcolor = db.Column(db.String(15))
    haircolor = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime)

class PostReactions(db.Model):
    __tablename__ = "post_reactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer)
    reaction = db.Column(db.String(10))
    reaction_count = db.Column(db.Integer)

class UserReactions(db.Model):
    __tablename__ = "user_reactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(256))
    reaction_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)
