from tkinter import *
import socket
import sys
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = str(sys.argv[1])
porta = int(sys.argv[2])
conexao = int(sys.argv[3])
print(f'Meu ip: {host}:{porta} conexoa: {conexao}')
msg = "Enviando mensagem para o cliente ola"
s.bind((host,porta))
s.listen(conexao)

while True:
    c, e = s.accept()
    print(f"Conectado com {e}")
    c.send(msg.encode('ascii'))
    c.close()
    sleep(0.5)


