matriz = []
col1 = []
col2 = []
col3 = []
for c in range(0,3):
  col1.append(int(input(f'Digite o valor da posição [0, {c}]')))
matriz.append(col1)
for c in range(0,3):
  col2.append(int(input(f'Digite o valor da posição [1, {c}]')))
matriz.append(col2)
for c in range(0,3):
  col3.append(int(input(f'Digite o valor da posição [2, {c}]')))
matriz.append(col3)

print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
