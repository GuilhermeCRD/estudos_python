s = float(input('Qual o valor do seu salario atual: R$'))
if s >= 1250:
    novo =  s + ( s * 10 ) / 100 
else:
    novo = s + ( s * 15 ) / 100 
print('Quem ganhava {:.2F}, passou a ganhar R${:.2F} apos o aumento'.format(s, novo))