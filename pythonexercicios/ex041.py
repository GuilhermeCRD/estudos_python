from datetime import date
nasc = int(input('Digie seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc 
if idade <= 9:
    print('Voce tem {} anos e esta na categoria MIRIM!!'.format(idade))
elif idade <= 14:
    print('Voce tem {} anos e esta na categoria INFANTIL!!'.format(idade))
elif idade <= 19:
    print('Voce tem {} anos e esta ma categoria JUNIOR!!'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos e esta na categoria SÊNIOR!!'.format(idade))
else:
    print('Voce tem {} anos e esta na categoria MASTER!!'.format(idade))