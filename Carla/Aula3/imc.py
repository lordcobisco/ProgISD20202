#Aula 3- índice de massa corporal (IMC)

print('Programa utilizado para o calculo do IMC.')
peso= float(input("informe seu peso:"))

altura= float(input("informe sua altura:"))
print(type(peso))
imc = peso/(altura ** 2)
print("Muito abaixo do peso",imc < 17)
print("Abaixo do peso normal", 17<= imc < 18.5)
print("Dentro do peso normal", 18.5<= imc < 25)
print("Acima do peso normal", 25<= imc < 30)
print("Muito acima do peso", imc> 30)

