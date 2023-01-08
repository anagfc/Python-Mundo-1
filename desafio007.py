nome = input('Insira seu nome: ')
n1 = float(input('{}, insira sua primeira nota: '.format(nome)))
n2 = float(input('Insira sua segunda nota: '))

print('\n{}, sua média é {:.1f}.'.format(nome, (n1+n2)/2))
