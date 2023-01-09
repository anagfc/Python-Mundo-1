salário = float(input('Insira seu salário: R$'))
if salário > 1250:
    novo_salário = salário + (salário * 10) / 100
    print('Você recebeu um aumento de 10%\nSeu novo salário é de R${:.2f}.'.format(novo_salário))
else:
    novo_salário = salário + (salário * 15) / 100
    print('Você recebeu um aumento de 15%\nSeu novo salário é de R${:.2f}.'.format(novo_salário))
    