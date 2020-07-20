from socket import *

def get_ip(x, y):
    x = gethostbyname(y)
    print(f"O endereso IP = {x}")

def menu():
   print("Ip scan Python")
   print("0 = Sair \n 1 = Obter Ip\n")
   return int(input("Escolha a opcao desejada: "))
 
while True:

    opcao = menu()
    
    if opcao == 0:
        print("Finalizado")
        break
    elif opcao == 1:
        dominio = str(input("Digite o Dominiuo:" ))
        get_ip(dominio,dominio)