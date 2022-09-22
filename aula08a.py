from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num,floor(raiz))) 
#floor arredonda para baixo ,ceil arredonda para cima
#from math import sqrt - importa apenas a função desejada, no caso raiz quadrada

