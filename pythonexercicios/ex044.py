print ('=' * 20, 'Build tech', '=' * 20)
valor = float(input('Qual o valor do produto? R$ '))
print(
    '=' * 5, 'FORMAS DE PAGAMENTO', '=' * 5,
    '\n[1] A vista com dinheiro ou cheque:'\
    '\n[2] A vista no cartão:'\
    '\n[3] Em até 2x no cartão:'\
    '\n[4] Em até 3x ou mais no cartão:'\
)
pagamento = (int(input('Qual sera a forma de pagamento? ')))
if pagamento == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format( valor, valor - ( valor * 10 ) / 100 ))
elif pagamento == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format( valor, valor - ( valor * 5 ) / 100 ))
elif pagamento == 3:
    print('O valor total de R${:.2f} vai ser paga em 2x de R${:.2f}'.format(valor, valor / 2))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas?'))
    print('O valor total de R${:.2f} sera parcelado em {}x de R${:.2f} COM JUROS'.format(valor, parcela, (valor + (valor * 20 ) / 100 ) / parcela ))
    print(' Sua com compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor + (valor * 20 ) / 100))