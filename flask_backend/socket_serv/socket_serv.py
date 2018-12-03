import json

from flask import Flask, request

from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

ws_app = Flask(__name__)

socket_dict = {}


@ws_app.route("/app/<app_id>")
def app(app_id):
    app_socket = request.environ.get("wsgi.websocket")  # type: WebSocket
    socket_dict[app_id] = app_socket
    print(len(socket_dict), socket_dict)

    while True:
        app_msg = app_socket.receive()
        app_dict = json.loads(app_msg)
        tou_user = app_dict.get("to_user")
        toy_socket = socket_dict.get(tou_user)

        toy_socket.send(app_dict.get("music"))


@ws_app.route("/toy/<toy_id>")
def toy(toy_id):
    toy_socket = request.environ.get("wsgi.websocket")  # type: WebSocket
    socket_dict[toy_id] = toy_socket
    print(len(socket_dict), socket_dict)

    while True:
        toy_msg = toy_socket.receive()
        print(toy_msg)


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0", 9572), ws_app, handler_class=WebSocketHandler)
    http_serv.serve_forever()
