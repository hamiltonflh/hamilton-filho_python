from datetime import date 
hoje=date.today().year 
nasc= int(input('Qual o ano de nascimento: '))
idade = hoje - nasc 
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
  print('O atleta é da categoria MIRIM')
elif idade <= 14:
  print('O atleta é da categoria INFANTIL')
elif idade <= 19:
  print('O atleta é da categoria JÚNIOR')
elif idade <= 25:
  print('O atleta é da categoria SÊNIOR')
elif idade > 25:
  print('O atleta é da categoria MASTER')
  