velo = int(input('A que velocidade o carro passou no radar? '))
multa = (velo - 80) * 7
if velo >= 81:
    print('Voce passou acima do limite da via e deve pagar R${:,.2F} de multa'.format(multa))
else:
    print('Voce e muito responsavel, continue assim.')