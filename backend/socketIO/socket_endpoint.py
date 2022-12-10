from app import app

from os import environ

from flask_socketio import SocketIO
from flask_socketio import emit, send

socketio = SocketIO(app, cors_allowed_origins=[environ["FRONTEND_URL"]])

@socketio.on('connect')
def connect():
    print("connect")

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

@socketio.on('hello')
def handle_message(data):
    print('received message: ' + data)
    emit("hello", "world")
