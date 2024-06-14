n = 0
s = 0
s1 = 0
while n != 999:
  n = int(input('Digite um número [999 para PARAR]: '))
  if n != 999:
    s+=n
    s1 += 1
print(f'Você digitou {s} números \ne a soma entre eles foi {s1}')
