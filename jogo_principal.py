from tkinter import *
from mundo import mundos
global janela


def principal():
    global janela
    janela = Tk()
    janela.title("Educa Python")
    janela.geometry("640x480+500+153")
    janela.resizable(width=False, height=False)
    janela.iconbitmap(default="imagens_principal\\Python.ico")

    img_fundo = PhotoImage(file="imagens_principal\\Pagina Inicial.png")
    img_botaoinicio = PhotoImage(file="imagens_principal\\Iniciar.png")
    img_botaosair = PhotoImage(file="imagens_principal\\Sair.png")
    #
    # Criação de Labels
    lab_fundo = Label(janela, image=img_fundo)
    lab_fundo.pack()

    # Criação de botões
    bt_inicio = Button(janela, bd=0, image=img_botaoinicio, command=lambda: [mundos(janela)])
    bt_inicio.place(width=159, height=85, x=134, y=253)
    #
    bt_fim = Button(janela, bd=0, image=img_botaosair, command=janela.destroy)
    bt_fim.place(width=159, height=85, x=340, y=253)
    janela.mainloop()
    return janela


principal()
