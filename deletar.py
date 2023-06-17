from operacoesbd import *
connect = abrirBancoDados("localhost", "root", "root", "ouvidoria")
def excluir():
    codigo = input("Digite seu codigo, para excluir a ocorrencia: ")
    sql = "select codigo from manisfetacoes"
    resultado = listarBancoDados(connect, sql )
    resultado = str(resultado).strip("[](),")
    if codigo in resultado:   
        sql = "delete from manifestacoes where codigo =" + codigo
        excluirBancoDados(connect, sql,)