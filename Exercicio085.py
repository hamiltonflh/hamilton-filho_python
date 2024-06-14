princ = [[], []]
for c in range (0, 7):
  num = int(input(f'Digite o {c+1}° valor: '))
  if num % 2 == 0:
    princ[0].append(num)
  else:
    princ[1].append(num)

print(f'Lista dos números pares: {sorted(princ[0])}')
print(f'Lista dos números impares: {sorted(princ[1])}')




  