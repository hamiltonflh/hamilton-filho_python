n=int(input('Digite um número intsiro: '))
s=0
print('-='*40)
print('Divisores do número {}'.format(n))
for c in range(1, 101):
  if n % c  == 0:
    print(c, end = ' ')
    s += 1 
print('\n O número {} foi divisível por {} números.'.format(n,s))
if s == 2:
  print('Então o número é PRIMO.')
else:
  print('Então o número NÃO É PRIMO.')