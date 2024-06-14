import random
print('====== CHAVES E CONFRONTOS DA COPA DO BRASIL =========')

time1= str(input('Primeiro time: '))
time2= str(input('Segundo time: '))
time3= str(input('Terceiro time: '))
time4= str(input('Quarto time: '))
time5= str(input('Quinto time: '))
time6=str(input('Sexto time: '))
time7= str(input('Sétimo time: '))
time8= str(input('Oitavo time: '))
lista=[time1, time2, time3, time4, time5, time6, time7, time8]
random.shuffle(lista)
gpa=[lista[0], lista[1], lista[2], lista[3]]
gpb=[lista[4], lista[5], lista[6], lista[7]]

print('='*60)
print('''GRUPO A:
1. {}
2. {}
3. {}
4. {} '''.format(gpa[0], gpa[1], gpa[2], gpa[3]))

print('='*60)
print('''GRUPO B:
1. {}
2. {}
3. {}
4. {}'''.format(gpb[0], gpb[1], gpb[2], gpb[3]))

random.shuffle(gpa)
random.shuffle(gpb)

print('='*60)
print('CONFRONTOS')
print('''========= JOGO 1 =========
{} x {}'''.format(gpa[0], gpa[1]))
print('')
print('''========== JOGO 2 ==========
{} x {}'''.format(gpb[0], gpb[1]))
print('')
print('''========== JOGO 3 ==========
{} x {}'''.format(gpa[2], gpa[3]))
print('')
print('''========== JOGO 4 ==========
{} x {}'''.format(gpb[2], gpb[3]))
