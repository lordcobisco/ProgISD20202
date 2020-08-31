# Aula 03 - Exercício 01 - índice de massa corporal (IMC)
# Realizada a atulização de entrada de dados (Exercício 2)

print('Índice de Massa Corpotal (IMC)')
altura = float(input('Por favor, digite a sua altura:'))
peso = float(input('Por favor, digite o seu peso:'))
print('Sua altura é %sm e o seu peso é %skg' %(altura, peso))
imc = peso/(altura**2)
print('Seu IMC é: %s' %(imc))
print('Você está:')
if imc < 17:
    print('Muito abaixo do peso.')
if 17 <= imc < 18.5:
    print('Abaixo do peso normal.')
if 18.5 <= imc <25:
    print('Dentro do peso normal.')
if 25 <= imc < 30:
    print('Acima do peso normal.')
if imc>30:
    print('Muito acima do peso.')
print('')
print('Cuide da sua saúde e faça exercícios físicos.')