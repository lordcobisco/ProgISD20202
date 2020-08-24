# EXERCÍCIO 01 - Índice de massa corporal (IMC)

print('Programa usado para calcular o indice de massa corporal.')
peso = float(input('Informe seu peso: '))

altura = float(input('Informe sua altura: '))
print(type(peso))
imc = peso/(altura ** 2)
print('Muito abaixo do peso', imc < 17)
print('Abaixo do peso normal', 17 <= imc < 18.5)
print('Dentro do peso normal', 18.5 <= imc < 25)
print('Acima do peso normal', 25 <= imc < 30)
print('Muito acima do peso', imc > 30)
