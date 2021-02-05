import os
import sqlite3

pasta = os.path.dirname(__file__)

def Conexao():
    caminho = pasta+"\\despesas.db"
    cone = None
    try:
        cone = sqlite3.connect( caminho )
    except:
        print('ERRO CONEC')

    return cone


vcone = Conexao()


def CadUser(nome, senha, saldo):
    dados = f"""INSERT INTO tb_user
            (NOME, SENHA, SALDO)
        VALUES("{nome}","{senha}","{saldo}")"""
    try:
        c = vcone.cursor()
        c.execute(dados)
        vcone.commit()
        print("Foi user")
        return 1
    except:
        print("nao user")
        return 0


def CadProduto(Id, produto, valor, pag, data):

    dados = f"""INSERT INTO tb_despesas
            ( ID, PRODUTO, VALOR, PAGAMENTO, DATA)
        VALUES("{Id}","{produto}","{valor}","{pag}","{data}")"""

    try:
        c = vcone.cursor()
        c.execute(dados)
        vcone.commit()
        return 1
        print('deu bom')
    except:
        print("deu ruim")
        return 0


def ConsulProduto(Id):
    Dados = f" SELECT * FROM tb_despesas WHERE ID LIKE '%{Id}%'"

    c = vcone.cursor()
    c.execute(Dados)
    resultado = c.fetchall()
    print("Dados Consultados")
    return resultado


def ConsulUser(senha):
    Dados = f" SELECT * FROM tb_user WHERE SENHA LIKE '%{senha}%'"

    c = vcone.cursor()
    c.execute(Dados)
    resultado = c.fetchall()
    print("Dados Consultados")
    return resultado


def Atualizar(novo, Id):
    Dados = f"UPDATE tb_despesas SET PRODUTO='{novo}' WHERE local_ID={Id}"
    try:
        c = vcone.cursor()
        c.execute(Dados)
        vcone.commit()
        print("Dados Atualizados")
    except:
        print("ERRO")



def CheckSenha(senha):
    Dados = f" SELECT * FROM tb_user WHERE SENHA='{senha}'"

    c = vcone.cursor()
    c.execute(Dados)
    resultado = c.fetchall()

    if resultado == []:
        print("foi senha")
        return 1
    else:
        print("nao Foi senha")
        return 0
