from datetime import date
ano= int(input('Digite o ano do seu nascimento: '))
anoat = date.today().year
idade = anoat-ano

if idade == 18:
  print('Você tem 18 anos e está apto a se alistar')
elif idade > 18:
  sobra = idade - 18
  print('Você tem {} anos e já passou {} anos da hora de se alistar'.format(idade, sobra))
  print('Você deveria ter se alistado em {}'.format(anoat - sobra))
elif idade < 18 and idade < 16:
  falta = 18 - idade
  print('Você tem apenas {} anos e faltam {} anos para você se alistar'.format(idade, falta))
  print('O seu ano de alistamento vai ser em {}'.format(anoat + falta))
  elif idade == 17:
    print('Resta 1 ano para você se alistar. Fique atento ao período de alistamento.')
