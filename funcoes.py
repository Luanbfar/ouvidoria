from operacoesbd import *

connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")

def listar_bd(): #função para listar as linhas do banco de dados
    sql = "select * from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    if len(resultado) == 0: #checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações cadastradas.")    
    else:
        for i in resultado: #imprime cada linha separadamente utilizando o hífen para separar os elementos de cada linha
            print(*i, sep=" - ")
            
def listarTipo_bd(): #função para listar as linhas do banco de dados por tipo de manifestação
    sql = "select * from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    if len(resultado) == 0: #checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações no banco de dados.")
    else:
        tipo = input(
            "Digite o tipo de manifestação a ser listada (Reclamação; Sugestão; Elogio): "
        ).capitalize()
        if tipo in ["Reclamação", "Sugestão", "Elogio"]: #checa se o tipo inserido pelo usuário pertence aos tipos válidos
            sql = "select * from manifestacoes where tipo = '{}'".format(tipo)
            resultado = listarBancoDados(connect, sql)
            for i in resultado: #imprime as manifestações com o tipo selecionado separando as colunas com o hífen
                print(*i, sep=" - ")
        else:
            print("Tipo inválido!") #mostra essa mensagem de erro se o tipo inserido for diferente dos tipos válidos

def add_bd(): #função para adicionar manifestação ao banco de dados
    titulo = input("Digite o título da manifestação: ")
    descricao = input("Digite a descrição da manifestação: ")
    autor = input("Digite o nome do autor da manifestação: ")
    tipo = input("Digite o tipo de manisfetação: ").capitalize()
    if tipo not in ["Reclamação", "Sugestão", "Elogio"]: #checa se o tipo inserido pelo usuário pertence aos tipos válidos ou não
        print("Tipo de manifestação inválida!")
    else:
        sql = (
            "insert into manifestacoes (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"
        )
        dados = (titulo, descricao, autor, tipo)
        insertNoBancoDados(connect, sql, dados)
        print("Manifestação criada com sucesso!")

def exibirQnt_bd():
    # Cursor para executar consultas SQL
    cursor = connect.cursor()

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
    connect.close()


def pesquisar_bd(): #função usada para pesquisar manifestações pelo seu código
    codigo = input("Digite o código da manifestação a ser pesquisada: ")
    sql = "select * from manifestacoes where codigo =" + codigo
    resultado = listarBancoDados(connect, sql)

    if len(resultado) == 0: #checa se o código inserido está no banco de dados
        print("Não existe manifestação com o código informado")
    else:
        for i in resultado: #imprime cada linha com valores das colunas separados pelo hífen
            print(*i, sep=" - ")

def editar_bd(): #função para editar título e descrição de manifestações
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


def excluir_bd(): #função para excluir manifestação do banco de dados
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
