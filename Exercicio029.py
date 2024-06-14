#RADAR ELETRONICO
vel= float(input('Velocidade do veiculo(km/h): '))

if vel > 80:
  print('Você foi multado(a)')
  multa = 7*(vel-80)
  print('Sua multa foi de R${:.2f}'.format(multa))
else:
  print('Você está dentro da velocidade permitida :)')