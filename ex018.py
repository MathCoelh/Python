import math
a = float(input('Digite o número do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O sen é {:.2f}, o cos é {:.2f} e o tang é {:.2f}!'.format(s,c,t))