n = int(input('Digite um Número: '))
t = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        t += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end='\033[m ')
print('\nO número {} foi divisível {}x'.format(n,t))
if t == 2:
    print('Por isso ele é sim um Número Primo!')
else:
    print('Por isso ele não é um Número Primo!')

