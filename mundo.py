from mundo1 import mundo1_perguntas
from mundo2 import mundo2_Perguntas
from mundo3 import mundo3_Perguntas
from mundo4 import mundo4_Perguntas
global janelamundo, janela


def mundos(janela):
    global janelamundo
    from tkinter import PhotoImage, Label, Button, Toplevel
    janelamundo = Toplevel(janela)
    janelamundo.title("Educa Python")
    janelamundo.geometry("640x480+500+153")
    janelamundo.resizable(width=False, height=False)
    janelamundo.iconbitmap(default="imagens_principal\\Python.ico")

    # variaveis globais

    # importando imagens
    img_fundo1 = PhotoImage(file="imagens_mundos/Menu de mundos.png")
    img_botaomundo1 = PhotoImage(file="imagens_mundos/Mundo1 - Fácil ( Soma).png")
    img_botaomundo2 = PhotoImage(file="imagens_mundos/Mundo2 - Fácil ( Subtração).png")
    img_botaomundo3 = PhotoImage(file="imagens_mundos/Mundo3 - Médio ( Multiplicação).png")
    img_botaomundo4 = PhotoImage(file="imagens_mundos/Mundo4 - Difícil ( Divisão).png")
    # Criação de Labels
    lab_fundo = Label(janelamundo, image=img_fundo1)
    lab_fundo.pack()

    # Criação de botões
    bt_mundo1 = Button(janelamundo, bd=0, image=img_botaomundo1, command=lambda: [mundo1_perguntas(janelamundo)])
    bt_mundo1.place(width=190, height=40, x=25, y=244)

    bt_mundo2 = Button(janelamundo, bd=0, image=img_botaomundo2, command=lambda: [mundo2_Perguntas(janelamundo)])
    bt_mundo2.place(width=195, height=40, x=264, y=244)

    bt_mundo3 = Button(janelamundo, bd=0, image=img_botaomundo3, command=lambda: [mundo3_Perguntas(janelamundo)])
    bt_mundo3.place(width=195, height=40, x=25, y=335)

    bt_mundo4 = Button(janelamundo, bd=0, image=img_botaomundo4, command=lambda: [mundo4_Perguntas(janelamundo)])
    bt_mundo4.place(width=195, height=40, x=264, y=335)

    sair_botao = Button(janelamundo, text="Sair", font=("Arial", 20), bg="#5abceb", fg="yellow",
                        command=lambda: [janelamundo.destroy(), janela.destroy()])
    sair_botao.place(width=162, height=40, x=450, y=430)
    janelamundo.mainloop()
    return janelamundo
