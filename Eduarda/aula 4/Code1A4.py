import math #Importando a biblioteca math para uso de operações como pow
#pegando valores do peso e altura do usuário
peso=float(input('Insira seus peso '))
altura=float(input('Insira seus altura '))
#calculo do IMC
imc= peso/math.pow(altura,2)
#Mostrando o valor de IMC na tela
print(imc)

#Mostrando a analise do IMC
if (imc<17.0):
    print ("Muito abaixo do peso")
elif (imc>=17.0 and imc<18.5):
    print ("Abaixo do peso")
elif (imc>=18.5 and imc<25.0):
    print ("Peso dentro do normal")
elif (imc>=25 and imc<30):
    print ("Acima do peso normal")
elif (imc>=30):
    print ("Muito acima do peso normal")


    

