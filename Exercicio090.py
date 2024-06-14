dados = {}
while True:
  dados["Aluno"] = str(input('Aluno: '))
  dados["Media"] = float(input('Média: '))
  if dados["Media"] >= 7:
    dados["Situacao"] = "Aprovado"
  elif dados["Media"] >= 4 < 7:
    dados["Situacao"] = "Está de Recuperação"
  else:
    dados["Situacao"] = "Reprovado"
  print('-='*30)
  for k, v in dados.items():
    print(f'{k:<15} = {v:>30}')
  print('-='*30)
  
    
    