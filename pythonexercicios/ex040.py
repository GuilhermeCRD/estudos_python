n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digie sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 7.0 :
    print('Parabens aluno, sua nota foi {:.1f} que e maior que a media  (7.0), VOCE PASSOU DE ANO!!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Voce tirou {:.1f} e não alcançou a media, mas ainda pode fazer a recuperação.'.format(media))
else:
    print('Voce tirou {:.1f} não alcançou a media, esta REPROVADO!!'.format(media))