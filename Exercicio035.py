print('-='*40)
print('       Analisador de triângulo')
print('-='*40)
l1 = float(input('Lado 1 (cm): '))
l2 = float(input('Lado 2 (cm): '))
l3 = float(input('Lado 3 (cm): '))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
  print('Esses segmentos de reta formam um triângulo')
else:
  print('Esses segmentos de reta não formam um triângulo')