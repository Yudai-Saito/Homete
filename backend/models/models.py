import datetime

from sqlalchemy.schema import ForeignKey

from app import db

class User(db.Model):
    __tablename__ = "users"

    email = db.Column(db.String(256), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime)

class Posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(256), ForeignKey("users.email", name="fk_posts_user_email"))
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
    post_id = db.Column(db.Integer, ForeignKey("posts.id", name='fk_post_reaction_posts_id'))
    reaction = db.Column(db.String(10))
    reaction_count = db.Column(db.Integer)

class UserReactions(db.Model):
    __tablename__ = "user_reactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(256), ForeignKey("users.email", name="fk_user_reaction_posts_user_email"))
    reaction = db.Column(db.String(10))
    post_id = db.Column(db.Integer, ForeignKey("posts.id", name='fk_user_reasction_posts_id'))
