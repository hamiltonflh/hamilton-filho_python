from time import sleep
print('-='*40)
n = int(input('Digite um número inteiro e eu mostrarei sua tabuada: '))
print('-='*40)
for c in range(0, 11):
  produto = n * c
  print('{} x {} = {}'.format(n, c, produto))
  sleep(1)
print('-='*40)