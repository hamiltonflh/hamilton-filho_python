matriz = [[0,0,0],[0,0,0],[0,0,0]]
sp = 0
scol3 = 0
maior2 = 0
for linha in range(0,3):
  for coluna in range(0,3):
    matriz[linha][coluna] = int(input(f'Valor da posição [{linha}, {coluna}]'))

for linha in range(0,3):
  for coluna in range(0,3):
    print(f'[{matriz[linha][coluna]:^ 5}]', end = ' ')
  print()

print('-='* 30)
for l in range(0,3):
  for c in range(0,3):
    if matriz[l][c] % 2 == 0:
      sp += matriz[l][c]
    if c == 2:
      scol3 += matriz[l][c]
    if l == 1:
      if c == 0:
        maior = matriz[l][c]
      else:
        if matriz[l][c] > maior:
          maior = matriz[l][c]
print(f'A soma dos valores pares da matriz é igual a {sp}')
print(f'A soma dos valores da Terceira coluna é igual a {scol3}')
print(f'O maior valor da segunda linha é o número {maior}')

