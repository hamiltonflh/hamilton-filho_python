frase=str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "A" aparece primeiro no caractere {} e por último no caractere {}'.format(frase.find("A")+1, frase.rfind("A") -frase.count(' ')+1))