'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

#ALTERNATIVA COMUM

'''import math
ângulo = float(input("Digite o ãngulo que você deseja: "))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ângulo,seno))
print('O ângulo de {} tem o  COSSENO de {:.2f}.'.format(ângulo,cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ângulo,tangente))'''

# ALTERNATIVA IMPORTANDO APENAS OS MÉTODOS

from math import radians, sin, cos, tan

ângulo = float(input("Digite o ãngulo que você deseja: "))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ângulo,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ângulo,cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ângulo,tangente))
