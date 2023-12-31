from funcoes import *

opMenu = -1

connect = abrirBancoDados("localhost", "root", "password", "bdouvidoria")



print("Bem-vindo(a) ao sistema de ouvidoria!")

while opMenu != 8:
    print()
    print("Opção 1: Listar as manifestações")
    print("Opção 2: Listar manifestação por tipo")
    print("Opção 3: Criar nova manifestação")
    print("Opção 4: Exibir quantidade de manifestações")
    print("Opção 5: Pesquisar uma manifestação por código")
    print("Opção 6: Alterar o Título e Descrição de uma Manifestação")
    print("Opção 7: Excluir uma Manifestação pelo Código")
    print("Opção 8: Sair do Sistema")
    print()

    opMenu = int(input("Escolha uma opção: "))

    if opMenu == 1:
        listarManifestacoes()
    elif opMenu == 2:
        listarManifestacoesTipo()
    elif opMenu == 3:
        addManifestacao()
    elif opMenu == 4:
        exibirQntManifestacoes()
    elif opMenu == 5:
        pesquisarManifestacao()
    elif opMenu == 6:
        editarManifestacao()
    elif opMenu == 7:
        excluirManifestacao()
    elif opMenu == 8:
        print("Saindo...")
    else:
        print("Opção inválida. Digite novamente")

encerrarBancoDados(connect)
