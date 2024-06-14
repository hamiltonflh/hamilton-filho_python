print('-='* 40)
print('                10 PRIMEIROS TERMOS DA PA')
print('-='*40)
pt = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a Razão da PA: '))

for c in range(0, 11):
  print('{}'.format(pt))
  pt += r
