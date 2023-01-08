from math import sin, cos, tan, radians
angulo = float(input('Insira o ângulo desejado: '))
print('Sobre o ângulo de {}º\nSeu seno: {:.2f}\nSeu cosseno: {:.2f}\nSua tangente: {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
