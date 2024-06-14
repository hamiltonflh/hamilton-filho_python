num=(int(input('Número a ser convertido: ')))

print('''[1] Numero Binário
[2] Número Octal
[3] Número Hexadecimal''')

esc=int(input('Escolha uma opcão entre as 3: '))

if esc == 1:
  print('O número {} convertido em binário é {}'.format(num, bin(num)))
elif esc == 2:
  print('O número {} convertido em Octal é {}'.format(num, oct(num)))
elif esc == 3:
  print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)))
else:
  print('Opção inválida')
  