from time import sleep
tabela = ('Palmeiras', 'Grêmio', 'Atl MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atl PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Curitiba', 'America MG')
col = col5 = 1 
col4 = 17
print('TABELA FINAL BRASILEIRÃO 2023')
for c in range(0, 20):
  print(f'{col}° - {tabela[c]}')
  col += 1
print('='*30)
sleep(1)
print('Tabela dos primeiros 5 colocados do Brasileirão 2023.')
for c in range(0, 5):
  print(f'{col5}° - {tabela[c]}')
  col5 += 1
print('='*30)
sleep(1)
print('Rebaixados:')
for c in range(16, 20):
  print(f'{col4}° - {tabela[c]}')
  col4 += 1 
print('='*30)
sleep(1)
print('Times do Brasileirão em Ordem Alfabética:')
alfa = sorted(tabela)
for c in range(0, len(alfa)):
  print(alfa[c])
print('='*30)
esc = str(input('Qual time você quer ver a posição? ')).strip().title()
while esc not in tabela:
  esc = str(input('Desculpe digite o nome do time corretamente e com acentos devidos: ')).strip().title()
postime = tabela.index(esc)
print(f'O time {esc} está na {postime + 1}° posição do Brasileirão 2023.')



  
  
