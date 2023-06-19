def pesquisar():
    cod = input("Digite o codigo da manifestação a ser pesquisada: ")
    sql = "select * from manifestacoes where codigo =" + codigo
    resultado = listarBancoDados(connect, sql)

    if len(resultado) == 0:
        print('Não existe manifestação com o codigo informado')
    else:
        for i in resultado:
            print(*i, sep=" - ")