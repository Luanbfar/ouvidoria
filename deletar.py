from operacoesbd import *

connect = abrirBancoDados("localhost", "root", "831920", "bdouvidoria")


def excluir_bd():
    codigo = input("Digite seu codigo, para excluir a ocorrencia: ")
    sql = "select codigo from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    resultado = str(resultado).strip("[](),")
    if codigo in resultado:
        sql = "delete from manifestacoes where codigo =" + codigo
        dados = ()
        excluirBancoDados(connect, sql, dados)
