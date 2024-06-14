from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
fechar = False
while not fechar:
  print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Digitar novos números
[5] Sair do programa''')
  opcao = int(input('Escolha outra opcao '))
  if opcao == 5:
    fechar = True
    print('Finalizando...')
    print('-='*12)
    sleep(2)
  elif opcao == 1:
    soma = v1 + v2
    print('A soma de {} e {} é igual a {}'.format(v1, v2, soma))
  elif opcao == 2:
      mult = v1*v2
      print('O produto dos números {} e {} é igual a {}'.format(v1, v2, mult))
  elif opcao == 3:
    if v1 > v2:
      print('O número maior é o {}'.format(v1))
    else:
      print('O número maior é o {}'.format(v2))
  elif opcao == 4:
    v1 = int(input('Primeiro valor: '))
    v2 = int(input('Segundo valor: '))
  else:
    print('Opção inválida')
  sleep(2)
print('Finalizado. Obrigado por jogar!')
  
  
  
    
    
    
  