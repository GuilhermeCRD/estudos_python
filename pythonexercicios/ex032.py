from datetime import date
ano = int(input('Digite o ano 0 para o ano atual, ou coloque o ano que voce quiser: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} e um ano BISSEXTO'.format(ano))
else:
    print('O ano {} Não e BISSEXTO'.format(ano))