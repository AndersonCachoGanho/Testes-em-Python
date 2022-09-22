# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da Parede: '))
alt = float(input('Altura da parede: '))
área = larg*alt
tinta = área/2
print('A sua parede tem {} x {} e sua área em m² é {:.2f}'.format(larg, alt, área))
print('Para pintar essa parede você precisará de {:.2f} l de tinta'.format(tinta))