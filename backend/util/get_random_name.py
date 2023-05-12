import random
from app import db
from sqlalchemy import desc
from models.models import PostsName

def random_name():
	# TODO_単語数をハードコーディングするのではなくテーブルから取ってくる
  random_name_numbers = random.sample(range(1, 2538), 2)

  name = db.session.query(PostsName.name).filter(PostsName.id.in_(random_name_numbers)).order_by(desc(PostsName.name)).all()

  if len(name[0][0] + name[1][0]) > 12:
    return random_name()
  else:
    return random_name_numbers, name
