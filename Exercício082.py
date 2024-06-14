valores = []
pares = []
impares = list()
while True:
  num = int(input('Digite um valor: '))
  valores.append(num)
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
  r = str(input('Quer continuar? [S/N]: ')).upper()[0]
  while r not in 'SsNn':
    r = str(input('Opção inválida. digite somente Sim ou Não: ')).upper()[0]
  if r in 'Nn':
    break
print(f'Você digitou {len(valores)} números e eles são {sorted(valores)}')
if len(pares) > 0:
   print(f'Os valores pares foram {sorted(pares)}')
if len(impares) > 0:
   print(f'Os valores imapares foram {sorted(impares)}')
    