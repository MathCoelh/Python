r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima Podem formar um Triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
#    if r1 != r2 and r2 != r3 - outra maneira de escrever
#    if r1 == r2 and r2 == r3 - outra maneira de escrever
else:
    print('Os seguimentos acima Não Podem formar um Triângulo')
