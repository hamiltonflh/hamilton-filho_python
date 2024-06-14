lista = []
op = ''
cont = 0
while True:
  n = int(input('Digite um valor: '))
  lista.append(n)
  cont += 1
  op = str(input('Quer continuar? [S/N]: '))
  if op in 'Nn':
    break
print(f'Você digitou {cont} números.')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente {lista}')
if 5 in lista:
  print('O número 5 está na lista!')
  