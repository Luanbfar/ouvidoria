from funções import *
import time

opMenu = -1

connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")

print("Bem-vindo(a) ao sistema de ouvidoria!")
print()
print('Carregando', end='')
for i in range(3):
    time.sleep(0.2)
    print(".", end='')

while opMenu != 5:
    print()
    print("Opção 1: Listar")
    print("Opção 2: Adicionar")
    print("Opção 3: Excluir")
    print("Opção 4: Editar")
    print("Opção 5: Sair")
    print()

    opMenu = int(input("Escolha uma opção: "))

    if opMenu == 1:
        listar_bd()
    elif opMenu == 2:
        adicionarFeedback()
    elif opMenu == 3:
        excluir_bd()
    elif opMenu == 4:
        editar_bd()
    elif opMenu == 5:
        print("Saindo do Sistema", end='')
        for i in range(3):
            time.sleep(0.2)
            print(".", end='')
    else:
        print("Opção inválida.")

encerrarBancoDados(connect)
