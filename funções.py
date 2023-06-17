from operacoesbd import *
import time

connect = abrirBancoDados("localhost", "root", "831920", "bdouvidoria")

def listar_bd(): #função para listar as linhas do banco de dados
    sql = "select * from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    if len(resultado) == 0: #checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações cadastradas.")
        print()
    else:
        for i in resultado: #imprime cada linha separadamente utilizando o hífen para separar os elementos de cada linha
            print(*i, sep=" - ")
            print()

def adicionarFeedback():
    tipo = input("Digite o tipo de feedback desejado: ").capitalize()

    if not tipo in ["Reclamação", "Sugestão", "Elogio"]:
        print("Manifestação invalida!")
    else:
        if tipo == "Elogio":
            titulo = input("Insira o titulo do seu elogio: ")
            print()
            time.sleep(0.5)

            descricao = input("Digite a descrição da manifestação: ")
            print()
            time.sleep(0.5)
            autor = input("Digite o autor da manifestação: ")
            print()
            time.sleep(0.5)
            sql = "insert into manifestacoes (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"
            dados = (titulo, descricao, autor, tipo)
            insertNoBancoDados(connect, sql, dados)
        elif tipo == "Reclamação":
            titulo = input("Digite o titulo da reclamação: ")
            print()
            time.sleep(0.5)

            descricao = input("Digite a descrição da manifestação: ")
            print()
            time.sleep(0.5)
            autor = input("Digite o autor da manifestação: ")
            print()
            time.sleep(0.5)
            sql = "insert into manifestacoes (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"
            dados = (titulo, descricao, autor, tipo)
            insertNoBancoDados(connect, sql, dados)
        elif tipo == "Sugestão":
            titulo = input("Digite o titulo da sugestão: ")
            print()
            time.sleep(0.5)

            descricao = input("Digite a descrição da manifestação: ")
            print()
            time.sleep(0.5)
            autor = input("Digite o autor da manifestação: ")
            print()
            time.sleep(0.5)
            sql = "insert into manifestacoes (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"
            dados = (titulo, descricao, autor, tipo)
            insertNoBancoDados(connect, sql, dados)

def excluir_bd():
    codigo = input("Digite seu código, para excluir a ocorrência: ")
    sql = "select codigo from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    resultado = str(resultado).strip("[](),")
    if codigo in resultado:
        sql = "delete from manifestacoes where codigo =" + codigo
        dados = ()
        excluirBancoDados(connect, sql, dados)
        print("A ocorrência foi apagada com sucesso!")
    else:
        print("Código inexistente!, tente novamente.")
