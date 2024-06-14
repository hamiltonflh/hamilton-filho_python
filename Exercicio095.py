from time import sleep

def titulo(msg):
  print('-'*50)
  print(msg)
  print('-'*50)
  

jogador = dict()
dados = list()
golspartida = list()
gols = dict()
while True:
  jogador['Nome'] = str(input('Nome do Jogador: '))
  partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
  tot = 0
  for c in range(0,partidas):
    golspartida.append(int(input(f'   Gols na {c+1}° partida: ')))
    tot += golspartida[c]
  gols[jogador["Nome"]] = golspartida[:]
  jogador['Gols'] = tot
  dados.append(jogador.copy())
  jogador.clear()
  golspartida.clear()
  r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  while r not in 'SN':
    r = str(input('Resposta inválida: [S/N]: ')).upper().strip()[0]
  if r in 'N':
    break


titulo('JOGADOR           GOLS')
for j in range(0,len(dados)):
  print(f'{dados[j]["Nome"]:<15}        {dados[j]["Gols"]:>15}')


while True:
  resp = str(input('De qual jogador você quer ver os gols? (999 para parar): ')).title().strip()
  for k, g in gols.items():
    if k in resp:
      titulo(f'Gols por partido do {k}') 
      for c in range(0, len(g)):
        print(f'   Na {c+1}° partida marcou {g[c]} gols')
        sleep(1)
      break
  if resp == 999:
    break
  
  
  


  
  
    
  