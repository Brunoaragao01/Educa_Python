from mundo2 import fechar, mundo2_Perguntas
janela = [1, 2, 3, 4, 5]
img_fundo = [1, 2, 3, 4, 5]
i = 0
global acertos_mundo1, janelamundo
acertos_mundo1 = 0


def encerrar_janelas():
    global acertos_mundo1, i
    for i in janela:
        i.destroy()
        acertos_mundo1 = 0
        i = 0


def resultado_mundo1(janelamundo):

    global acertos_mundo1
    global janela_resultado1
    from tkinter import Button, PhotoImage, Label, Toplevel

    janela_resultado1 = Toplevel(janelamundo)
    janela_resultado1.title("Educa Python")
    janela_resultado1.geometry("640x480+500+153")
    janela_resultado1.resizable(width=False, height=False)
    janela_resultado1.iconbitmap(default="imagens_principal\\Python.ico")

    if acertos_mundo1 > 2:
        img_fundo1 = PhotoImage(file="imagens_mundos/Mundo1/Resultado_Mundo1.png")
    else:
        img_fundo1 = PhotoImage(file="imagens_mundos/Mundo1/Resultado_Mundo1_não_passou.png")
    # Criação de Labels
    lab_fundo = Label(janela_resultado1, image=img_fundo1)
    lab_fundo.pack()
    # Criação de Label das perguntas

    campo1 = Label(janela_resultado1,
                   text=f'Você acertou {acertos_mundo1} respostas',
                   font=("Arial", 20), fg="yellow", justify="center",
                   compound="center", padx=10, bg="#2583a7")
    campo1.place(width=350, height=50, x=120, y=250)

    if acertos_mundo1 > 2:
        proximo_nivel = Button(janela_resultado1,
                               text="Proximo nivel",
                               font=("Arial", 20),
                               bg="#5abceb",
                               fg="yellow",
                               command=lambda: [janela_resultado1.destroy(),
                                                encerrar_janelas(),
                                                mundo2_Perguntas(janelamundo)])
        proximo_nivel.place(width=170, height=40, x=200, y=430)
    else:
        proximo_nivel = Button(janela_resultado1,
                               text="Tentar novamente",
                               font=("Arial", 20),
                               bg="#5abceb",
                               fg="yellow",
                               command=lambda: [encerrar_janelas(),
                                                janela_resultado1.destroy(),
                                                mundo1_perguntas(janelamundo)])
        proximo_nivel.place(width=245, height=40, x=100, y=430)

    sair_botao = Button(janela_resultado1,
                        text="Sair",
                        font=("Arial", 20),
                        bg="#5abceb",
                        fg="yellow",
                        command=lambda: [janela_resultado1.destroy(),
                                         encerrar_janelas()])
    sair_botao.place(width=162, height=40, x=400, y=430)

    janela_resultado1.mainloop()
    return janela_resultado1


def fechar():
    global i
    # print(f'funcao fechar {i}')
    i += 1
    return i
    if i <= 4:
        mundo2_Pergunta1()


def mundo1_perguntas(janelamundo):
    global i
    # if i > 0:
    # janela[i-1].destroy()
    if i > 4:
        resultado_mundo1(janelamundo)
        pass
    if i <= 4:
        global var
        global acertos_mundo1
        var = 0
        from tkinter import Button, Radiobutton, PhotoImage, Label, IntVar, Toplevel
        from random import randint, shuffle
        janela[i] = Toplevel(janelamundo)
        janela[i].title("Educa Python")
        janela[i].geometry("640x480+500+153")
        janela[i].resizable(width=False, height=False)
        janela[i].iconbitmap(default="imagens_principal\Python.ico")

        # variaveis globais
        numero_1 = randint(6,15)
        numero_2 = randint(1,5)

        lista_resultado = [numero_1 + numero_2,(numero_1 + numero_2)+3 ,(numero_1 + numero_2)+5]
        shuffle(lista_resultado)

        #importando imagens

        img_fundo[i] = PhotoImage(file=f'imagens_mundos/Mundo1/Mundo 1_Pergunta{i+1}.png')

        # Criação de Labels
        lab_fundo = Label(janela[i], image=img_fundo[i])
        lab_fundo.pack()
        img_fundo_questoes = PhotoImage(file="imagens_mundos/fundo da tela.png")


        # Criação de Label das perguntas

        campo1 = Label(janela[i], text=f'{numero_1}',font=("Arial",30),fg="yellow", justify="center",compound="center",padx=10,bg="#2583a7")
        campo1.place(width=100,height=80,x=120,y=250)

        campo2 = Label(janela[i], text=f'+',font=("Arial",30),fg="yellow", justify="center",compound="center",padx=5,bg="#2583a7")
        campo2.place(width=50,height=80,x=216,y=250)

        campo3 = Label(janela[i], text=f'{numero_2}',font=("Arial",30),fg="yellow", justify="center",compound="center",padx=10,bg="#2583a7")
        campo3.place(width=150,height=80,x=250,y=250)

        campo4 = Label(janela[i], text=f'=',font=("Arial",30),fg="yellow", justify="center",compound="center",padx=5,bg="#2583a7")
        campo4.place(width=50,height=80,x=350,y=250)

        campo5 = Label(janela[i], text=f'?',font=("Arial",30),fg="yellow", justify="center",compound="center",padx=5,bg="#2583a7")
        campo5.place(width=50,height=80,x=400,y=250)

        def conta():
            global acertos_mundo1

            if var.get() == (numero_1 + numero_2):
                acertos_mundo1 +=1
                #print(acertos_mundo1)
            return acertos_mundo1

        var = IntVar()
        # Criação de Radios Respostas
        texto1 = Label(janela[i], text="(A)",font=("Arial",20),bg="#5abceb",fg="yellow")
        texto1.place(width=40,height=30,x=11,y=430)

        radio1 = Radiobutton(janela[i],text=f'{lista_resultado[0]}',value=lista_resultado[0],variable=var,indicatoron=0,bg="#5abceb",command=conta)
        radio1.place(width=40,height=30,x=60,y=430)
        radio1.deselect()

        texto2 = Label(janela[i], text="(B)",font=("Arial",20),bg="#5abceb",fg="yellow",)
        texto2.place(width=40,height=30,x=200,y=430)

        radio2 = Radiobutton(janela[i],text=f'{lista_resultado[1]}',value=lista_resultado[1],variable=var,indicatoron=0,bg="#5abceb",command=conta)
        radio2.place(width=40,height=30,x=249,y=430)

        texto3 = Label(janela[i], text="(C)",font=("Arial",20),bg="#5abceb",fg="yellow")
        texto3.place(width=40,height=30,x=389,y=430)

        radio3 = Radiobutton(janela[i],text=f'{lista_resultado[2]}',value=lista_resultado[2],variable=var,indicatoron=0,bg="#5abceb",command=conta)
        radio3.place(width=40,height=30,x=438,y=430)

        #Criação de botão

        proxima = Button(janela[i], text="Proximo", font=("Arial",20), bg="#5abceb", fg="yellow", command=lambda:[fechar(), mundo1_perguntas(janelamundo)])
        proxima.place(width=110,height=30,x=510,y=430)



        janela[i].mainloop()
        return janelamundo
#mundo1_Perguntas()


