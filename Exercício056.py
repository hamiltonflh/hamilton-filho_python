soma = 0
somaf = 0
velho = 0
for usuario in range(1, 5):
  print('-=-=-=-= {}° PESSOA -=-=-=-='.format(usuario))
  nome = str(input('NOME: ')).title()
  idade = int(input('IDADE: '))
  sexo = str(input('Sexo [M]/[F]: ')).upper()
  soma += idade
  if sexo == 'F' and idade < 20:
    somaf += 1
  if sexo == 'M' and usuario == 1:
    velho = idade
    nomev = nome
  else:
    if sexo == 'M' and idade > velho:
      velho = idade
      nomev = nome
midade = soma / 4
print('A média de idade dos usuários é de {}'.format(midade))
print('O homem mais velho tem {} e se chama {}'.format(velho, nomev))
if somaf > 0:
  print('Ao todo são {} mulher(s) com menos de 20 anos.'.format(somaf))
else:
  print('Não existe mulher com menos de 20 anos.')


  

  
  


  
