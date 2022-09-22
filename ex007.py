# DESENVOLVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UMA ALUNO,CALCULE E MOSTRE SUA MÉDIA.

n1 = float(input('PRIMEIRA NOTA DO ALUNO:  '))
n2 = float(input('SEGUNDA NOTA DO ALUNO:  '))
média = (n1 + n2) / 2
print('A média entre {} e {} é : {}'.format(n1, n2 , média))

# fiz if / else por conta própria e funcionou

if média >= 6 :
    print('Aluno aprovado')

else:
    print('Aluno reprovado')