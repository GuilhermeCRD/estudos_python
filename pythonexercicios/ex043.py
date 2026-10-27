peso = float(input('Qual e o seu peso atual? (KG) '))
altura = float(input('Qual a sua altura? ' ))
imc = peso / (altura ** 2) 
if imc < 18.5:
    print('O seu IMC esta em {:.1f}, voce esta na classificação ABAIXO DO PESO!!'.format(imc))
elif imc < 25:
    print('O seu IMC esta em {:.1f}, voce esta na classificação PESO IDEAL!!'.format(imc))
elif imc < 30:
    print('O seu IMC esta em {:.1f}, voce esta na classificação SOBRE PESO!!'.format(imc))
elif imc < 40:
    print('O seu IMC esta em {:.1f}, voce esta na classificação OBESIDADE!!'.format(imc))
else:
    print('O seu IMC esta em {:.1f}, voce esta na classificação OBESIDADE MORBIDA!!'.format(imc))
