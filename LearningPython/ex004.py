algo = input('Digite algo:')
print('O tipo primitivo é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É um alfabeto?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())