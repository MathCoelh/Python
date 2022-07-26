"""ano = int(input('Digite o seu ano de nascimento: '))
idade = 2022 - ano
alistar = 18 - idade
print('Quem nasceu em {} tem {} anos em 2022.'.format(ano,idade))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('''Ainda faltam {} anos para o alistamento.
    Seu alistamento será em {}'''.format(alistar, (alistar + 2022)))
elif idade > 18:
    print('''Você já deveria ter se alistado há {} anos.
    Seu alistamento foi em {}'''.format(idade - 18,2022 - alistar))"""

from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa se alistar Imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format())
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format())