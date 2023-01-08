km = float(input('Insira quantos Km foram percorridos: '))
dias = int(input('Insira quantos dias durou o aluguel: '))
preço = 0.15*km + 60*dias

print('O preço total a ser pago por {} dias de aluguel e {}Km rodados é de R${:.2f}.'.format(dias, km, preço))