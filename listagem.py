from operacoesbd import *

opMenu = -1

connect = abrirBancoDados("localhost", "root", "12345", "bdouvidoria")


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

print("Bem-vindo(a) ao sistema de ouvidoria!")
print()

while opMenu != 3:
    print("Opção 1: Listar")
   #print("Opção 2: Listar por tipo")
    print("Opção 3: Sair")
    print()

    opMenu = int(input("Escolha uma opção: "))

    if opMenu == 1:
        listar_bd()
   #elif opMenu == 2:
   #   listarTipo()
    elif opMenu == 3:
        print("Saindo...")
    else:
        print("Opção inválida.")

encerrarBancoDados(connect)
