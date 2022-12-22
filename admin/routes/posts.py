from app import db
from models.models import Posts

from sqlalchemy import desc
from flask import Blueprint, render_template

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("/")
def posts_template():
  posts = db.session.query(Posts).filter(Posts.approved == None).order_by(desc(Posts.id)).all()
  return render_template("posts.html", posts=posts)

@posts.route("/delete")
def posts_delete():
  return render_template("postsDelete.html", posts=posts)
