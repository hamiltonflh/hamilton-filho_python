#Meu raciocínio
expressão = str(input('Digite a sua expressão: '))
abre = expressão.count('(')
fecha = expressão.count(')')
if abre == fecha:
  print('Sua expressão é válida!!')
else:
  print('Sua expressão é inválida!!')
  
#Raciocinio com listas. Essa solução foi apresentada no curso
expr = str(input('Digite a expressão'))
pilha = []
for c in expr:
  if c == '(':
    pilha.append('(')
  elif c == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) > 0:
  print('A expressão é inválida!')
else:
  print('A expressão é válida')
