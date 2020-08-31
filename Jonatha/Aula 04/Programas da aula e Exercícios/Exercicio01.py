# EXERCÍCIO 01 - Índice de massa corporal (IMC) - Estruturas de Decisão
from os import system
system('clear')

print('Programa usado para calcular o indice de massa corporal.')
peso = float(input('Informe seu peso: '))

altura = float(input('Informe sua altura: '))
imc = peso/(altura ** 2)

print('\nIMC: ', imc)
if(imc < 17):
    print('Muito abaixo do peso')
elif (17 <= imc < 18.5):
    print('Abaixo do peso normal')
elif (18.5 <= imc < 25):
    print('Dentro do peso normal')
elif (25 <= imc < 30):
    print('Acima do peso normal')
else:
    print('Muito acima do peso')
