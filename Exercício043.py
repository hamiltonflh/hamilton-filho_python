peso = float(input('Peso em (KG): '))
altura = float(input('Altura em metros: '))
imc = peso / (altura**2)
print('Seu IMC é de {:.1f}kg/m2. Você está '.format(imc), end='')

if imc < 18.5:
  print('com BAIXO PESO!')
elif imc > 18.5 < 24.9:
  print('com o PESO ADEQUADO!')
elif imc >= 25.0 < 29.9:
  print('com SOBREPESO!')
elif imc >= 30.0 < 34.9:
  print('com OBESIDADE GRAU 1')
elif imc >= 35.0 < 39.9 
  print('com OBESIDADE GRAU 2')
else:
  print('com OBESIDADE EXTREMA')
