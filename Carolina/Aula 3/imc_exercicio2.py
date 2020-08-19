import math
#valores do peso e altura
peso=float(input('Insira seu peso '))
altura=float(input('Insira sua altura '))
#IMC
imc= peso/math.pow(altura,2)
#Mostrando o valor de IMC
print(imc)

#Mostrando a analise do IMC
print ("Muito abaixo do peso",imc<17.0)

print ("Abaixo do peso",imc>=17.0 and imc<18.5)

print ("Peso dentro do normal",imc>=18.5 and imc<25.0)

print ("Acima do peso normal",imc>=25 and imc<30)

print ("Muito acima do peso normal", imc>=30)