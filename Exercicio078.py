num = list()
c = 1
maior = 0
menor = 0
posmaior = []
posmenor = []
for i in range(0, 5):
 num.append(int(input(f'Digite o {c}° número: ')))
 c += 1
 if i == 0:
  maior = num[i]
  menor = num[i]
 else: 
   if num[i] > maior:
    maior = num[i]
   elif num[i] < menor:
    menor = num[i]

for pos, i in enumerate(num):
  if i == maior:
    posmaior.append(pos)
  if i == menor:
    posmenor.append(pos)
    
print(f'O maior número digitado foi {maior} nas posições...', end = '')
for i in posmaior:
  print(f'{i}...')

print(f'O menor número digitado foi {menor} nas posições...', end = '')
for i in posmenor:
  print(f'{i}...')

    


  
    