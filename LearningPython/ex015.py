km = float(input('Digite a Quantidade de Km:'))
d = int(input('Digite a quantidade de dias usados:'))
custo = d * 60
custokm = km * 0.15
t = custo + custokm
print('O valor dos dias usados é R${}, o valor dos kms usados é R${} e o valor total a pagar é R${}'.format(custo,custokm,t))
