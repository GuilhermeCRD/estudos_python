print('\033[4;35;47mHello word!!\033[m')
a = 3
b = 4
print('Os valores são \033[32m{}\033[m e \033[34m{}\033[m!!!'.format(a, b))
nome = 'Guilherme'
cores = {
    'limpa' : '\033[m',
    'azul' : '\033[34m',
    'roxo:' : '\033[35m',
    'pretoebranco' : '\033[7; 30m'
}
print('Muito prazer em te conhecer {}{}{} '.format('\033[4;31m', nome, '\033[m'))
print('Muito prazer em te conhecer {}{}{} '.format(cores['roxo:'], nome, cores['limpa']))