
from app import db
from sqlalchemy import func, desc, case, and_, JSON
from sqlalchemy.orm import aliased
from models.models import User, Posts, PostReactions, Reactions, PostsName

def get_posts(user_id, update, created_at, channel, update_time_start="", update_time_end="", session=db.session):
  filters = []
  if update == "new":
    filters.append(Posts.created_at > update_time_start)
    filters.append(Posts.created_at <= update_time_end)
  elif update == "old":
    filters.append(created_at > Posts.created_at)
  else:
    filters.append("2000-01-01" < Posts.created_at)

  if channel == "history":
    filters.append(Posts.user_id == user_id)

  reaction_subquery = session.query(Reactions.reaction).filter(Reactions.id == PostReactions.reaction_id).label("post_reactions")

  post_reaction_subquery = session.query(PostReactions.post_id, reaction_subquery, func.count(PostReactions.reaction_id).label("reaction_count"))\
                            .group_by(PostReactions.post_id, PostReactions.reaction_id).subquery()

  reaction_subquery = session.query(Reactions.reaction).filter(Reactions.id == PostReactions.reaction_id, PostReactions.user_id == user_id)

  user_reaction_subquery = session.query(PostReactions.post_id, func.json_arrayagg(reaction_subquery, type_=JSON)\
                            .label("user_reactions")).filter(PostReactions.user_id == user_id).group_by(PostReactions.post_id).subquery()
  
  fn = aliased(PostsName)
  ln = aliased(PostsName)
  
  posts_query = session.query(func.json_object("post_id", Posts.id, \
            "icon", func.json_object("head", Posts.head, "face", Posts.face, "facial_hair", Posts.facialhair, "accessories", Posts.accessories,\
                                        "skin_color", Posts.skincolor, "clothing_color", Posts.clothingcolor, "hair_color", Posts.haircolor, type_=JSON),\
              "name",  func.concat(fn.name, ' ', ln.name), "created_at", Posts.created_at, "contents", Posts.contents, 
                "private", case([(Posts.user_id == user_id, False)], else_=Posts.private),\
                  "user_post", case([(Posts.user_id == user_id, True)], else_=False),\
                    "post_reactions", func.json_arrayagg(func.json_object("reaction", post_reaction_subquery.c.post_reactions,\
                      "count", case([(Posts.user_id == user_id, post_reaction_subquery.c.reaction_count),\
                        (Posts.private == True, None)], else_=post_reaction_subquery.c.reaction_count)), type_=JSON),\
                          "user_reaction", user_reaction_subquery.c.user_reactions, type_=JSON))\
                            .outerjoin(post_reaction_subquery, post_reaction_subquery.c.post_id == Posts.id)\
                            .outerjoin(user_reaction_subquery, user_reaction_subquery.c.post_id == post_reaction_subquery.c.post_id)\
                            .outerjoin(fn, Posts.first_name == fn.id)\
                            .outerjoin(ln, Posts.last_name == ln.id)\
                              .filter(and_(*filters, Posts.deleted_at == None))\
                                .group_by(Posts.id, post_reaction_subquery.c.post_id, user_reaction_subquery.c.post_id, user_reaction_subquery.c.user_reactions)\
                                  .order_by(desc(Posts.created_at))

  if update == "new":
    posts = posts_query.all()
  else:
    posts = posts_query.limit(15).all()

  return posts
