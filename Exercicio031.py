km = float(input('Quantos quilometros você vai viajar? '))
if km < 200:
  print('A sua viagem custará R${:.2f}'.format(km*0.50))
else:
  print('A sua viagem tem um valor promocional de R${:.2f}'.format(km*0.45))