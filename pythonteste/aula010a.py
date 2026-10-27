'''nome = str(input('Qual e seu nome? '))
if nome == 'Guilherme':
    print('Que nome lindo e o seu')
else:
    print('Teu nome e mou marola')
print('Bom dia {}'.format(nome))  '''

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))
if m >= 6:
    print('Parabens voce passou de ano!!')
else:
    print('Que pena voce esta de recuperação')
print('Boas ferias !!')