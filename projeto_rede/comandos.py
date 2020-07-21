#Pacotes
from rede.ips import *
from tkinter import *

#Comandos
def Comando(comando):
    temp = comando.split(" ")
    coman = []
    for c in range(0,len(temp)):
        if '\n' in temp[c] :
            coman.append(temp[c][:-1])
        else:
            coman.append(temp[c])
    #Comando compostos
    if len(coman) >= 2:
        if coman[0] == 'ip':
            return descobre_ip(coman[1],coman[1])
        else:
            return f"Comando: {comando} não reconhecido"
    #Comandos simples
    else:
        if coman[0] == 'inic':
            pass
        else:
            return f"Comando: {comando} não reconhecido"

