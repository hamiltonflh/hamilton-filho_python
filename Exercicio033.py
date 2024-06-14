n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
n3=int(input('Terceiro número: '))

#Verificação do menor valor
if n1<n2 and n1<n3:
  menor=n1
if n2<n1 and n2<n3:
  menor=n2
if n3<n1 and n3<n2:
  menor=n3

#Verificação do maior valor
if n1>n2 and n1>n3:
  maior=n1
if n2>n1 and n2>n3:
  maior=n2
if n3>n2 and n3 >n1:
  maior=n3
  
print('{} é o maior número e o {} é o menor número'.format(maior, menor))