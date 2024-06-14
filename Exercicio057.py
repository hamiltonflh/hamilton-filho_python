sexo= str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
  print('Opção inválida')
  sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
if sexo in 'M':
  print('Você é um homem')
elif sexo in 'F':
  print('Você é uma mulher')
