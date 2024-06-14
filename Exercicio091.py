from random import randint
from time import sleep
from operator import itemgetter
print('-='*30)
print('JOGO DE DADOS COM 4 JOGADORES')
print('-='*30)
comeco = str(input('ClIQUE EM QUALQUER TECLA PARA COMEÇAR'))
jogo = { "jogador1": randint(1,6),
         "jogador2": randint(1,6),
         "jogador3": randint(1,6),
         "jogador4": randint(1,6)}
ranking = list()
for k, v in jogo.items():
  print(f'{k} jogou o {v}')
  sleep(1)
cont = 1
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
r = "RANKING DOS JOGADORES"
print('-='*30)
print(f'{r: ^30}')
print('-='*30)
for pos, c in enumerate(ranking):
  print(f'{cont}° --> {c[0]} jogou {c[1]}')
  cont += 1
  sleep(1)