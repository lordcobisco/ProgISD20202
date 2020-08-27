#Exercício IMC (sem input)

peso = 46
print("Qual o seu peso em quilogramas? ", peso)
print(type(peso))
altura = 1.52
print("Qual a sua altura em metros? ", altura)
print(type(altura))
imc = peso / (altura**2)
print("Seu IMC é: ", imc)
print(type(imc))

print("Muito abaixo do peso quando o IMC for menor que 17: ", imc<17)
print("Abaixo do peso normal quando o IMC estiver entre 17 e 18.5: ", 17 <= imc < 18.5)
print("Peso dentro do normal quando o IMC estiver entre 18.5 e 25: ", 18.5 <= imc < 25)
print("Acima do peso normal quando o IMC estiver entre 25 e 30: ", 25 <= imc <30)
print("Muito acima do peso quando o IMC estiver acima de 30: ", imc>=30)