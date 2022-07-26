import random
a = input('Digite o Primeiro nome:')
b = input('Digite o Segundo nome:')
c = input('Digite o Terceiro nome:')
d = input('Digite o Quarto nome:')
list = [a,b,c,d]
r = random.choice(list)
print('O escolhido foi: {}'.format(r))
