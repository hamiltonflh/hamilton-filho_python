valores = []
opcao = ''
while True:
  valor = int(input('Digite um valor: '))
  while valor in valores:
    valor = int(input('Você já digitou esse valor. Tente outro: '))
  valores.append(valor)
  opcao = str(input('Quer continuar? [S/N]: '))
  if opcao in 'Nn':
    break

print(f'Você digitou {sorted(valores)}')