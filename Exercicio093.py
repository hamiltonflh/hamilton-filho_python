estatisticas = dict()
partidas = list()
somagols = 0
estatisticas["Nome"] = str(input('Nome do Jogador: '))
totpar = int(input(f'Quantas partidas {estatisticas["Nome"]} jogou? '))

for c in range(0, totpar):
  partidas.append(int(input(f'Quantos gols {estatisticas["Nome"]} marcou na partida {c+1}?')))
  somagols += partidas[c]

estatisticas["Gols"] = somagols
estatisticas["Gols/Partida"] = somagols/totpar

print('-='*60)
print(f'APROVEITAMENTO DO JOGADOR {estatisticas["Nome"].upper()}')
print('-='*60)
for k, v in estatisticas.items():
  print(f"{k}: {v}")

