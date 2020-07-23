import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Variaves
valores = []
if str(sys.argv[1]) == '0':
    valores.append("127.0.0.1")
else:
    valores.append(str(sys.argv[1]))
host = valores[0]
porta = int(sys.argv[2])
if int(sys.argv[3]) == 0:
    valores.append(int(1))
else:
    valores.append(int(sys.argv[3]))
conexao = valores[1]
print(f'Meu ip: {host}:{porta} conexoa: {conexao}')

msg = "Enviando mensagem para o sock_cliente ola"
#Conexão
s.bind((host,porta))
s.listen(conexao)

#Espera da Conexão
while True:
    c, e = s.accept()
    print(f"Conectado com {e}")
    c.send(msg.encode('ascii'))
    c.close()


