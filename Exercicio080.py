#numeros = list()
#maior = 0
#menor = 0
#for c in range(0,5):
  #num = int(input('Digite um valor: '))
  #while num in numeros:
    #num = int(input('Número já digitado. Tente um diferente: '))
  #if c == 0:
    #numeros.append(num)
    #print('Número adicionado à posição 0...')
    #maior = num
    #menor = num
 #else:
    #if num > maior:
      #numeros.append(num)
      #print(f'Número adicionado ao final da lista...')
      #maior = num
    #elif num < menor:
      #numeros.insert(0, num)
      #print(f'Número adicionado à posição 0...')
      #menor = num
    #elif num < maior > menor:
      #if c == 2:
        #numeros.insert(1, num)
      #if c == 3:
        #if num < numeros[1]:
          #numeros.insert(1, num)
          #print('O número foi adicionado à posição 1...')
        #if num > numeros[1]:
          #numeros.insert(2, num)
          #print('O número foi adicionado à posição 2')
      #if c == 4:
        #if num < numeros[1]:
          #numeros.insert(1, num)
          #print('O número foi adicionado à posição 1...')
        #if num < numeros[2] < numeros[3]:
          #numeros.insert(2, num)
          #print('O número foi adicionado à posição 2...')
        #if nim < numeros[3]:
          #numeros.insert(3, num)
          #print('O número foi adicionado à posição 3...')
#print(f'números digitados: {numeros}')

#Lógica usada pelo guanabara no curso:

numeros = list()

for c in range(0,5):
  num = int(input('Digite um número: '))
  if c == 0 or num >= numeros[len(numeros)]:
    numeros.append(num)
    print('O número foi adicionado ao final da lista...')
  else:
    pos = 0
    while pos < len(numeros):
      if num <= numeros[pos]:
        numeros.insert(pos, num)
        print(f'O número foi adicionado à posição {pos}...')
        break
      pos += 1
print(f'Os números digitados foram {numeros}')



    