import math #Importando a biblioteca math para uso de operações como pow
#calculo do IMC
peso=57.5
altura=1.67
imc= peso/math.pow(altura,2)
#Mostrando o valor de IMC na tela
print(imc)

#Mostrando a analise do IMC
print ("Muito abaixo do peso",imc<17.0)

print ("Abaixo do peso",imc>=17.0 and imc<18.5)

print ("Peso dentro do normal",imc>=18.5 and imc<25.0)

print ("Acima do peso normal",imc>=25 and imc<30)

print ("Muito acima do peso normal", imc>=30)