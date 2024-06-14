from random import randint
comp = randint(0, 10)
print('''Sou seu computador e acabei de pensar em um número 
entre 0 e 10, tente adivinhá-lo''')
jog = int(input("Qual o seu palpite? "))
tentativas = 1
while jog != comp:
  if jog > comp:
    print('Menos... tente novamente')
  elif jog < comp:
    print('Mais... tente novamente')
  jog = int(input('Me dê outro palpite: '))
  tentativas += 1 

print('Você acertou depois {} tentativa(s), parabéns!!!'.format(tentativas))

  