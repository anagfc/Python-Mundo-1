pp = float(input('Insira o valor do produto: R$'))
desc = int(input('Insira a porcentagem do desconto: '))
print('O valor a ser pago por esse produto, com {}%'.format(desc), end=" ")
print('de desconto, é de R${:.2f}.'.format(pp-pp*(5/100)))
