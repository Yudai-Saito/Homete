from app import app
from socketIO.socket_endpoint import socketio

import gevent.monkey; gevent.monkey.patch_thread()
import threading
from util.check_new_posts import task


if __name__ == "__main__":
    t1 = threading.Thread(target=task)
    t1.start()

    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
