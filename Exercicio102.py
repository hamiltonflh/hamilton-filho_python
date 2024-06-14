def fatorial(num, show=False):
  """  ->Faz o calculo do fatorial de um número:
  :param. num: Recebe o número que vai ser feito o fatorial
  :param show=False: Opção que não mostra o processo para chegar no fatorial
  :param show=True: Opção que mostra o processo para chegar no fatorial do número
  :return: A função retorna o valor do fatorial do número
  """
  cont = num
  fat = 1
  if show==False:
    while cont >= 1:
      fat *= cont
      cont -= 1
    return fat
  if show==True:
    cont = num
    fat = 1
    while cont >= 1:
      print(f'{cont} ', end = '')
      print('x ' if cont > 1 else '= ', end = '')
      fat *= cont
      cont -= 1
    return fat


#Programa Principal   
n = int(input('Qual número você quer ver o fatorial? '))
resp = str(input('Quer ver o Processo de multiplicação? [S/N]:')).upper().strip()[0]
while resp not in 'SN':
  resp = str(input('Resposta inválida: ')).upper().strip()[0]
fat = fatorial(n)
print('-='*30)
if resp in 'Nn':
  print(fat)
if resp in 'Ss':
  fat = fatorial(n, show=True)
  print(fat)