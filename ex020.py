import random
a = input('Digite o Primeiro nome:')
b = input('Digite o Segundo nome:')
c = input('Digite o Terceiro nome:')
d = input('Digite o Quarto nome:')
list = [a,b,c,d]
random.shuffle(list)
print('A ordem de apresentação é {}'.format(list))