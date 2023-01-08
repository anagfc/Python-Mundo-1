salario = float(input('Insira o salário do funcionário: R$'))
aumento = int(input('Insira a porcentagem de aumento: '))
print('O novo salário, com aumento de {}%'.format(aumento), end=' ')
print('é de R${:.2f}.'.format(salario+salario*(aumento/100)))
