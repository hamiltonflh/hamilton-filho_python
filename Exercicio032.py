from datetime import date
ano= int(input('Digite um ano e eu falarei se ele é bissexto ou não. Se quiser o ano atual digite 0'))
if ano == 0
  ano = date.today().year()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('{} é um ano bissexto'.format(ano))
else:
  print('{} não é um ano bissexto'.format(ano))
  