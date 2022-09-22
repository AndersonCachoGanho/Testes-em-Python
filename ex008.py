# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E MOSTRE EM CENTIMETROS E MILIMETROS.

medida = float(input('Medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm ))