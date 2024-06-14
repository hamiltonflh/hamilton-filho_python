frase=str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
t = len(junto)
i = ''
for c in range(t-1, -1, -1):
  i += junto[c]
print('A frase {} escrita de trás para frente fica {}'.format(junto, i))
if junto == i:
  print('A frase é um palíndromo')
else:
  print('A frase não é um palíndromo')






