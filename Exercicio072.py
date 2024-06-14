numext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Dose', 'Treze', 'Quartorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numint = int(input('Digite um valor de 0 a 20: '))
while numint > 20:
  numint = int(input('Tente novamente.\nDigite um número entre 0 e 20: '))

print(f'O número {numint} escrito por extenso é "{numext[numint]}"')