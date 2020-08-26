altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = (peso/altura**2)

if imc < 17.0:
    print("Muito abaixo do peso!")
elif imc >= 17.0 and imc < 18.5:
    print("Abaixo do peso normal")
elif imc >= 18.5 and imc < 25.0:
    print("Peso dentro do normal")
elif imc >= 25.0 and imc < 30.0:
    print("Acima do peso normal")
elif imc > 30:
    print("Muito acima do peso")