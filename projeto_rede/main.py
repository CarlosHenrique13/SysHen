from tkinter import *
from comandos import *


def comand(digito):
    comand_saida.insert(0.0,f'{Comando(comand_entra.get(0.0, END))}')
    comand_recent.insert(0.0,comand_entra.get(0.0, END))
    comand_saida.insert(0.0,"===================================")
    comand_entra.delete('1.0', END)


janela = Tk()
janela.geometry("800x500")
#Entrada de Comandos
Label(text="Area de Comandos").place(x=5,y=3)
comand_entra = Text(janela,widt=50,height=10,bg='black',fg='#ffa500')
comand_entra.place(x=5,y=20)
janela.bind('<End>',comand)
#Saida de Comandos
Label(janela,text='Saida de Comandos').place(x=408,y=3)
comand_saida = Text(janela,width=35,height=20,bg='black',fg='#ccff33')
comand_saida.place(x=408,y=20)
#Comando recentes
comand_recent = Text(janela,width=50,height=10,bg='black',fg='#ffffff')
comand_recent.place(x=5,y=180)

janela.mainloop()