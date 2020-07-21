from tkinter import *



janela = Tk()
janela.geometry("800x500")
#Entrada de Comandos
Label(text="Area de Comandos").place(x=5,y=3)
comand_entra = Text(janela,widt=50,height=10)
comand_entra.place(x=5,y=20)
#Saida de Comandos
comand_saida = Text()
comand_saida.place(x=750,y=20)
janela.mainloop()