sal=float(input('Salário do funcionário: R$'))
if sal <= 1250.00:
  aumento= (sal * 15/100) + sal
  print('Você recebeu um aumento de 15% e seu salário ficou R${:.2f}'.format(aumento))
else:
  aumento = (sal * 10/100) + sal
  print('Você recebeu um aumento de 10% e seu salário ficou R${:.2f}'.format(aumento))
  