from app import app, session

from os import environ
from json import dumps

from flask_socketio import SocketIO
from flask_socketio import emit

from util.get_posts import get_posts

socketio = SocketIO(app, cors_allowed_origins=[environ["FRONTEND_URL"]], cors_credentials=True )

@socketio.on('connect')
def connect():
    print("connect")

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

def emit_posts(update_time_start, update_time_end):
    with session.begin():
        posts = get_posts(user_id=None, update="new", created_at="", channel="", update_time_start=update_time_start, update_time_end=update_time_end)

    socketio.emit("new_posts", dumps({"posts": [row[0] for row in posts]}, ensure_ascii=False))
