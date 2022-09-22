#faça um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor.
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
#print(' O valor de {} tem como antecessor o número {} e como sucessor o número {}'.format( n, a, s))
print(' O valor de {} tem como antecessor o número {} e como sucessor o número {}'.format( n, (n - 1 ), (n + 1)))