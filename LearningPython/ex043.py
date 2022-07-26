peso = float(input('Digite seu Peso: (KG) '))
altura = float(input('Digite sua Altura: (m) '))
imc = peso / (altura ** 2)
print(' O seu IMC é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está Abaixo do Peso!')
elif 18.5 <= imc < 25:
    print('Parabéns você está no peso Ideal')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso')
elif 30 <= imc < 40:
    print('Você está com Obesidade, Se cuide mais!')
elif imc >= 40:
    print('Você está com Obesidade mórbida, procure um médico imediatamente!')
