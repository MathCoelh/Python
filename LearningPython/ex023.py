nun = int(input('Digite um número: '))
u = nun // 1 % 10
c = nun // 10 % 10
d = nun // 100 % 10
m = nun // 1000 % 10
print('Analisando seu número...')
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(c))
print('Centena: {}'.format(d))
print('Milhar: {}'.format(m))
