from time import sleep

def contador(ini, fim, pas):
  if pas < 0:
    pas *= -1
  if pas == 0:
    pas = 1
  if ini < fim:
    for c in range(ini, fim+1, pas):
      print(f"{c} ")
      sleep(0.5)
  if ini > fim :
    for c in range(ini, fim-1, -pas):
      print(f'{c} ')
      sleep(0.5)
  

print('Contagem de 1 até 10...')
print('='* 50)
contador(1, 10, 1)

print('Contagem regressiva de 10 até 0 de 2 em 2')
print('='*50)
contador(10,0, 2)

print('='*50)
print('Agora é sua vez de personalizar:')
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
if p > 0:
  print(f'Contagem de {i} até {f} de {p} em {p}.')
elif p < 0:
  print(f'Contagem regressiva de {f} até {i} de {p*-1} em {p*-1} ')
print('='*30)
contador(i,f,p)
