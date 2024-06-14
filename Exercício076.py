prod = ('Lápis', 1.75, 'Caderno', 15.90, 'Caneta', 2.30, 'Régua', 5.00, 'Compasso', 4.00, 'Estojo', 10.00)
#
for pos in range(0, len(prod)):
  if pos % 2 == 0:
    print(f'{prod[pos]:.<30}')