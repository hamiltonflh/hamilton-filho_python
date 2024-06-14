nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media = (nota1 + nota2)/2 

print('A média do aluno foi de {:.1f} pontos'.format(media))

if media < 5.0:
  print('Aluno REPROVADO!')
elif media >= 5.0 or media < 7.0:
  print('Aluno está de RECUPERAÇÃO!')
elif media >= 7.0:
  print('Aluno APROVADO')