km = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(km))
"""if km < 200:
    preço = km / 2
    print('Sua viágem vai custa R${:.2f}'.format(preço))
else:
    preço2 = km * 0.45
    print('Sua viagem vai custar {:.2f}'.format(preço2))"""
preço = km *0.50 if km <= 200 else km * 0.45
print('E o Preço da sua Passagem será de R${:.2f}'.format(preço))
