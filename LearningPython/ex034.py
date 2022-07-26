salario = float(input('Qual é o Salário?: '))
aumento = salario + (salario * 0.10 if salario >= 1250 else salario * 0.15)
print('Quem recebia R${:.2f} agora recebe R${:.2f}!'.format(salario, aumento))
#outra opção talvez melhor
"""
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)"""