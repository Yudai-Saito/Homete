from sqlalchemy import func

from app import db
from models.models import PostReactions, Reactions

DEFAULT_REACTION = ["👍", "👀", "💯", "🥰", "🎉"]

def posts_reaction_count_validate(post_id, reaction_id):
    reaction = db.session.query(Reactions.reaction).filter(Reactions.id == reaction_id).first()[0]
    exists_reaction = db.session.query(PostReactions.query.filter(PostReactions.reaction_id == reaction_id).exists()).scalar()

    if reaction in DEFAULT_REACTION or exists_reaction:
        return

    posts_reaction_count = db.session.query(func.count(func.distinct(Reactions.id))) \
                .join(PostReactions, Reactions.id == PostReactions.reaction_id) \
                    .filter(PostReactions.post_id == post_id, ~Reactions.reaction.in_(DEFAULT_REACTION)).scalar()

    if posts_reaction_count >= 15:
        raise ValueError("over reaction")
