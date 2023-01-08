from math import trunc
num = float(input('Insira um número real: '))
print('\nAnalisando o número inserido...\nA parte inteira do número {} é {}.'.format(num, trunc(num)))

''' Também é possível usar int(num) ao invés de precisar importar'''