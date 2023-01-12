import datetime

from app import db
from models.models import Posts, PostReactions, ReportPosts

from sqlalchemy import desc, func
from flask import Blueprint, render_template, request, redirect, url_for, session

from util.auth_decorator import auth_required

posts = Blueprint("posts", __name__, url_prefix="/posts")

@posts.route("/")
@auth_required
def posts_template():
  posts = db.session.query(Posts).filter(Posts.approved == None).order_by(desc(Posts.id)).all()
  return render_template("posts.html", display_name="全体投稿" ,posts=posts)

@posts.route("/report")
@auth_required
def posts_report_template():
    report_posts = db.session.query(ReportPosts.post_id).all()
    report_posts = [post.post_id for post in report_posts] 

    posts = db.session.query(Posts).filter(Posts.id.in_(report_posts), Posts.approved == None).order_by(desc(Posts.id)).all()

    return render_template("posts.html", display_name="通報投稿", posts=posts)

@posts.route("/approved")
@auth_required
def posts_approved():
  post_id = request.args.get("post_id")
  
  post = db.session.query(Posts).filter(Posts.id == post_id).first()
  post.approved = True

  db.session.query(ReportPosts).filter(ReportPosts.post_id == post_id).delete()
  
  db.session.commit()
  
  return redirect(request.referrer)

@posts.route("/delete")
@auth_required
def posts_delete_template():
  post_id = request.args.get("post_id")

  posts = db.session.query(Posts).filter(Posts.id == post_id).first()
  delete_count = db.session.query(func.count(Posts.approved)).filter(Posts.user_id == posts.user_id, Posts.approved == False).all()

  session['previous_url'] = request.referrer

  return render_template("postsDelete.html", posts=posts, delete_count=delete_count[0][0], referrer=request.referrer)

@posts.route("/destroy")
@auth_required
def posts_destoroy():
  post_id = request.args.get("post_id")

  db.session.query(PostReactions).filter(PostReactions.post_id == post_id).delete()

  post = db.session.query(Posts).filter(Posts.id == post_id).first()
  post.approved = False
  post.deleted_at = datetime.datetime.now()
  
  db.session.query(ReportPosts).filter(ReportPosts.post_id == post_id).delete()

  db.session.commit()

  previous_url = session.pop('previous_url', '/')
  return redirect(previous_url)
