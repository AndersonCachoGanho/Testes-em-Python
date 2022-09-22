# CRIE UM PROGRAMA QUE MOSTRE QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E QUANTOS DÓLARES ELA PODE COMPRAR
#CONSIDERE US$1,00 = R$5,10
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.10
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))