#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep #biblioteca de tempo para gerar expectativa antes de dar o resultado
computador = randint(0,5) # faz o computador sortear.
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número pensei? '))# jogador tenta adivinhar
print('-=-'*20)
print('Processando...')
sleep(3)

if jogador == computador: # Se o jogador escolher um número igual ao do computador...
    print('Você acertou!')

else:
    print('Errou! o número correto é {}'.format(computador))