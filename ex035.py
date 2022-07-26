print('=-='*20)
print('Analisador de Triângulos')
print('=-='*20)
r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo Seguimento: '))
r3 = int(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima Podem Formar um Triângulo')
else:
    print('Os seguimentos acima Não podem Formar um Triângulo')
