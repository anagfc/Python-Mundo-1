x = input('Insira algo: ')

primitivo = type(x)
numerico = x.isnumeric()
alfabetico = x.isalpha()
alfanumerico = x.isalnum()
caixaalta = x.isupper()
minusculas = x.islower()

print('')
print('Analisando o input')
print('')
print('O valor digitado foi {} e pertence ao tipo primitivo {}.'.format(x, primitivo))
print('O valor digitado só tem espaços?', x.isspace())
print('O valor digitado é numérico: {}.'.format(numerico))
print('O valor digitado é alfabético: {}.'.format(alfabetico))
print('O valor digitado é alfanumérico: {}.'.format(alfanumerico))
print('O valor digitado está em caixa alta: {}.'.format(caixaalta))
print('O valor digitado está em letras minúsculas: {}.'.format(minusculas))
print('O valor está capitalizado?', x.istitle())