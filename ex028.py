import random
n = int(input("""Olá, acabei de pensar em um número, vamos ver se você adivinha?"
Digite o número que você acha que eu pensei!: """))
numero = random.randint(0, 5)
if n == numero:
    print('PARABÉNS VOCÊ GANHOU!')
else:
    print('O COMPUTADOR GANHOU!')
