import datetime

from sqlalchemy.schema import ForeignKey

from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(256), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime)

class Posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey("users.id", name="fk_posts_user_id"))
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
    approved = db.Column(db.Boolean)

class PostReactions(db.Model):
    __tablename__ = "post_reactions"

    user_id = db.Column(db.Integer, ForeignKey("users.id", name="fk_post_reactions_user_id"), primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey("posts.id", name='fk_post_reactions_posts_id'), primary_key=True)
    reaction_id = db.Column(db.Integer, ForeignKey("reactions.id", name='fk_post_reactions_reaction_id'), primary_key=True)

class Reactions(db.Model):
    __tablename__ = "reactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reaction = db.Column(db.String(10), unique=True)

class ReportPosts(db.Model):
    __tablename__ = "report_posts"

    user_id = db.Column(db.Integer, ForeignKey("users.id", name="fk_report_posts_user_id"))
    post_id = db.Column(db.Integer, ForeignKey("posts.id", name='fk_report_posts_post_id'), primary_key=True)

