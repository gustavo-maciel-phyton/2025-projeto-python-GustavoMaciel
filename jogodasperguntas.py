'''
Projeto: Jogo das perguntas
2025.06.30
Gustavo Maciel da Silva
'''
# Objetivo: Desenvolver um Jogo sobre perguntas e respostas, onde o computador faz as perguntas e o jogador deve responder corretamente para ganhar pontos.

# Espaço para as bibliotecas
from random import randint  # Biblioteca para importar a função randint do módulo random
from time import sleep      # Biblioteca para importar a função sleep do módulo time
from modules import limpaTela, mostraLine, msgCenter, msgLeft, mostraCabecalho, mostraMenu, sortNum, validaValue, getValue, mostraDica, playAgain    # Importa as funções do arquivo modules.py

# Constante
TAM = int(50)     # Tamanho da linha de exibição de caracteres
MAR = int(2)      # Tamanho da margem de exebição
CAR = '_'         # Caractere utilizado para exibir a parte de cima da linha
LAT = '|'         # Caractere utilizado para exibir a parte lateral da linha

# Variaveis
resposta = 0          # Variavel onde fica armazenada a resposta do usuário
msg = ' '         # Variavel onde fica armazenada a mensagem de exibição

# Listas
MSGS = []         # Lista onde ficam armazenada as mensagens de exibição

# Função do jogo
MSGS = []         # Inicializa a lista de mensagem
def playGame():   # Função principal do jogo( onde inicia o jogo)
    global resposta, MSGS    # Declara a variavel global resp e MSGS para serem utilizadas
    limpaTela()       # Função que limpa a tela do terminal
    mostraCabecalho(['JOGO DAS PERGUNTAS', 'Desenvolvido por Gustavo Maciel'])  # Exibe o cabeçalho do jogo
    sleep(6)     # Pausa a execução durante 6 segundos para o usuário ler o cabeçalho
    limpaTela()  # Limpa a tela novamente
    msg = '-> Digite o número correspondente ao nível'
    # Perguntas e respostas sobre divisões
    perguntas = [        # Listas das perguntas e respostas
        {"pergunta": "Quanto é 144 ÷ 12?", "resposta": 12},
        {"pergunta": "Quanto é 58 ÷ 2?", "resposta": 29},
        {"pergunta": "Quanto é 169 ÷ 13?", "resposta": 13},
        {"pergunta": "Quanto é 77 ÷ 7?", "resposta": 11},
        {"pergunta": "Quanto é 128 ÷ 16?", "resposta": 8},
        {"pergunta": "Quanto é 152 ÷ 8?", "resposta": 19},
        {"pergunta": "Quanto é 108 ÷ 9?", "resposta": 12},
        {"pergunta": "Quanto é 196 ÷ 14?", "resposta": 14},
        {"pergunta": "Quanto é 112 ÷ 2?", "resposta": 56},
        {"pergunta": "Quanto é 147 ÷ 3?", "resposta": 49},
    ]

    pontos = 0       # Variavel que armazena os pontos do jogador
    mostraCabecalho(["Perguntas de Divisão"])    # Exibe o cabeçalho das perguntas
    for i, q in enumerate(perguntas, 1):        # Loop para exibir todas as perguntas
        mostraCabecalho([f"Pergunta {i} de {len(perguntas)}"])     # Exibe o número da pergunta atual
        print(q["pergunta"])         # Exibe a pergunta atual
        try:         # Tenta capturar a resposta do usuário
            resposta = int(input("Sua resposta: "))       # Captura a resposta do usuário e converte para um número inteiro
        except ValueError:      # Caso ocorra um erro de conversão, exibe uma mensagem de erro
            resposta = None     # Mensagem de erro exibida
        if resposta == q["resposta"]:     # Verifica se a resposta está correta
            print("Boa!")      # Se estiver correta exibe mensagem de acerto
            pontos += 1         # Aumenta 1 em pontos  do jogador
        else:          # Caso a resposta esteja errada, exibe mensagem de erro
            print(f"Errrouuuu! A resposta certa é {q['resposta']}.")       # Mensagem de erro exibida e resposta correta
        sleep(1.5)     # Pausa a execução para o usuário ler a mensagem

    limpaTela()     # Limpa a tela novamente
    mostraCabecalho(["Fim do Jogo"])      # Exibe o cabeçalho de fim de jogo
    print(f"Você acertou {pontos} de {len(perguntas)} perguntas.")    # Exibe a quantidade de acertos do jogador
    if playAgain():     # Pergunta se o jogador deseja jogar novamente
        playGame()      # Se sim, chama a função principal e inicia o jogo novamente
if __name__ == "__main__":      # Chama a função principal do jogo
    playGame()         # Inicia o jogo