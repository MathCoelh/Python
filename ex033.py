a = float(input('Digite o Primeiro Número: '))
b = float(input('Digite o Segundo Número: '))
c = float(input('Digite o Terceiro Número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
