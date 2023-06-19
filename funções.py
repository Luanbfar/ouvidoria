from operacoesbd import *
import time

connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")


def listar_bd():  # função para listar as linhas do banco de dados
    sql = "select * from manifest"
    resultado = listarBancoDados(connect, sql)
    if len(resultado) == 0:  # checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações cadastradas.")
        print()
    else:
        for i in resultado:  # imprime cada linha separadamente utilizando o hífen para separar os elementos de cada linha
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

def exibirQnt():
    # Cursor para executar consultas SQL
    cursor = conexao.cursor()

    # Consulta para obter a quantidade geral de manifestações
    consulta_geral = "SELECT COUNT(*) FROM manifestacoes"
    cursor.execute(consulta_geral)
    quantidade_geral = cursor.fetchone()[0]

    # Consulta para obter a quantidade de reclamações
    consulta_reclamacoes = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'reclamacao'"
    cursor.execute(consulta_reclamacoes)
    quantidade_reclamacoes = cursor.fetchone()[0]

    # Consulta para obter a quantidade de elogios
    consulta_elogios = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'elogio'"
    cursor.execute(consulta_elogios)
    quantidade_elogios = cursor.fetchone()[0]

    # Consulta para obter a quantidade de sugestões
    consulta_sugestoes = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'sugestao'"
    cursor.execute(consulta_sugestoes)
    quantidade_sugestoes = cursor.fetchone()[0]

    # Exibição dos resultados
    print("Quantidade Geral de Manifestações:", quantidade_geral)
    print("Quantidade de Reclamações:", quantidade_reclamacoes)
    print("Quantidade de Elogios:", quantidade_elogios)
    print("Quantidade de Sugestões:", quantidade_sugestoes)

    # Fechando a conexão e o cursor
    cursor.close()
    conexao.close()


print("Quantidade Geral de Manifestações:", quantidade_geral)
print("Quantidade de Reclamações:", quantidade_reclamacoes)
print("Quantidade de Elogios:", quantidade_elogios)
print("Quantidade de Sugestões:", quantidade_sugestoes)

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


def editar_bd():
    cod = input("Digite o código da manifestação a ser editada: ")
    sql = "select cod from manifest"
    resultado = listarBancoDados(connect, sql)
    resultado = str(resultado).strip("[](),")
    if cod in resultado:
        titulo = input("Digite o novo título: ")
        descr = input("Digite a nova descrição: ")
        sql = "update manifest set titulo = %s, descr = %s where cod = %s"
        dados = (titulo, descr, cod)
        atualizarBancoDados(connect, sql, dados)
        print("Manifestação editada com sucesso!")
    else:
        print("Código inválido")
