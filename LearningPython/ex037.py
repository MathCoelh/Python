n = int(input('Digite o Número: '))
q = int(input("""Das opções a baixo:
    1 para Binário'
    2 para Octal'
    3 para Hexadecimal
Qual será a Base de Conversão?: """))

if q == 1:
    print('Seu número Binário é {}'.format(bin(n)[2:]))
elif q == 2:
    print('Seu número Octal é {0:o}'.format(n))
elif q == 3:
    print('Seu número Hexadecimal é {0:x}'.format(n))
else:
    print('Opção Inválida, tente novamente.')
