'''
Arquivos de unões utilizadas
2025.06.25
Gustavo Maciel
'''

# Objetivos: Criar um arquivo de funçõe que seão utilizadas em nossos Projetos

#BIBLIOTECAS
from random import randint    # Importa a função randint da biblioteca random

# CONSTANTE
TAM = int(38)   # Tamanho da tela
MAR = int(2)    # Tamanho da margem
CAR = '_'       # Caractere utilizado para desenhar a linha
LAT = '|'
# VARIÁVEIS


# LISTAS



# FUNÇOES

# Função pra limpar a tela (fingir)
def limpaTela():
    print('\n'*TAM)

# Função para desenhar uma linha
def mostraLine():
    print(f'{CAR}'*TAM)

#Função para mostrar a MSG Centralia
def msgCenter(msg):
    print(f'{LAT} {msg:^{TAM-MAR-MAR}} {LAT}')

# Função pra mostrar uma msg a esquerda
def msgLeft(msg):
    print(f'{LAT} {msg:<{TAM-MAR-MAR}} {LAT}')

# Função para mostrar Cabeçalho
def mostraCabecalho(MSGS):
    mostraLine()
    for msg in MSGS:
        msgCenter(msg)
    mostraLine()

# Função para mostrar Menu
def mostraMenu(MSGS):
    mostraLine()
    for msg in MSGS:
        msgLeft(msg)
    mostraLine()

# Função pra sortear um número
def sortNum(limite):
    key = randint(1, limite)
    return key

#Função para validar as entradas
def validaValue(resp, opcoes):
    if resp in opcoes:
        return True
    else:
        MSGS = [f'{resp} <- Esta reposta ta errada, seu analfabeto.', f'Põe uma dessas {opcoes}']
        mostraMenu(MSGS)
        return False

# Função para obter a entrada do usuario
def getValue(msg):
    resp = input(f'{LAT} {msg}: ').strip()
    return resp

# Função mostra dica
def mostraDica(resp, key):
    if resp > key:
        mostraCabecalho(['Tente um número menor!'])
    else:
        mostraCabecalho(['Tente um número maior!'])

# Função praprguntar se ele quer jogar de novo
def playAgain ():
    opcoes = ['1', '0']
    mostraCabecalho(['Deseja jogar novamente?', '[1] Sim', '[0] Não'])
    resp = getValue('Escolha uma opção')
    return resp == '1'
