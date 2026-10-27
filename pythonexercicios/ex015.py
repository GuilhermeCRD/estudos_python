dia = int(input("Quantos dias de alugado? " ))
km = int(input("Quantos km rodados? "))
pago = (dia * 60) + (km * 0.15) 
print("O aluguel total ficou no valor de R${}".format((pago)))