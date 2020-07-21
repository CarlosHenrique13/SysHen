from socket import *


def descobre_ip(x,y):
    x = gethostbyname(y)
    return f"O endereso IP = {x}"