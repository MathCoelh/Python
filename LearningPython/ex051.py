primeiro = int(input('Digite o Primeiro número: '))
intervalo = int(input('Digite o Intervalo: '))
decimo = primeiro + (10 - 1) * intervalo
for c in range(primeiro, decimo + intervalo, intervalo):
    print('{}'.format(c), end=' >> ')
print('Fim')
