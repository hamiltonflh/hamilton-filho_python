h = 0
m = 0
maiores = 0
while True:
  print('-'*60)
  print('           CADASTRO DE PESSOAS      ')
  print('-'*60)
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
  while sexo not in 'MF':
    print('Sexo inválido. digite somente Masculino, Feminino ou somente as iniciais "M" ou "F"')
    sexo = str(input('Sexo [M/F]: '))
  if sexo in 'M':
    h += 1
  elif sexo in 'F':
    if idade < 20:
      m += 1
  if idade > 18:
    maiores += 1
  opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  while opcao not in 'SN':
    print('Opção inválida. Digite somente Sim, Não ou somente as iniciais "S" ou "N"')
    opcao = str(input('Quer continuar? [S/N]')).upper().strip()[0]
  if opcao in 'N':
    break
print(f'Total de pessoas com mais de 18 anos é {maiores}')
print(f'Você cadastrou {h} homens.')
print(f'Você cadastrou {m} mulheres menores que 20 anos')


  