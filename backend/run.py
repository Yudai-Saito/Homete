from app import app
from socketIO.socket_endpoint import socketio

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)


