s = float(input("Qual o seu salario atual? R$"))
aumento = s + (s * 15 / 100)
print("O seu salario saiu de R${:,} para R${:,} com um aumento de 15%".format(s, aumento))