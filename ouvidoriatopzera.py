from funções import *
import time

opMenu = -1

connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")



print("Bem-vindo(a) ao sistema de ouvidoria!")
print()

while opMenu != 4:
    print(end='Carregando')
    time.sleep(0.2)
    print(end='.')
    time.sleep(0.2)
    print (end='.')
    time.sleep(0.2)
    print('.')
    print()
    print("Opção 1: Listar")
    print("Opção 2: Adicionar")
    print("Opção 3: Excluir")
    print("Opção 4: Sair")
    print()

    opMenu = int(input("Escolha uma opção: "))

    if opMenu == 1:
        listar_bd()
    elif opMenu == 2:
        adicionarFeedback()
    elif opMenu == 3:
        excluir_bd()
    elif opMenu == 4:
        print("Saindo...")
    else:
        print("Opção inválida.")

encerrarBancoDados(connect)
