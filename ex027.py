# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu segundo nome é {}'.format(nome[len(nome)-1]))