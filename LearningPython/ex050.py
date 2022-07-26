soma = 0
cont = 0
for n in range(1, 7):
    s = int(input('Digite o {}° valor: '.format(n)))
    if s % 2 == 0:
        soma += s
        cont += 1
print('Você digitou {} números pares e a soma dos números foi {}'.format(cont, soma))
