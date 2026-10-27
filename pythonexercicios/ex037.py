num = int(input('Digite um número qualque: '))
print('Escolha uma das bases para converção ' \
'\n[ 1 ] Converter para BÍNARIO ' \
'\n[ 2 ] Converter para OCTAL' \
'\n[ 3 ] Converter para HEXADECIMAL')
opc = int(input('Sua opção: '))
if opc == 1:
    print('O seu numero {} foi convertido para {} em bínario'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O seu numero {} foi convertido para {} em Octal'.format(num , oct(num)[2:]))
elif opc == 3:
    print('O seu numero {} foi convertido para {} em Hexadecimal'.format(num, hex(num)[2:]))
else:
    print('\033[31mSua opção esta incorreta')
