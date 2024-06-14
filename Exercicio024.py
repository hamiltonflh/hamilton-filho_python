cidade=str(input('Digite o nome de uma cidade: '))
maiuscula = cidade.upper()
dividido= maiuscula.split()
print('A cidade começa com Santo?')
print('SANTO' in dividido[0])


