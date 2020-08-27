# Exercício IMC (com input)

peso = float(input ("Qual o seu peso em quilogramas? "))
altura = float(input ("Qual a sua altura em metros? "))
imc = peso / (altura**2)
print("Como o seu peso é: %skg e a sua altura é: %sm, logo, o seu IMC será: %s" %(peso, altura, imc))

print("Muito abaixo do peso: ", imc<17)
print("Abaixo do peso normal: ", 17 <= imc < 18.5)
print("Peso dentro do normal: ", 18.5 <= imc < 25)
print("Acima do peso normal: ", 25 <= imc <30)
print("Muito acima do peso: ", imc>=30)