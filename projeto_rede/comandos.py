#Pacotes
from rede.ips import *
import os
import sys
from tkinter import *


def retorno(resutado):
    if len(resutado) < 35:
        for c in range(0,35-len(resutado)):
            resutado += ' '
    return resutado
#Comandos
def Comando(comando,area):
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
            return retorno(descobre_ip(coman[1],coman[1]))
        elif coman[0] == 'serv':
            print(comando,coman[1],coman[2],coman[3])
            arg = open(f"{os.getcwd()}/serve.py", 'wt+')
            arg.write(f"import os\nos.system(fr'{os.getcwd()}/rede/serve/__init__.py {coman[1]} {coman[2]} {coman[3]}')\n")
            arg.close()
            os.startfile(f"{os.getcwd()}/serve.py")
            return retorno("Servido Iniciando")
        else:
            return f"Comando: {comando} não reconhecido"
    #Comandos simples
    else:
        if coman[0] == 'cstop':
            import subprocess, signal
            p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = p.communicate()
        else:
            return f"Comando: {comando} não reconhecido"

