"""
ANSI = scape sequence
\033[estilo;text;background;m
ex:
\033[0;33;44m
style: 0 (nada) 1 (bold) 4 (sublinhado) 7 (negativo)
text: 30 (branco) 31 (vermelho) 32 (verde) 33 (amarelo) 34 (azul) 35 (rosa) 36 (azul agua) 37 (marrom)
back(fundo): 40 (branco) 41 (vermelho) 42 (verde) 43 (amarelo) 44 (azul) 45 (rosa) 46 (azul agua) 47 (marrom)

\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m

print('\033[7;33mOlá, Mundo!\033[m')
#outra opção
nome = 'Matheus'
print('Bem Vindo {}{}{}'.format('\033[1;31;47m', nome, '\033[m'))

#para lista de cores """
nome = 'Matheus'
cores = {'limpo':'\033[m', 'vermelho':'\033[31m', 'pretoebranco':'\033[7;32m'}
print('Olá {}!{}!{}!'.format(cores['vermelho'], nome, cores['limpo'], cores['pretoebranco']))

