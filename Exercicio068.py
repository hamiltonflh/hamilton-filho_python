import random
venc = 0
while True:
  esc = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
  while esc not in 'PI':
      print('Digite somente par ou impar.')
      esc = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
  jog = int(input('Qual número você quer jogar? '))
  comp = random.randint(0, 10)
  soma = jog + comp
  if esc in 'P':
    if soma % 2 == 0:
       print(f'Você jogou {jog} e o computador {comp} e deu PAR.Você GANHOU')
    elif soma % 2 != 0:
       print(f'Você jogou {jog} e o computador {comp} e deu IMPAR. Você PERDEU.')
       break
  if esc in 'I':
    if soma % 2 == 0:
      print(f'Você jogou {jog} e o computador {comp} e deu PAR. você PERDEU')
      break
    elif soma % 2 != 0:
      print(f'Você jogou {jog} e o computador {comp} e deu IMPAR. Você GANHOU.')
  venc += 1 
  print('Vamos jogar novamente...')
if venc == 1:
  print(f'GAME OVER. VOCÊ GANHOU {venc} VEZ.')
else:
  print(f'GAME OVER. VOCÊ GANHOU {venc} VEZES.')


    