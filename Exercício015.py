dias=int(input('Quantos dias alugado? '))
km=float(input('Quantos Km rodados? '))
aluguel= 60*dias + 0.15*km
print('O aluguei a pagar é de R${:.2f}'.format(aluguel))