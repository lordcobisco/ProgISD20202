import math
#valores
peso=float(input('Insira seu peso '))
altura=float(input('Insira sua altura '))
imc= peso/math.pow(altura,2)
print(imc)

#analise do IMC
if(imc<17.0):
    print("Muito abaixo do peso")

elif(imc>=17 and imc<25):
    print("Abaixo do peso")

elif(imc>=18.5 and imc<25):
    print("Peso dentro do normal")

elif(imc>=25 and imc<30):
    print("Acima do peso normal")

elif(imc>=30):
    print("Muito acima do peso normal")