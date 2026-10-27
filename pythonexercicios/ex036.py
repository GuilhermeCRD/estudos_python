casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual seu salário mensal: R$'))
anos = int(input('Em quantos anos pretende pagar: '))
prestmes = casa / (anos * 12)
if  prestmes <= (sal * 30) / 100:
    print('Para pegar uma casa de R${:.2f} em {} anos a prestação sera de {:.2f} por mês \nEmpretimo APROVADO!!'.format(casa, anos,prestmes ))
elif prestmes >= (sal * 30 ) / 100:
    print('Para pegar uma casa de R${:.2f} em {} anos a prestação sera de {:.2f} por mês \nEmpretimo NEGADO!!'.format
    (casa, anos, prestmes))