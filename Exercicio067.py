while True:
  print('-'*60)
  v = int(input('Qual valor você quer ver a tabuada? '))
  print('-'*60)
  if v < 0:
    break
  c = 0
  while c < 11:
    print(f'{v} x {c} = {v*c}')
    c += 1
print('PROGRAMA ENCERRADO. VOLTE SEMPRE!!!')