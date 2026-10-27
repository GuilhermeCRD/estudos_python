r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta:   '))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print (' Voce consegue formar um triangulo', end= ' ')
    if  r1 == r2 == r3:
        print('EQUILÁTICO!!')
    elif  r1 != r2 != r3 != r1:
        print('ESCALENO!!')
    else:
        print('ISÓSCELES!!')
else:
    print('Voce não consegue formar um triangulo com essas retas')