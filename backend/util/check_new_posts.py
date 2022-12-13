from app import session

import time
import datetime
import threading

from flask_socketio import emit

from socketIO.socket_endpoint import emit_posts

from models.models import Posts

update_time_start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def check_new_posts():
    global update_time_start
    update_time_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with session.begin():
        new_posts_exists = session.query(Posts.query.filter(Posts.created_at > update_time_start, Posts.created_at <= update_time_end).exists()).scalar()

    if new_posts_exists == True:
        emit_posts(update_time_start=update_time_start, update_time_end=update_time_end)

    update_time_start = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def task():
    check_new_posts()
    threading.Timer(5, task).start()

