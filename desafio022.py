nome = input('Digite seu nome completo: ').strip()
print('\nAnalisando nome.....\n')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.\n'.format(nome.lower()))

separado = nome.split()

print('As partes que fazem seu nome são {}\n'.format(separado))

print('Seu nome completo tem {} palavras.\n'.format(len(separado[0:])))

print('Seu primeiro nome é {} e tem {} letras.\n'.format(separado[0].capitalize(), len(separado[0])))

print('Seu nome completo tem {} letras.\n'.format(len(nome)-nome.count(' ')))
