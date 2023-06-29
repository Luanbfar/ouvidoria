from operacoesbd import *


def listarManifestacoes(): #função para listar as linhas do banco de dados
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    sql = "select * from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    if len(resultado) == 0: #checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações cadastradas.")    
    else:
        for i in resultado: #imprime cada linha separadamente utilizando o hífen para separar os elementos de cada linha
            print(*i, sep=" - ")
            
def listarManifestacoesTipo(): #função para listar as linhas do banco de dados por tipo de manifestação
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    tipo = int(input("Digite o tipo de manifestação a ser listada (1 - Reclamação; 2 - Sugestão; 3 - Elogio): "))

    if tipo == 1:
        tipo_selecionado = "Reclamação"
    elif tipo == 2:
        tipo_selecionado = "Sugestão"
    elif tipo == 3:
        tipo_selecionado = "Elogio"
    else:
        print("Opção inválida!")
        return

    sql = "select * from manifestacoes where tipo = '{}'".format(tipo_selecionado)
    resultado = listarBancoDados(connect, sql)

    if len(resultado) == 0: #checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações desse tipo no banco de dados.")
    else:
        for i in resultado: #imprime as manifestações com o tipo selecionado separando as colunas com o hífen
            print(*i, sep=" - ")

def addManifestacao(): #função para adicionar manifestação ao banco de dados
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    titulo = input("Digite o título da manifestação: ")
    descricao = input("Digite a descrição da manifestação: ")
    autor = input("Digite o nome do autor da manifestação: ")
    tipo = input("Digite o tipo de manisfetação: ").capitalize()
    print("Selecione o tipo de manifestação:")
    print("1. Reclamação")
    print("2. Sugestão")
    print("3. Elogio")

    opcao = int(input("Digite o número correspondente à opção: "))

    if opcao == 1:
        tipo = "Reclamação"
    elif opcao == 2:
        tipo = "Sugestão"
    elif opcao == 3:
        tipo = "Elogio"
    else:
        print("Opção inválida!")
        return
    
    sql = 'insert into manifestacoes (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)'
    dados = (titulo, descricao, autor, tipo)
    insertNoBancoDados(connect, sql, dados)
    print('Manifestação criada com sucesso!')

def exibirQntManifestacoes(): #função para exibir a quantiade de manifestações cadastradas no total e por tipo
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    sql = "select count(tipo) from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    print("{} Manifestação(ões)".format(resultado[0][0])) #mostra a quantidade de manifestações total
    sql = "select count(tipo) from manifestacoes where tipo = 'Reclamação'"
    resultado = listarBancoDados(connect, sql)
    print("{} Reclamação(ões)".format(resultado[0][0])) #mostra a quantiade de reclamações
    sql = "select count(tipo) from manifestacoes where tipo = 'Sugestão'"
    resultado = listarBancoDados(connect, sql)
    print("{} Sugetão(ões)".format(resultado[0][0])) #mostra a quantiade de sugestões
    sql = "select count(tipo) from manifestacoes where tipo = 'Elogio'"
    resultado = listarBancoDados(connect, sql)
    print("{} Elogio(s)".format(resultado[0][0])) #mostra a quantiade de elogios


def pesquisarManifestacao(): #função usada para pesquisar manifestações pelo seu código
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    codigo = input("Digite o código da manifestação a ser pesquisada: ")
    sql = "select * from manifestacoes where codigo =" + codigo
    resultado = listarBancoDados(connect, sql)

    if len(resultado) == 0: #checa se o código inserido está no banco de dados
        print("Não existe manifestação com o código informado")
    else:
        for i in resultado: #imprime cada linha com valores das colunas separados pelo hífen
            print(*i, sep=" - ")

def editarManifestacao(): #função para editar título e descrição de manifestações
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    codigo = input("Digite o código da manifestação a ser editada: ")
    sql = "select codigo from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    resultado = str(resultado).strip("[](),")
    if codigo in resultado: #checa se o código inserido é válido e procede para a próxima etapa
        titulo = input("Digite o novo título: ")
        descricao = input("Digite a nova descrição: ")
        sql = "update manifestacoes set titulo = %s, descricao = %s where codigo = %s"
        dados = (titulo, descricao, codigo)
        atualizarBancoDados(connect, sql, dados)
        print("Manifestação editada com sucesso!")
    else:
        print("Código inválido")


def excluirManifestacao(): #função para excluir manifestação do banco de dados
    connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")
    codigo = input("Digite seu código para excluir a ocorrência: ")
    sql = "select codigo from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    resultado = str(resultado).strip("[](),")
    if codigo in resultado: #checa se o código pertence ao banco de dados e procede para os próximos passos
        sql = "delete from manifestacoes where codigo =" + codigo
        dados = ()
        excluirBancoDados(connect, sql, dados)
        print("A ocorrência foi apagada com sucesso!")
    else:
        print("Código inexistente! Tente novamente.")
