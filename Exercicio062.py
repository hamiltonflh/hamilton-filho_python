from time import sleep
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
tamais = 1
soma = 0
for c in range(1, 11):
  print(pt)
  pt += r
  soma += 1
print('PAUSA')
while tamais != 0:
  tamais = int(input('Quantos termos a mais você quer mostrar? '))
  for c in range(1, tamais+1):
    print(pt)
    pt+=r 
    soma+=1
print('Calculando...')
sleep(1)
print('Programa finalizado. \n Você mostrou {} termos da PA'.format(soma))
  
