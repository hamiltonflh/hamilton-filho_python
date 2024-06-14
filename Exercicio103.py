def ficha(nome= '', gols= ''):
   print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')
   
#Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Gols marcados: '))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == '':
  n = " <desconhecido> "
  
ficha(n, g)
