# Aula 03 - Exercício 01 - índice de massa corporal (IMC)

print('Índice de Massa Corpotal (IMC)')
altura = 1.73
peso = 80
print('Sua altura considerada é %sm e o seu peso é %skg' %(altura, peso))
imc = peso/(altura**2)
print('Seu IMC é: %s' %(imc))
print('')
print('Muito abaixo do peso:', imc < 17)
print('')
print('Abaixo do peso normal:', 17 <= imc <18.5)
print('')
print('Dentro do peso normal:', 18.5 <= imc <25)
print('')
print('Acima do peso normal:', 25<=imc<30)
print('')
print('Muito acima do peso:', imc>30)