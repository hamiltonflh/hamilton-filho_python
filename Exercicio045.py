import random
from time import sleep
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Faça sua jogada: '))
comp = random.randint(0, 2)
print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PO!!!')
print('-='* 30)
if jogador == 0 and comp == 1:
  print('Jogador jogou PEDRA e o computador jogou PAPEL')
  print('COMPUTADOR GANHOU!')
elif jogador == 1 and comp == 2:
  print('Jogador jogou PAPEL e o computador jogou TESOURA')
  print('COMPUTADOR GANHOU!')
elif jogador == 2 and comp == 0:
  print('Jogador jogou TESOURA e o comoutador jogou PEDRA')
  print('COMPUTADOR GANHOU!')
elif jogador == 2 and comp == 1:
  print('Jogador jogou TESOURA e o computador jogou PAPEL')
  print('JOGADOR GANHOU!')
elif jogador == 1 and comp == 0:
  print('Jogador jogou PAPEL e o computador jogou PEDRA')
  print('JOGADOR GANHOU')
elif jogador == 0 and comp == 2:
  print('Jogador jogou PEDRA e o computador jogou TESOURA')
  print('JOGADOR GANHOU')
elif jogador == comp:
  if jogador == 0:
    print('Você jogou PEDRA e o Computador também, joguem novamente')
  elif jogador == 1:
    print('Você jogou PAPEL e o Computador também, joguem novamente')
  elif jogador == 2:
    print('Você jogou TESOURA e o Computador também, joguem novamente')
else:
  print('Opção inválida, digite um número entre 0 e 2')
print('-='*30)