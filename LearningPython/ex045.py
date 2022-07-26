from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
pc = randint(0, 4)
print('--' * 20)
print('Bem Vindo ao Jogo: Pedra, Papel, Tesoura, Lagarto, Spock')
print('--' * 20)
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
[ 3 ] Lagarto
[ 4 ] Spock''')
jogador = int(input('Qual é a sua Jogada? '))
print('--' * 12)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('--' * 12)
print('Computador jogou {}'.format(itens[pc]))
print('O Jogador Jogou {}'.format(itens[jogador]))
print('--' * 12)
if pc == 0:         # computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Papel Envolve de Pedra, O Jogador Ganhou!')
    elif jogador == 2:
        print('Pedra Amassa a Tesoura, O Computador Ganhou!')
    elif jogador == 3:
        print('Pedra Esmaga o Lagarto, O Computador Ganhou!')
    elif jogador == 4:
        print('Spock Vaporiza a Pedra, O Jogador Ganhou!')
    else:
        print('Jogada Inválida')
elif pc == 1:       # computador jogou papel
    if jogador == 0:
        print('Papel Envolve a Pedra, O Computador Ganhou!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Tesoura Corta o Papel, O Jogador Ganhou!')
    elif jogador == 3:
        print('Lagarto Come o Papel, O Jogador Ganhou!')
    elif jogador == 4:
        print('Papel Refuta o Spock, O Computador Ganhou!')
    else:
        print('Jogada Inválida')
elif pc == 2:       # computador jogou tesoura
    if jogador == 0:
        print('Pedra Amassa a Tesoura, O Jogador Ganhou!')
    elif jogador == 1:
        print('Tesoura Corta o Papel, O Computador Ganhou!')
    elif jogador == 2:
        print('Empate!')
    elif jogador == 3:
        print('Tesoura Decapita o Lagarto, O Computador Ganhou!')
    elif jogador == 4:
        print('Spock Derrete a Tesoura, O Jogador Ganhou!')
    else:
        print('Jogada Inválida')
elif pc == 3:       # computador jogou Lagarto
    if jogador == 0:
        print('Pedra Esmaga o Lagarto, O Jogador Ganhou!')
    elif jogador == 1:
        print('Lagarto Come o Papel, O Computador Ganhou!')
    elif jogador == 2:
        print('Tesoura Decapita o Lagarto, O Jogador Ganhou!')
    elif jogador == 3:
        print('Empate!')
    elif jogador == 4:
        print('Lagarto Envenena Spock, O Computador Ganhou!')
    else:
        print('Jogada Inválida')
elif pc == 4:       # computador jogou Spock
    if jogador == 0:
        print('Spock Vaporiza a Pedra, O Computador Ganhou!')
    elif jogador == 1:
        print('Papel Refuta Spock, O Jogador Ganhou!')
    elif jogador == 2:
        print('Spock Derrete Tesoura, O Computador Ganhou!')
    elif jogador == 3:
        print('Lagarto Envenena Spock, O Jogador Ganhou!')
    elif jogador == 4:
        print('Empate!')
    else:
        print('Jogada Inválida')
