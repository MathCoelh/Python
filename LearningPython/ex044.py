print('{:=^40}'.format('Lojas MM'))
valor = int(input('Valor das compras: R$ '))
print('''Formas de Pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a Opção? '))
if opção == 1:
    total = valor - (valor * 0.10)
    print('Sua Compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,total))
elif opção == 2:
    total = valor - (valor * 0.05)
    print('Sua Compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
elif opção == 3:
    total = valor
    print('Sua Compra total é de R${:.2f} parcelado em 2 vezes de R${:.2f}.'.format(total,total / 2))
elif opção == 4:
    vz = int(input('Em quantas vezes gostaria de Parcelar?: '))
    total = valor + (valor * 0.20)
    print('Sua Compra de R${:.2f} vai custar R${:.2f} com juros no final parcelado em {} vezes de R${:.2f}'.format(valor, total , vz, total / vz))
else:
    opção = 0
    print('Opção inválida por favor tente novamente!')
