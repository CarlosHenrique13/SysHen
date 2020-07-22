from socket import *


def descobre_ip(x,y):
    x = gethostbyname(y)
    resutado =f"IP ({y}) = [{x}]"
    return f"IP ({y}) = [{x}] "