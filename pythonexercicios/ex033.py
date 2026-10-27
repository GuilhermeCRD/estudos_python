n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
n3 = int(input('Digite o ultimo numero: '))
#print('O maior numero digitado foi {}, e o menor numero digitado foi {}'.format(max(n1, n2, n3), min(n1, n2, n3)))
#Verificando o menor numero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando maior numero
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor foi {} '.format(menor))
print('O maior valor foi {} '.format(maior))
