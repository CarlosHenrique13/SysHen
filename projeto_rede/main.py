from tkinter import *
from comandos import *


def comand():
    comand_saida.insert(1.0,'oi\n')

janela = Tk()
janela.geometry("800x500")

#Saida de Comandos
comand_saida = Text(janela)
comand_saida.place(x=750,y=20)
comand_saida.insert(1.0,'oi\n')
#Entrada de Comandos
Label(text="Area de Comandos").place(x=5,y=3)
comand_entra = Text(janela,widt=50,height=10)
comand_entra.place(x=5,y=20)
janela.bind('<Return>',comand)

janela.mainloop()