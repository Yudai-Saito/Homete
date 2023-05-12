import datetime

from app import db
from models.models import Posts, PostReactions, ReportPosts, BanAccount

from sqlalchemy import desc, func
from flask import Blueprint, request, redirect, session

from util.auth_decorator import auth_required

account = Blueprint("account", __name__, url_prefix="/account")

@account.route("/ban")
@auth_required
def posts_ban():
  user_id = request.args.get("user_id")

  db.session.add(BanAccount(user_id=user_id))
  
  posts = db.session.query(Posts).filter(Posts.user_id == user_id).all()
  for post in posts:
    post.deleted_at = datetime.datetime.now()
    post.approved = False
  
  post_ids = [post.id for post in posts]
  delete_query = db.session.query(PostReactions)
  delete_query = delete_query.filter(PostReactions.post_id.in_(post_ids))
  delete_query.delete(synchronize_session=False)

  post_ids = db.session.query(ReportPosts.post_id).join(Posts, Posts.id == ReportPosts.post_id).filter(Posts.user_id == user_id).subquery()
  db.session.query(ReportPosts).filter(ReportPosts.post_id.in_(post_ids)).delete(synchronize_session=False)
  
  db.session.commit()

  previous_url = session.pop('previous_url', '/')
  return redirect(previous_url)
