frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase)
# Só é possível alterar a frase, se ela for 'salva', ou seja, se houvesse: frase = frase.replace('Python', 'Android')

print('Curso' in frase)
print(frase.find('Curso'))

print(frase.split()) #Cria uma lista (usa [])
dividido = frase.split()
print(dividido[0])
print(dividido [2][3])


# Para imprimir textos longos, é possível deixá-los em linhas separadas, usando três aspas duplas no início e no final.

print('''Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().''')