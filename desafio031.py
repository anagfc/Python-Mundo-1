distância = float(input('Insira a distância da viagem em Km: '))
if distância <= 200:
    valor = 0.5 * distância
    print('O valor a ser pago é de R${:.2f}.'.format(valor))
else:
    valor = 0.45 * distância
    print('O valor a ser pago é de R${:.2f}.'.format(valor))
