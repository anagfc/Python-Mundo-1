frase = input('Digite uma frase: ').strip()
frasemin = frase.lower()
print(frasemin)
print('\nNa sua frase existem {} letras "a".'.format(frasemin.count('a') + frasemin.count('á') + frasemin.count('ã') + frasemin.count('à')))
print('A primeira letra "a" aparece na posição {}.'.format(1 + frasemin.find('a')))
print('A última letra "a" aparece na posição {}.'.format(frasemin.rfind('a') + 1))