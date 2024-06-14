dados = []
lista = list()

while True:
  aluno = str(input('Nome: ')).title().strip()
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  dados.append(aluno)
  dados.append(nota1)
  dados.append(nota2)
  dados.append(media)
  lista.append(dados[:])
  dados.clear()
  r = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
  while r not in 'SN':
    r = str('Opção inválida. Digite apenas Sim ou Não: ')
  if r in 'N':
    break
  
print('-='*30)
print(f' ' *10, 'ALUNO', ' '*20, 'MEDIA' )
print('-'*100)
for pos,p in enumerate(lista):
  print(f'{pos+1}', ' '*5, f'{p[0]:<15} {p[3]:>15}')
print('-='*30)

while True:
  flag = str(input('De quem você quer ver as notas? (999, se quiser parar): ')).title().strip()
  for c in range(0, len(lista)):
      if flag in lista[c][0]:
        print(f'As notas do aluno {lista[c][0]} foram {lista[c][1]} e {lista[c][2]}')
        print('-='*30)
        break
  if flag in '999':
    break

   