l = float(input("Qual a largura da parde?"))
h = float(input("Qual a altura da parede?"))
a = h * l 
t = a / 2
print("Sua parede tem {:.2f}m² e voce vai precisar comprar {:.1f}L de tinta".format(a, t))