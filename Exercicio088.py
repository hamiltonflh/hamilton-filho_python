#importação de bibliotecas
from random import randint
from time import sleep

#Area de variáveis
jogos = []
qtd = int(input('Quantos jogos você quer fazer?'))
jogo = list()

#laços para criação dos jogos
for j in range(0, qtd):
  for n in range(0,6):
     num = randint(1,60)
     while num in jogo:
       num = randint(1,60)
     jogo.append(num)
  jogo.sort()
  jogos.append(jogo[:])
  jogo.clear()

#Jogos sendo mostrados na tela
print('-='*3, f'SORTEANDO {qtd} JOGOS', '-='*3)
for c in range(0, qtd):
  print(f'Jogo {c+1}:  {jogos[c]}')
  print()
  sleep(1)
  
  