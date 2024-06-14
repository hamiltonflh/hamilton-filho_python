def leiaint(msg):
    print(msg)
    valor = str(input())
    while valor.isalpha():
      print('ERRO. Digite um número válido')
      print(msg)
      valor = str(input())
    return int(valor)
      


#Programa principal
v = leiaint('Digite um número: ')
print(f'Você digitou o número {v}')
