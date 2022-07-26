n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('''Tirando as notas {:.1f} e {:.1f} sua média é {:.1f}.
    O aluno está Reprovado.'''.format(n1,n2,media))
elif media >=5 and media <=7:
    #outra opção é 7 > media >=5
    print('''Tirando as notas {:.1f} e {:.1f} sua média é {:.1f}.
    O aluno está em Recuperação.'''.format(n1,n2,media))
elif media >= 7:
    print('''Tirando as notas {:.1f} e {:.1f} sua média é {:.1f}.
    O aluno está Aprovado.'''.format(n1,n2,media))