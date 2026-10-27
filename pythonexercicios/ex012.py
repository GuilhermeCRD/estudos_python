p = float(input("Qual o preço do produto? R$"))
novo = p - (p * 5 / 100)
print("O preço total do seu produto ficou R${:.2f}, apos o desconto de 5%".format(novo)) 