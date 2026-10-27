import math
ang = float(input('Digite um angulo qualquer: '))
rad = math.radians(ang)
print('O angulo e {}, e seu seno mede {:.2f}cm, seu cosseno {:.2f}cm, e sua tangente {:.2f}cm'.format(rad, math.sin(rad), math.cos(rad), math.tan(rad)))