from random import shuffle

t1 = input('Insira o líder do grupo: ')
t2 = input('Insira o líder do grupo: ')
t3 = input('Insira o líder do grupo: ')
t4 = input('Insira o líder do grupo: ')

lista_trabalhos = [t1, t2, t3, t4]
shuffle(lista_trabalhos)
# O shuffle já misturou a ordem, então agora basta imprimir

print('\nA ordem das apresentações será:\n{}'.format(lista_trabalhos))