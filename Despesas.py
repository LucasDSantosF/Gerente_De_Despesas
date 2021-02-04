from tkinter import *
from tkinter import ttk


janela = Tk()

def homepage():
    janela.destroy()
    home = Tk()
    home.title("Home")
    home.geometry("700x500")
    home.configure(background="#099")

    nb = ttk.Notebook(home)
    nb.pack()

    f_novo = Frame(nb, bg="#3cc")
    f_stat = Frame(nb, bg="#3cc")
    f_hist = Frame(nb, bg="#3cc")
    f_pesq = Frame(nb, bg="#3cc")
    f_alt = Frame(nb, bg="#3cc")
    
    nb.add(f_novo, text='Novo Produto')
    nb.add(f_pesq, text='Pesquisa')
    nb.add(f_alt, text="Alterar")
    nb.add(f_stat, text="Estatísticas")
    nb.add(f_hist, text="Histórico")
    

    # Novo Produto
    nsp = Label(f_novo, bg="#3cc")
    nsp.grid(column=0, row=0, pady=7)

    lb_nome = Label(f_novo, text="Nome do produto", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_valor = Label(f_novo, text="Valor(R$)", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_pag = Label(f_novo, text="Tipo de pagamento", fg="#ff0", bg="#3cc", font=("Arial",13))

    lb_nome.grid(column=0,row=1, sticky="w",padx=10, pady=5)
    lb_valor.grid(column=0, row=2, sticky='w',padx=10,pady=5)
    lb_pag.grid(column=0, row=3, sticky='w',padx=10,pady=5)

    e_nome = Entry(f_novo, fg="#03c", bg="#0ff", font=("Arial",13))
    e_valor = Entry(f_novo, fg="#03c", bg="#0ff", font=("Arial",13))
    e_pag = Entry(f_novo, fg="#03c", bg="#0ff", font=("Arial",13))

    e_nome.grid(column=1,row=1, sticky="w",padx=10,pady=5)
    e_valor.grid(column=1,row=2, sticky="w",padx=10,pady=5)
    e_pag.grid(column=1,row=3, sticky="w",padx=10,pady=5)

    bt_novo = Button(f_novo, text="Enviar" ,fg="#3cc", bg="#ff0", font=("Arial",13))
    bt_novo.grid(column=0, row=4, columnspan=2, pady=7)

    # pesquisa
    nsp = Label(f_pesq, bg="#3cc")
    nsp.grid(column=0, row=0, pady=7)

    lb_nome = Label(f_pesq, text="Nome do produto", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_nome.grid(column=0,row=1, sticky="w",padx=10, pady=5)

    e_nome = Entry(f_pesq, fg="#03c", bg="#0ff", font=("Arial",13))
    e_nome.grid(column=1,row=1, sticky="w",padx=10,pady=5)

    bt_novo = Button(f_pesq, text="Pesquisar" ,fg="#3cc", bg="#ff0", font=("Arial",13))
    bt_novo.grid(column=0, row=2, columnspan=2, pady=7)

    # Alterar
    nsp = Label(f_alt, bg="#3cc")
    nsp.grid(column=0, row=0, pady=7)

    lb_nome = Label(f_alt, text="Nome do produto", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_nome.grid(column=0,row=1, sticky="w",padx=10, pady=5)

    e_nome = Entry(f_alt, fg="#03c", bg="#0ff", font=("Arial",13))
    e_nome.grid(column=1,row=1, sticky="w",padx=10,pady=5)

    lb_novo = Label(f_alt, text="Novo Nome", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_novo.grid(column=0,row=2, sticky="w",padx=10, pady=5)

    e_novo = Entry(f_alt, fg="#03c", bg="#0ff", font=("Arial",13))
    e_novo.grid(column=1,row=2, sticky="w",padx=10, pady=5)

    bt_alt = Button(f_alt, text="Alterar" ,fg="#3cc", bg="#ff0", font=("Arial",13))
    bt_alt.grid(column=0, row=4, columnspan=2, pady=7)

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
