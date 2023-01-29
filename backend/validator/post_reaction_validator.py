from sqlalchemy import func

from app import db
from models.models import PostReactions

def posts_reaction_count_validate(post_id):
    posts_reaction_count = db.session.query(func.count(PostReactions.post_id)).filter(PostReactions.post_id == post_id).all()
    print(posts_reaction_count)
    if posts_reaction_count[0][0] >= 15:
        raise ValueError("over reaction")
