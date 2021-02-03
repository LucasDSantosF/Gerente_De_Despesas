from tkinter import *
from tkinter import ttk


janela = Tk()

def homepage():
    janela.destroy()
    home = Tk()
    home.title("Home")
    home.geometry("700x500")
    home.configure(background="#099")

    

    home.mainloop()


def login():
    janela.title("Login Despesas")
    janela.geometry("700x500")
    janela.configure(background="#099")

    Senha = StringVar()

    lb = Label(janela, text="Login", bg="#099", fg="#ff0", font=("Arial", 15))

    lnome = Label(janela, text="Nome", bg="#099", fg="#ff0", font=("Arial",13) )
    lsenha = Label(janela, text="Senha", bg="#099", fg="#ff0",font=("Arial",13))

    lnome.grid(column=1, row=3, pady=50, padx=10)
    lsenha.grid(column=3, row=3, padx=10)
    lb.grid(column=3, row=0, pady= 20)

    enome = Entry(janela, bg="#3cc", fg="#ff0", font=("Arial",13))
    esenha = Entry(janela, textvariable=Senha, show="@", bg="#3cc", fg="#ff0", font=("Arial",13))
    
    enome.grid(column=2, row=3)
    esenha.grid(column=4, row=3)

    bt_Entra = Button(janela, text="Entrar", background="#ff0", fg="#099", font=("Arial",13), command=homepage)
    bt_cria =  Button(janela, text="Criar Conta", background="#ff0", fg="#099",font=("Arial",13))
    bt_Entra.grid(column=2, row=4, ipadx=17)
    bt_cria.grid(column=4, row=4)


    sp = Label(janela, bg="#099")
    sp.grid(column=0, row=0, padx=30)


    janela.mainloop()


login()
