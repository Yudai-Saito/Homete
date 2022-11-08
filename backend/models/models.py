import datetime
from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime)

class Posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    face_id = db.Column(db.Integer)
    name = db.Column(db.String(15))
    contents = db.Column(db.String(400))
    private = db.Column(db.Boolean, default=True)
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
    user_id = db.Column(db.Integer)
    reaction_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

class PostFaces(db.Model):
    __tablename__ = "post_faces"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    head = db.Column(db.String(15))
    face = db.Column(db.String(15))
    facialHair = db.Column(db.String(15))
    accessories = db.Column(db.String(15))
    skinColor = db.Column(db.String(15))
    clothingColor = db.Column(db.String(15))
    hairColor = db.Column(db.String(15))
