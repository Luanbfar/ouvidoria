import mysql.connector


def abrirBancoDados(host, user, password, database):
    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


def encerrarBancoDados(connection):
    connection.close()


def insertNoBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id


def listarBancoDados(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results


def atualizarBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas


def excluirBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas


def obterQuantidadesManifestacoes(cursor):
    # Query to get the overall quantity of manifestations
    consulta_geral = "SELECT COUNT(*) FROM manifestacoes"
    cursor.execute(consulta_geral)
    quantidade_geral = cursor.fetchone()[0]

    # Query to get the quantity of complaints
    consulta_reclamacoes = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'reclamacao'"
    cursor.execute(consulta_reclamacoes)
    quantidade_reclamacoes = cursor.fetchone()[0]

    # Query to get the quantity of compliments
    consulta_elogios = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'elogio'"
    cursor.execute(consulta_elogios)
    quantidade_elogios = cursor.fetchone()[0]

    # Query to get the quantity of suggestions
    consulta_sugestoes = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'sugestao'"
    cursor.execute(consulta_sugestoes)
    quantidade_sugestoes = cursor.fetchone()[0]

    return quantidade_geral, quantidade_reclamacoes, quantidade_elogios, quantidade_sugestoes
