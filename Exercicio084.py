dados = []
pessoas = list()
r = ''
while True:
  dados.append(str(input('Nome: ')))
  dados.append(float(input('Peso: ')))
  pessoas.append(dados[:])
  dados.clear()
  r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
  while r not in 'SsNn':
    r = str(input('Opção inválida. Digite Sim ou Não: ')).upper().strip()[0]
  if r in 'Nn':
    break

maior = 0
menor = 0
nomemaior = []
nomemenor = []


for c in range(0, len(pessoas)):
  if c == 0:
    maior = pessoas[c][1]
    menor = pessoas[c][1]
  else:
    if pessoas[c][1] > maior:
      maior = pessoas[c][1]
    if pessoas[c][1] < menor:
      menor = pessoas[c][1]
  
for c in pessoas:
  if c[1] >= maior:
    nomemaior.append(c[0])
  if c[1] <= menor:
    nomemenor.append(c[0])
    
print(f''' Você registrou {len(pessoas)} pessoas.
O maior peso registrado foi {maior}kg da(s) pessoa(s): {nomemaior}.
O menor peso registrado foi {menor}kg da(s) pessoa(s): {nomemenor}.''')
    




    
