"""
socket is python's networking module
https://docs.python.org/3/library/socket.html
"""

import socket

def ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return {'IP': ip, 'Hostname' : hostname}

