import random
from time import sleep
print('Sou seu computador e vou pensar em 5 números aleatórios e falarei qual é o maior e qual o menor entre eles.')

print('='*50)
print('Lista dos números que eu pensei')
num = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
for c in range(0, 5):
  print(f'{num[c]} -' if c < 4 else f'{num[c]}', end = ' ')
maior = 0
menor = 0
for c in range(0, 5):
  if c == 1:
    maior = num[c]
    menor = num[c]
  else:
    if num[c] > maior:
      maior = num[c]
    if num[c] < menor:
      menor = num[c]
print(f'\nO maior número foi {maior} e o menor foi o {menor}')



