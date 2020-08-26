print("Cálculadora de IMC.\n")
peso = float(input("Insira seu peso em kg, no formato KK.GGG\n"))
altura = float(input("Insira sua altura no formato M.CM\n"))

resultado = peso/(altura*altura)

print("\nSeu imc é: ", resultado)
print("Você está muito abaixo do peso normal?", resultado < 17)
print("Você está abaixo do peso normal?", (resultado > 17) and (resultado <= 18.5))
print("Você está dentro do peso normal?", (resultado > 18.5) and (resultado <= 25))
print("Você está acima do peso normal?", (resultado > 25) and (resultado <= 30))
print("Você está muito acima do peso normal", resultado > 30)