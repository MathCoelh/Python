a = float(input('Bem vindo, qual o valor da casa?: '))
b = float(input('Qual é o seu Salário atual?: '))
c = float(input('Em quantos anos você pretende pagar?: '))

va = a / c
vm = va / 12
tpc = b * 0.3

if vm <= tpc:
    print('Parabéns seu emprestimo foi aceito! Você pagará mensalidades R${:.2f} por mês!'.format(vm))
else:
    print('Infelizmente seu empréstimo foi Negado')
