#Pacotes
from rede.ips import *
from tkinter import *

#Comandos
def Comando(comando):
    coman = comando.split(" ")
    #Comando compostos
    if len(coman) >= 2:
        if coman[0] == f'ip {coman[1]}':
            return descobre_ip(coman[1],coman[1])
        else:
            return f"Comando: {coman} não reconhecido"
    #Comandos simples
    else:
        if coman[0] == 'inic':
            pass
        else:
            return f"Comando: {coman} não reconhecido"

