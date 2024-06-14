from datetime import date
anoat = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
  nasc = int(input('Ano de nascimento {}° da pessoa: '.format(c)))
  idade = anoat - nasc
  if idade <= 21:
    menor += 1 
  else:
    maior += 1 
print('{} pessoas são de maioridade e {} são de menoridade'.format(maior, menor))

  
