n = int(input('''Digite um número para
eu calcular o seu fatorial: '''))
c = n
fat = 1
print('{}! = '.format(n), end = ' ')
while c > 0:
  print ('{}'.format(c), end = ' ')
  print(' x ' if c > 1 else ' = ', end = ' ')
  fat *= c
  c-= 1
print('{}'.format(fat))
  
  