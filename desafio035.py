r1 = float(input('Insira o comprimento da 1ª reta: '))
r2 = float(input('Insira o comprimento da 2ª reta: '))
r3 = float(input('Insira o comprimento da 3ª reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Suas medidas formam um triângulo.')
else:
    print('Suas medidas NÃO formam um triângulo.')
    