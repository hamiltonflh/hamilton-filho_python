def maior(num=0):
  maior = 0
  for c in range(0, len(num)):
    if c == 0:
      maior = num[c]
    else:
      if num[c] > maior:
        maior = num[c]
  return maior


lst = []
while True:
  lst.append(int(input('Digite um valor: ')))
  r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  if r in 'N':
    break

m = maior(lst)

print(f'O maior valor digitado foi {m}')
  

        
