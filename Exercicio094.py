dados = {} 
pessoas = list()
sidade = 0
mulheres = list()
maismedia = list()

#Parte do programa de entrada de dados
while True:
  dados['nome'] = str(input('Nome: '))
  dados['idade'] = int(input('Idade: '))
  dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
  sidade += dados['idade']
  if dados['sexo'] in 'F':
    mulheres.append(dados.copy())
  pessoas.append(dados.copy())
  dados.clear()
  r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
  while r not in 'SN':
    r = str(input('Resposta inválida. Digite somente "Sim" ou "Não": ')).upper().strip()[0]
  if r in 'N':
   break
 
#Parte da saída de dados
midade = sidade / len(pessoas)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print('-'*100)
print(f'A média de idade dos cadastrados foi de {midade:.1f} anos')
print('-'*100)
print('Lista de pessoas mais velhas que a média de idade:')
for c in range(0, len(pessoas)):
  if pessoas[c]["idade"] > midade:
    print(pessoas[c]["nome"])
print('-'*100)
if len(mulheres) > 0:
  print('Lista de mulheres cadastradas:')
  for c in range(0, len(mulheres)):
     print(f'{mulheres[c]["nome"]}')
