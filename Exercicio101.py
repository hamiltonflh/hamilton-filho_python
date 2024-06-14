from datetime import datetime
def voto(n):
  at = datetime.now().year 
  idade = at - n
  print(f'Com {idade} anos: ', end = '')
  if idade >= 16 and idade < 18 or idade >= 70:
    return 'O VOTO É OPCIONAL'
  elif idade >= 18 < 70:
    return 'O VOTO É OBRIGATÓRIO'
  else:
    return 'NÃO VOTA'


#Programa principal:
nasc = int(input('Data de Nascimento: '))
sit = voto(nasc)
print(sit)
    
  
  