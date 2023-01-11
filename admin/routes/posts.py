from app import db
from models.models import Posts

from sqlalchemy import desc
from flask import Blueprint, render_template, request

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("/")
def posts_template():
  posts = db.session.query(Posts).filter(Posts.approved == None).order_by(desc(Posts.id)).all()
  return render_template("posts.html", posts=posts)

@posts.route("/approved")
def posts_approved():
  post_id = request.args.get("post_id")
  
  post = db.session.query(Posts).filter(Posts.id == post_id).first()
  post.approved = True
  
  db.session.commit()
  
  posts = db.session.query(Posts).filter(Posts.approved == None).order_by(desc(Posts.id)).all()
  return render_template("posts.html", posts=posts)

@posts.route("/delete")
def posts_delete_template():
  post_id = request.args.get("post_id")
  posts = db.session.query(Posts).filter(Posts.id == post_id).first()

  return render_template("postsDelete.html", posts=posts)
