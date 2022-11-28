import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String 

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

class Reactions(Base):
    __tablename__ = "reactions"

    reaction = Column(String(10), primary_key=True,)


emoji = open("emoji.csv", encoding="utf-8")

f = csv.reader(emoji, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)

for row in f:
  db_session.add(Reactions(reaction=row[0]))

db_session.commit()
