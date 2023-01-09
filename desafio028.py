from random import randint
from time import sleep #importa a função do delay para simular o pensamento do computador
print('Olá! Eu sou o seu computador e te desafio para um jogo.')
nome = input('Se você estiver pronto, digite seu nome: ')
print('Boa sorte, {}!\nVou pensar em um número inteiro de 0 a 5.'.format(nome.capitalize()))
print('Hmm...')
num = randint(0,5)
sleep(1) #espera de 1s antes de continuar a execução
print('Pronto!')
resposta = int(input('Em qual número você acha que eu pensei? '))
sleep(2)
if resposta == num:
    print('Parabéns, você me venceu!')
else:
    print('Você perdeu, eu pensei no número {}!'.format(num))
