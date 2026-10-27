dist = float(input('Qual a distancia da sua viagem: '))
print('Voce esta prestes a começar uma viagem de {}KM'.format(dist))
if dist <= 200:
    print('Sua viajem ficou no valor total de: R${:,.2F}'.format(dist * 0.50))
else:
    print('Sua viagem ficou no valor total de: R${:,.2f}'.format(dist * 0.45))
print('--> MUITO OBRIGADO POR ESCOLHER A TDH TOUR <--')    
        
