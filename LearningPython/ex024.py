nome = input('Digite a Cidade em que você nasceu: ')
espaço = nome.strip()
minusculo = espaço.lower()
primeira = minusculo.title()
frase = 'Santo' in primeira
print(frase)
