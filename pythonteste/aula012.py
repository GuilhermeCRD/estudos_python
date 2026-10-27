nome = str(input('Qual o seu nome: '))
if nome == 'Guilherme':
    print('Que nome bonito!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'paulo':
    print('Todo mundo tem esse nome ')
elif nome in 'Guilherme Isabella Feyman Rina':
    print('Voce faz parte da nossa familia')
else:
    print('Seu nome e feioso mane!!')
print('Bom dia {}'.format(nome))