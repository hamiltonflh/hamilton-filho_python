from random import randint
def sorte(lst):
  for c in range(0, 5):
    lst.append(randint(0,10))
    
def somapares(pares):
    s = 0
    for c in range(0, len(pares)):
      if pares[c] % 2 == 0:
        s+=pares[c]
    return s
    
      

numeros = []
sorte(numeros)
somp = somapares(numeros)
print(f'A lista foi {numeros}')
print(f'A soma dos números pares é igual a {somp}')


