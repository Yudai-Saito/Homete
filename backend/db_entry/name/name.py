import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

from os import environ

engine = create_engine("mysql://{}:{}@mysql/{}?charset=utf8mb4".format(environ["MYSQL_USER"], environ["MYSQL_PASSWORD"], environ["MYSQL_DATABASE"]))

db_session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
  )
)


Base = declarative_base()
Base.query  = db_session.query_property()

class PostsName(Base):
    __tablename__ = "posts_name"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(15), unique=True)


tango = open("tango.csv", encoding="utf-8")
f = csv.reader(tango, delimiter=' ')
f = [ row for row in f]

for row in f:
  db_session.add(PostsName(name=row[0].replace(',', '')))

db_session.commit()
