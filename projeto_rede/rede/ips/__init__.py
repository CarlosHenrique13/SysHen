from socket import *
import os

#Mostra o ip em vez do DNS
def descobre_ip(x,y):
    x = gethostbyname(y)
    resutado =f"IP ({y}) = [{x}]"
    return f"IP ({y}) = [{x}] "

#Finalizar Servidores
def finaliza_serve():
    processo = os.system('taskkill /f /im conhost.exe')
    return "Servidores finalizado"