velocidade = int(input('Insira a velocidade do veículo em Km/h: '))
if velocidade > 80:
    print('Você está acima do limite e foi multado.')
    multa = (velocidade - 80) * 7
    print('Valor a pagar: R${:.2f}.'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')
    