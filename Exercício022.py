nome=str(input('Qual seu nome completo? ')).strip()
dividido = nome.split()
print('Nome com letras maiusculas: ')
print(nome.upper())
print('')
print('Nome com letras minusculas: ')
print(nome.lower())
print('')
print('Quantidade de letras sem considerar espacos: ')
print(len(nome) - nome.count(' '))
print('')
print('Quantas letras tem o primeiro nome: ')
print(len(dividido[0]))
