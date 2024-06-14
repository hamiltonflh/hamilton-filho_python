h=float(input('Altura da parede(m): '))
b=float(input('Comprimento da parede(m): '))
a=b*h
x=a/2
print('Sua parede é de {}x{} com uma área de {:.2f} metros quadrados'.format(b,h,a))
print('Você usará {:.2f}l de tinta para pintar essa parede'.format(x))
