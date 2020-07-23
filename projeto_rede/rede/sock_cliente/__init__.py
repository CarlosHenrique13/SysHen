import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Variaves
valores = []
if str(sys.argv[1]) == '0':
    valores.append("127.0.0.1")
else:
    valores.append(str(sys.argv[1]))
print(valores)
host = valores[0]
porta = int(sys.argv[2])

s.connect((host, porta))
dados = s.recv(1024)
print(dados.decode('ascii'))
