v = float(input('Digite a Velocidade do seu veículo: '))
n = 80
if v < n:
    print('Tenha um bom dia, dirija com segurança!')
else:
    m = v - n
    t = m * 7
    print("""Você foi multado por tansita acima da velocidade
Sua multa é de R${},00""".format(t))



