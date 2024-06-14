casa=float(input('Valor da casa:'))
sal=float(input('Sua renda mensal: '))
tempo=int(input('Em quantos anos você pretende pagar?'))
mes=tempo*12
prest=casa/mes

if prest > sal*30/100:
   print('''Seu empréstimo foi negado
   O valor da prestação excede 30% do seu salário''')
elif prest < sal*30/100:
  print('''PROPOSTA DE FINANCIAMENTO:
  VALOR DO BEM: R${:.2f}
  PRESTAÇÕES: {} MESES
  VALOR DA PARCELA: R${:.2f}'''.format(casa, mes, prest))

  

