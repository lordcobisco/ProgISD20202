altura = 1.59
peso = 55

imc = (peso/altura**2)

print("Muito abaixo do peso", imc < 17.0)
print("Abaixo do peso normal", imc >= 17.0 and imc < 18.5)
print("Peso dentro do normal", imc >= 18.5 and imc < 25.0)
print("Acima do peso normal", imc >= 25.0 and imc < 30.0)
print("Muito acima do peso", imc > 30)