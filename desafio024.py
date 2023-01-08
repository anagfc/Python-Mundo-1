cidade = input('Digite o nome de uma cidade: ').strip()
nome = cidade.title()
partes = nome.split()
print('Essa cidade começa com "Santo"? {}.'.format(partes[0] == 'Santo'))