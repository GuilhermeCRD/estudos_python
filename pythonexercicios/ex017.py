from math import hypot
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa do triangulo retangulo e: {:.2f}'.format(hypot(co, ca)))