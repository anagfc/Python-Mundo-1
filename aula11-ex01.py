print('Olá, Mundo!')
print('\033[31mOlá, Mundo!')
print('\033[31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m') # Deixa o fundo só até o fim do conteúdo
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;37mOlá, Mundo!\033[m')
print('\033[33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

sobrenome = 'Silva'
print('Prazer em te conhecer, senhor {}{}{}.'.format(cores['amarelo'], sobrenome, cores['limpa']))


# Para colorir no Python, também existe o método colorize