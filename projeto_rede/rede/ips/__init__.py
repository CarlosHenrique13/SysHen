from socket import *


def descobre_ip(x,y):
    x = gethostbyname(y)
    resutado =f"IP ({y}) = [{x}]"
    if len(resutado) < 35:
        for c in range(0,35-len(resutado)):
            resutado += ' '
    return f"IP ({y}) = [{x}] "