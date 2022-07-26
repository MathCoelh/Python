# AULA SOBRE LAÇOS.
#EX: laço c no intervalo(0,10)
#        passo                #em portugues para entender
#    pega
#for c in range(0,10):
#    passo                    #assim como deve ser feito
#pega
#
#for c in range(0,3):   # o numero 3 é o numero de vezes que o programa precisa repetir dentro do laço
#    passo                #para dentro é o que vai ser repedido no laço
#    pula
#passo pega            # para fora é o que vai ser repedito depois do laço
#
#for c in range(0,3):
#    if (moeda):       #possibilidade de fazer outra ação SE tem alguma coisa pra fazer no caminho.
#        pega
#    passo
#    pula
#passo
#pega
"""
for c in range(0, 6):
    print(c)          # para contar até 6 crescente
print('Fim')

for d in range(6, 0, -1):
    print(d)          # para contar de 6 a 0 decresente
print('Fim')

for e in range(0, 7, 2):  # o terceiro numero (n,n,"esse") é o número da iteração onde você decide se é decresente, etc.
    print(e)          # para contar de 0 a 7 pulando de 2 em 2
print('Fim')

n = int(input('Digite um numero: '))
for f in range(0, f+1):     # o +1 é para que ele conte mais um. O programa conta até aquele numero excluindo o mesmo.
    print(f)
print('Fim')

g = int(input('Início: '))    # o numero que começa
h = int(input('Fim: '))       # o numero final
i = int(input('Passo: '))     # em qual maneira (pulando um, pulando 3, do jeito que quiser)
for j in range(g,  h+1, i):
    print(j)
print('Fim')

s = 0
for k in range(0,5):
    l = int(input('Digite um valor: '))
    s = s + l # ou s+= l - isso é a mesma coisa que s = s + l
print('A Somatória de todos os valores foi {}'.format(s))

end= ' ' - no final do print para ficar na mesma linha."""
