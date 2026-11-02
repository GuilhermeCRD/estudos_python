from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print (
    'Suas opções'
    '\n[0] PEDRA'
    '\n[1] PAPEL'
    '\n[2] TESOURA'
)
jogador = int(input('Qual sua jogada? '))
if jogador not in (0, 1, 2): #Corrigindo o erro de o numero for maior de 2
    print('Jogada inválida! Escolha entre 0, 1 e 2.')
    exit()
print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO!!')
sleep(0.3)
print('-=' * 15) 
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # Computador escolheu pedra 
    if jogador == 0: # Jogador escolhe pedra
        print('AS JOGADAS EMPATARAM') 
    elif jogador == 1: #Jogador escolheu papel
        print('Papel vence pedra, VOCE VENCEU!!')
    elif jogador == 2: #Jogador escolheu tesoura
        print('\033[7;30;41mTesoura vence papel, VOCE PERDEU!!\033[m')
elif computador == 1: # computador jogou papel
    if jogador == 0: #jogador jogou pedra
        print('\033[7;30;41mTesoura vence papel, VOCE PERDEU!!\033[m')
    elif jogador == 1: #jogador jogou papel
        print('AS JOGADAS EMPATARAM')
    elif jogador == 2: #jogador jogou tesoura
        print('Tesoura vence papel, VOCE VENCEU!!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0: #jogador jogou pedra
        print('Pedra vence tesoura, VOCE VENCEU!!')
    elif jogador == 1: #jogador jogou papel
        print('\033[7;30;41mTesoura vence papel, VOCE PERDEU!!\033[m')
    elif jogador == 2: #jogador jogou tesoura
        print('AS JOGADAS EMPATARAM')
