import random
num=random.randint(0,5)
print('='*60)
print('Vou pensar em um número agora, tente adivinhar')
print('='*60)
adv=int(input('Qual número eu pensei? '))
if num == adv:
  print('Parabéns, eu pensei em {}, você tem o dom de adivinhação!'.format(num))
else:
  print('Infelizmente você errou, o número que eu pensei foi o {}, tente novamente ;)'.format(num))
print('='*60)
