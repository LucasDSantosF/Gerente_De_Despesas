from tkinter import *
from tkinter import ttk
from banco import *


def voltar():
    home.destroy()
    login()

def homepage():
    global home
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

    bt_novo = Button(f_novo, text="Enviar" ,fg="#03c", bg="#ff0", font=("Arial",13))
    bt_novo.grid(column=0, row=4, columnspan=2, pady=7)

    # pesquisa
    nsp = Label(f_pesq, bg="#3cc")
    nsp.grid(column=0, row=0, pady=7)

    lb_nome = Label(f_pesq, text="Nome do produto", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_nome.grid(column=0,row=1, sticky="w",padx=10, pady=5)

    e_nome = Entry(f_pesq, fg="#03c", bg="#0ff", font=("Arial",13))
    e_nome.grid(column=1,row=1, sticky="w",padx=10,pady=5)

    bt_novo = Button(f_pesq, text="Pesquisar" ,fg="#03c", bg="#ff0", font=("Arial",13))
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

    bt_alt = Button(f_alt, text="Alterar" ,fg="#03c", bg="#ff0", font=("Arial",13))
    bt_alt.grid(column=0, row=4, columnspan=2, pady=7)

    # Estatísticas
    nsp = Label(f_stat, bg="#3cc")
    nsp.grid(column=0, row=0, pady=7)

    bl_ganho = Label(f_stat, text="Ganho Mensal (R$)", fg="#ff0", bg="#3cc", font=("Arial",13))
    bl_ganho.grid(column=0, row=2, sticky='w',padx=10,pady=5)

    vganho = Label(f_stat, text="200", fg="#03c", bg="#3cc", font=("Arial",13))
    vganho.grid(column=1, row=2, sticky='w',padx=10,pady=5)

    lb_gasto = Label(f_stat, text="Gasto Mensal (R$)", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_gasto.grid(column=0, row=3, sticky='w',padx=10,pady=5)

    vgasto = Label(f_stat, text="120", fg="#03c", bg="#3cc", font=("Arial",13))
    vgasto.grid(column=1, row=3, sticky='w',padx=10,pady=5)

    lb_prod = Label(f_stat, text="5 produtos mais comprados", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_prod.grid(column=0, row=4, sticky='w',padx=10,pady=5)


    # Histórico
    nsp = Label(f_hist, bg="#3cc")
    nsp.grid(column=0, row=0, pady=7)

    lb_prod = Label(f_hist, text="Ultimos 30 dias", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_prod.grid(column=0, row=1, sticky='w',padx=10,pady=5)

    lb_prod = Label(f_hist, text="Histórico Completo", fg="#ff0", bg="#3cc", font=("Arial",13))
    lb_prod.grid(column=0, row=2, sticky='w',padx=10,pady=5)


    # menu opcoes

    Barra = Menu(home)
    menu = Menu(Barra, tearoff=0)
    menu.add_command(label="Saldo")
    menu.add_separator()
    menu.add_command(label="Logout", command=voltar)
    menu.add_command(label="Fechar", command=lambda: home.destroy())
    Barra.add_cascade(label="Opções", menu=menu)

    home.config(menu=Barra)

    home.mainloop()


# Funções Criar Contar

def NovaConta(nome, senha, saldo):
    if nome != "" or senha !="":
        if len(senha) == 7:
            consul = CheckSenha(senha)
            if consul == 1:
                res = CadUser(nome,senha,saldo)
                if res == 1:
                    consulid = ConsulUser(senha)
                    Id = consulid[0][0]
                    app.destroy()
                    homepage()




def CriarConta():
    janela.destroy()
    global app
    app = Tk()
    app.title("Criar Conta")
    app.geometry("700x500")
    app.configure(background="#099")

    Senha = StringVar()

    lb = Label(app, text="Criar Conta", bg="#099", fg="#ff0", font=("Arial", 15))

    lnome = Label(app, text="Nome", bg="#099", fg="#ff0", font=("Arial",13) )
    lsenha = Label(app, text="Senha", bg="#099", fg="#ff0",font=("Arial",13))
    lsaldo = Label(app, text="Saldo", bg="#099", fg="#ff0",font=("Arial",13))

    lnome.grid(column=1, row=2, padx=10)
    lsenha.grid(column=1, row=3, padx=10, pady=7)
    lsaldo.grid(column=1, row=4, padx=10)
    lb.grid(column=1, row=0, pady= 20, columnspan=2)

    enome = Entry(app, bg="#3cc", fg="#ff0", font=("Arial",13))
    esenha = Entry(app, textvariable=Senha, show="@", bg="#3cc", fg="#ff0", font=("Arial",13))
    esaldo = Entry(app, bg="#3cc", fg="#ff0", font=("Arial",13))
    
    enome.grid(column=2, row=2)
    esenha.grid(column=2, row=3)
    esaldo.grid(column=2, row=4)

    bt_cria = Button(app, text="Criar Conta", background="#ff0", fg="#099",font=("Arial",13), command=lambda:NovaConta(enome.get(),esenha.get(),esaldo.get()))
    bt_cria.grid(column=1, row=5, ipadx=17, pady=20, columnspan=2)



    sp = Label(app, bg="#099")
    sp.grid(column=0, row=0, padx=50)


    app.mainloop()
    

# Funções Login

def CheckLogin(nome, senha):

    if nome != "" or senha != "":
        if len(senha) < 7:
            res = ConsulUser(senha)
            if nome == res[0][1] and senha == res[0][2]:
                global Id
                Id = res[0][0]
                janela.destroy()
                homepage()



def login():
    global janela
    janela = Tk()
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

    bt_Entra = Button(janela, text="Entrar", background="#ff0", fg="#099", font=("Arial",13), command=lambda:CheckLogin(enome.get(), Senha.get()))
    bt_cria =  Button(janela, text="Criar Conta", background="#ff0", fg="#099",font=("Arial",13), command=CriarConta)
    bt_Entra.grid(column=2, row=4, ipadx=17)
    bt_cria.grid(column=4, row=4)


    sp = Label(janela, bg="#099")
    sp.grid(column=0, row=0, padx=30)


    janela.mainloop()


login()

