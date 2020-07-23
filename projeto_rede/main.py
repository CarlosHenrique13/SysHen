from tkinter import *
from comandos import *


def comand(digito):
    comand_saida.insert(0.0,f'{Comando(comand_entra.get(0.0, END),janela,comand_saida)}')
    comand_recent.insert(0.0,comand_entra.get(0.0, END))
    comand_saida.insert(0.0,"===================================")
    comand_entra.delete('1.0', END)


janela = Tk()
janela.title("Painel")
janela.geometry("800x500")
#Entrada de Comandos
Label(text="Area de Comandos").place(x=5,y=3)
comand_entra = Text(janela,widt=50,height=10,bg='gray',fg='#ffa500')
comand_entra.place(x=5,y=20)
janela.bind('<End>',comand)
#Saida de Comandos
Label(janela,text='Saida de Comandos').place(x=408,y=3)
comand_saida = Text(janela,width=35,height=20,bg='gray',fg='#ccff33')
comand_saida.place(x=408,y=20)
#Comando recentes
comand_recent = Text(janela,width=50,height=10,bg='gray',fg='#ffffff')
comand_recent.place(x=5,y=180)
#Comando recentes
comand_recent = Text(janela,width=50,height=10,bg='gray',fg='#ffffff')
comand_recent.place(x=5,y=180)
janela.mainloop()
try:
    finaliza_serve()
    arquivos = ['sock_serve.py', 'tcp.py', 'ssh_client.py']
    for c in range(0, len(arquivos)):
        if os.path.isfile(f"{os.getcwd()}/{arquivos[c]}"):
            os.remove(f"{os.getcwd()}/{arquivos[c]}")
except:
    print('Erro ao apagar os arquivos')