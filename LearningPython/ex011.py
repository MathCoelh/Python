a = int(input('Digite a Altura de sua Parede: '))
l = int(input('Digite a Largura de sua Parede: '))
area = a * l
tinta = area/2
print('Sua parede tem um total de {} metros², será necessário então {} litros de tinta para pinta-la!'.format(area,tinta))