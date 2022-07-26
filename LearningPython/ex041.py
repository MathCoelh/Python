from datetime import date
ano = int(input('Ano de Nascimento: '))
hoje = date.today().year
idade = hoje - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif 14 >= idade >= 10:
    #outra opção é: 'idade <= 14' porque se ele é maior que 9 automaticamente ele vai para o próximo.
    print('Classificação: INFANTIL')
elif 19 >= idade >= 15:
    #aqui á mesma coisa outra opção é: idade <= 15
    print('Classificação: JUNIOR')
elif 25 >= idade >= 20:
    #aqui a mesma coisa
    print('Classificação: SÊNIOR')
elif idade > 25:
    #aqui a mesma coisa
    print('Classificação: MASTER')
