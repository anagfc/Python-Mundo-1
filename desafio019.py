from random import choice
a1 = input('Insira o nome do aluno 1: ')
a2 = input('Insira o nome do aluno 2: ')
a3 = input('Insira o nome do aluno 3: ')
a4 = input('Insira o nome do aluno 4: ')

lista_alunos = [a1, a2, a3, a4]
print("\nQuem apagará o quadro será {}.".format(choice(lista_alunos)))