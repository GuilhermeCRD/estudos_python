from random import randint
from time import sleep
print('-=-' * 20)
print('Descubra o numero entre 0 e 5. Que eu estou pensando') 
print('-=-' * 20)
num = int(randint(0, 5))
usuario = int(input('Digite o numero: '))
print('PROCESSANDO...')
sleep(1.5)
if usuario == num:
    print('Voce e quase um mago em, o numero esta correto')
else:
    print('Vixiiii, eu pensei no {} não no {}, mas continue tentando amigão'.format(num, usuario))
print('-->fim de game<--')        