s = c = 0
while True:
  n = int(input('Digite um número inteiro [999 para parar]: '))
  if n == 999:
    break
  s += n 
  c += 1
print(f'Você digitou {c} números e a soma entre eles foi {s}')
