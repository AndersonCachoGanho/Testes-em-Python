# Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúsculas e minúsculas.

from re import S


nome = str(input("Digite seu nome completo: ")).strip()#.strip() elimina espaços laterais
print('Analizando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome, nome.lower()))

#Quantas letras ao todo (sem considerar espaços).
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))#-nome.count(' ') elimina a contagem de espaços entre as frases


#Quantas letras tem o primeiro nome.
epara = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))