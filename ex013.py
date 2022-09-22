#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Qual é o salário do funcionário? R$'))
novo =  salário + (salário * 15/100)
print('O salário com reajuste de 15% é R${}'.format(novo))