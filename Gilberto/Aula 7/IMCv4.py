# Aula 07 - Atualização do programa de IMC para o 4.0

def imc(altura, peso):
    """Retornar IMC"""
    return peso / (altura**2)

print('Índice de Massa Corpotal (IMC)')    
altura = float(input('Por favor, digite a sua altura:'))
peso = float(input('Por favor, digite o seu peso:'))
print("Seu IMC é: ", imc(altura,peso))
print('Você está:')
if imc(altura,peso) < 17:
    print('Muito abaixo do peso.')
if 17 <= imc(altura,peso) < 18.5:
    print('Abaixo do peso normal.')
if 18.5 <= imc(altura,peso) <25:
    print('Dentro do peso normal.')
if 25 <= imc(altura,peso) < 30:
    print('Acima do peso normal.')
if imc(altura,peso)>30:
    print('Muito acima do peso.')
print('')
print('Cuide da sua saúde e faça exercícios físicos.')

