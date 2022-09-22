#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#  mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade =float(input('Digite a velocidade Km/h: '))
if velocidade >= 80:
    print('Multado! você excedeu a velocidade. A multa é de R${:.2f}.'.format((velocidade-80)*7))

else:
    print('Você não foi multado parabéns!')   