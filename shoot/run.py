import os
import socketserver

from shoot.server import ShootServer


def run():
    handler = ShootServer
    httpd = socketserver.TCPServer(("", 8000), handler)
    print("serving at port 8000...")
    httpd.serve_forever()
