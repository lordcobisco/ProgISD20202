import math
import csv
def imc():
    peso=float(input('Insira seu peso '))
    altura=float(input('Insira sua altura '))
    imc= peso/(altura**2)
    print(imc)
    if(imc<17.0):
        print("Muito abaixo do peso")
        
    elif(imc>=17 and imc<18.5):
        print("Abaixo do peso")
        
    elif(imc>=18.5 and imc<25):
        print("Peso dentro do normal")
        
    elif(imc>=25 and imc<30):
        print("Acima do peso normal")
        
    elif(imc>=30):
        print("Muito acima do peso normal")
    return imc

with open('imc.csv','w') as fileobject:
    calculo=imc()
    fileobject.write(str(calculo))

with open('imc.txt','w') as fileobject:
    calculo=imc()
    fileobject.write(str(calculo))