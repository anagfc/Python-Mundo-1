n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1+n2)/2
print('Sua média é {:.1f}.'.format(m))
if m < 6:
    print('Situação: REPROVADO')
else:
    print('Situação: APROVADO')
