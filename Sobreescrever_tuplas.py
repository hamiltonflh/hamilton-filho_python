#Tupla é imutável, porém podemos sobrescrevê-la para mudá-la:
cardapio = ('Prato feito', 25.00, 'Comida a Quilo', 50.00, 'Self Service', 35.00)
#Mostrará a tupla normal.
for i in range(0, len(cardapio)):
  #Perceba que os indices pares são as comidas e os indices impares são os preços. Por isso ultilizei a condicional.
  if i % 2 == 0:
    print(f'{cardapio[i]:.<40}', end = ' ')
  elif i % 2 != 0:
    print(f'R${cardapio[i]:>.2f}')
print('='*60)
print('Houve uma mudança no preço do quilo da comida para R$48,00')
#Sobreescrever uma variável no meio do programa é permitido, aqui estou sobreescrevendo a tupla cardapio:
cardapio = ('Prato feito', 25.00, 'Comida a Quilo', 48.00, 'Self service', 35.00)

#Esse laço mostrará a tupla modificada
for i in range(0, len(cardapio)):
  if i % 2 == 0:
    print(f'{cardapio[i]:.<40}', end = '')
  elif i % 2 != 0:
    print(f'R${cardapio[i]: > .2f}')


  