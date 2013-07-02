import os
import socketserver

from shoot.server import ShootServer


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoot.django_settings")
    handler = ShootServer
    httpd = socketserver.TCPServer(("", 8000), handler)
    print("serving at port 8000...")
    httpd.serve_forever()
