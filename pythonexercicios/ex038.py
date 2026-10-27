n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O primeiro valor {} e o maior que o segundo valor {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} e maior que o primeiro valor {}.'.format(n2, n1))
else:
    print('Os valores {} e {} são iguais.'.format(n1, n2))