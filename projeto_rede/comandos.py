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
def Comando(comando,janela,area):
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
            arg = open(f"{os.getcwd()}/sock_serve.py", 'wt+')
            arg.write(f"import os\nos.system(fr'{os.getcwd()}/rede/sock_serve/__init__.py {coman[1]} {coman[2]} {coman[3]}')\n")
            arg.close()
            os.startfile(f"{os.getcwd()}/sock_serve.py")
            return retorno("Servido Iniciando")
        elif coman[0] == "ctp":
            arg = open(f"{os.getcwd()}/tcp.py", 'wt+')
            arg.write(
                f"import os\nos.system(fr'{os.getcwd()}/rede/cliente/__init__.py {coman[1]} {coman[2]}')\n")
            arg.close()
            os.startfile(f"{os.getcwd()}/tcp.py")
            return retorno(f"Conectando ao servidor")
        elif coman[0] == 'ssh':
            arg = open(f"{os.getcwd()}/ssh_client.py", 'wt+')
            arg.write(
                f"import os\nos.system(fr'{os.getcwd()}/rede/sock_serve/__init__.py {coman[1]} {coman[2]} {coman[3]}')\n")
            arg.close()
            os.startfile(f"{os.getcwd()}/sock_serve.py")
            return retorno("Servido Iniciando")
        else:
            return f"Comando: {comando} não reconhecido"
    #Comandos simples
    else:
        if coman[0] == "finx":
            finaliza_serve()
            arquivos = ['sock_serve.py','tcp.py','ssh_client.py']
            for c in range(0,len(arquivos)):
                if os.path.isfile(f"{os.getcwd()}/{arquivos[c]}"):
                    os.remove(f"{os.getcwd()}/{arquivos[c]}")
            exit()
        elif coman[0] == 'cstopserv':
            return retorno(finaliza_serve())
        else:
            return f"Comando: {comando} não reconhecido"

