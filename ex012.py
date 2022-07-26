atual = float(input('Digite o Preço do Produto: '))
desc = atual*0.05
desconto = atual-desc
print('O preço do produto na liquidação é: R${} '.format(desconto))