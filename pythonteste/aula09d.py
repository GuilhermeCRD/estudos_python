#frase = 'curso em video python'
#dividido = frase.split()
#print()

#print('-'.join(dividido))

texto = ('guilherme,155492047070,306753351')
dados = texto.split(',')
print(dados)

tx = ('maçat bananat uvat')
print(tx.split())
print(tx.split('t'))

word = ('terra, areia, ferro, cobalto')
print(word.split(',', 2))
print(word.split(' ', 4))

s = 'acre,rio,belem'
result = s.split(',')
for item in result:
    print(item)