from socket import *


def descobre_ip(x,y):
    x = gethostbyname(y)
    return f"IP ({y}) = [{x}]"