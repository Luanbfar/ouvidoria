import time
from operacoesbd import *

connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")

def adicionarPorTipo():
    tipo = input ('Digite o tipo de feedback desejado: ').capitalize()
    
    if not tipo == ["Reclamação", "Sugestão", "Elogio"]:
        print ("Manifestação invalida!")
    else:
        if tipo == 'Elogio':
            titulo = input('Insira o titulo do seu elogio :): ')
            print()
            time.sleep(0.5)
           
          
        elif tipo == 'Reclamação':
            titulo = input('Digite o titulo da reclamação: ')
            print()
            time.sleep(0.5)
        
    
        elif tipo == 'Sugestão':
            titulo = input('Digite o titulo da sugestão: ')
            print()
            time.sleep(0.5)
    
    
    
    descricao = input ('Digite a descrição da manifestação: ')
    
    autor = input ('Digite o autor da manifestação: ')
    sql = "insert into manifestacoes (titulo, descricao, autor, tipo) values (%s, %s, %s, %s)"
    dados = (titulo, descricao, autor, tipo)
    insertNoBancoDados(connect,sql, dados)