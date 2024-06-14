import math
an= float(input('Digite um ângulo: '))
seno=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))

print('O SENO de {}° é igual a {:.2f}'.format(an, seno))
print('O COSSENO de {}° é igual a {:.2f}'.format(an, cos))
print('A TANGENTE de {}° é igual a {:.2f}'.format(an, tan))