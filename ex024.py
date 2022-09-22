# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Em que cidade você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

#strip e uper servem para o programa não dar erro
#quando o usuario digita errado a palavra santo