from time import sleep
total = 0
mais1000 = 0
cont = 1
maisbarato = 0
while True:
  prod = str(input('Nome do produto: '))
  preco = float(input('Preço do produto: R$'))
  if preco > 1000:
     mais1000 += 1 
  if cont == 1:
    maisbarato = preco
  else:
    if preco < maisbarato:
      maisbarato = preco
  total += preco
  opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  while opcao not in 'SN':
    print('Opção inválida.')
    sleep(0.75)
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  if opcao in 'N':
     break
print(f'Valor total da compra foi R${total:.2f}')
print(f'{mais1000} produtos custaram mais que R$1000,00')
print(f'O produto mais barato custou R${maisbarato:.2f}')