print('='*50)
media = 'MEDIA DE NOTAS'
print(f'{media:^50}')
print('='*50)

nome = str(input('Nome do Aluno: '))
matem = float(input('Nota em Matemática: '))
port = float(input('Nota em Português: '))
bio = float(input('Nota em Biologia: '))
notas = ['Matemática', 'Português', 'Biologia']
notas.insert(1, matem)
notas.insert(3, port)
notas.insert(5, bio)
s = 0
i = 0
print('=' * 50)
print(f'Aluno: {nome}')
for c in range(0, len(notas)):
  if c % 2 == 0:
    print(f'{notas[c]:<20}', end = '')
  else: 
    print(f'{notas[c]:.1f}')
    s+= notas[c]
    i += 1
medi = s/i 
print(f'A média do {nome} foi de {medi:.1f} e ele está ', end = '')
if medi >= 5:
  print('APROVADO')
else:
  print('REPROVADO')
  

    