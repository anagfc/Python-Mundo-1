# Forma clássica, mas não é 100% precisa
# ano = int(input('Insira um ano: '))
# print('O ano {} é bissexto'.format(ano) if ano % 4 == 0 else 'O ano {} não é bissexto.'.format(ano))

# Ano bissexto acontece de 4 em 4 anos, exceto em anos múltiplos de 100 que não são múltiplos de 400

# Para pegar o ano atual da máquina, é necessário importar a função date do módulo datetime
from datetime import date

ano = int(input('Insira um ano. Para analisar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
print('O ano {} é bissexto'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'O ano {} não é bissexto.'.format(ano))

# Para pegar o ano atual da máquina, é necessário importar a função date do módulo datetime