print('Digite 4 números abaixo: ')
num = (int(input('Digite um número:')), 
int(input('Digite outro número: ')), 
int(input('Digite mais um número: ')), 
int(input('Digite o ultimo número')))
print(f'Você digitou {num}')
cont = 0
# > meu raciocínio:
#for c in range(0, len(num)):
#  if num[c] == 9:
#    cont += 1
#print(f'O número 9 apareceu {cont} vezes.')

# > mas tambem posso fazer assim:
print(f'O número 9 apareceu {num.count(9)} vezes.')
print(f'O número 3 aparceu na {num.index(3) + 1}° posição.')
  