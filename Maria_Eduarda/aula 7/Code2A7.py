import math #Importando a biblioteca math para uso de operações como pow
#Função que calcula o IMC

def FuncImc(peso,altura):
    imc= round(peso/math.pow(altura,2),2)
    if (imc<17.0):
        print ("Imc:",imc,"Muito abaixo do peso")
    elif (imc>=17.0 and imc<18.5):
        print ("Imc:",imc,"Abaixo do peso")
    elif (imc>=18.5 and imc<25.0):
        print ("Imc:",imc,"Peso dentro do normal")
    elif (imc>=25 and imc<30):
        print ("Imc:",imc,"Acima do peso normal")
    elif (imc>=30):
        print ("Imc:",imc,"Muito acima do peso normal")

#Chamando a função
peso=float(input('Insira seus peso '))
altura=float(input('Insira seus altura '))

FuncImc(peso,altura)

