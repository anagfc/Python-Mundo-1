from math import sqrt, pow
c1 = float(input('Insira a medida do 1º cateto: '))
c2 = float(input('Insira a medida do 2º cateto: '))
hipo = sqrt(pow(c1,2)+pow(c2,2))
print('Lado oposto: {}\nLado adjascente: {}\nHipotenusa: {:.2f}'.format(c1, c2, hipo))


'''
O módulo math também tem a função hypot
'''