s = 0
c = 0
opcao = ''
maior = 0
menor = 0

while opcao in 'S':
  n = int(input('Digite um valor: '))
  s += n
  if c == 1:
    maior = n
    menor = n
  else:
    if n > maior:
      maior = n 
    elif n < menor:
       menor = n 
  c += 1
  opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  if opcao not in 'SN':
    while opcao not in 'SN':
       print('Opção inválida, dicgite apenas "S" ou "N"')
       opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()
media = s/c
print(f'Foram digitados {c} números')
print(f'O maior número digitado foi {maior} \nO menor foi {menor}')
print(f'A média entre os números foi {media}')

