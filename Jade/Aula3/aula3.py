'''
###Código da aula3

print('Hello World')
#Para comentar usamos cerquilha, para comentar um bloco usamos tres aspas simples
x= 3
print(x)
#Para fazer o debug pressionamos F5
from math import sqrt
print(sqrt(25))

import math
print(math.sqrt(25))

varString = "Andre Felipe"
print(varString)
print(type(varString))

varInt = 1
print(varInt)
print(type(varInt))

varFloat = 1.2
print(varFloat)
print(type(varFloat))

resultadoSoma = 5+5 #Atribuição
print(resultadoSoma)

print(5+5) #Soma
print(2-5) #Subtração
print(2*5) #Multiplicação
print(10/2) #Divisão
print(2**10) #exponenciação
print(10//9) #Parte inteira da divisão
print(11%10) #resto da divisão

varBool = True
print(varBool)
print(type(varBool))

varLogica = True
print("Valor de 'not varLogica': ", not varLogica)

print(2==2)
print(2!=2)
print(2>2)
print(2>=2)
print(2<2)
print(2<=2)
'''
#Exercício IMC
peso=56
altura=1.55
imc= peso/ (altura**2)
print(imc<17)
print(imc>= 17 and imc <18.5)
print(imc>= 18.5 and imc < 25)
print(imc>= 25 and imc < 30)
print(imc>30)

#Exercício IMC com input
peso2=float(input("Digite seu peso:"))
altura2=float(input("Digite sua altura:"))
imc2= peso2/ (altura2**2)
print(imc2<17)
print(imc2>= 17 and imc2 <18.5)
print(imc2>= 18.5 and imc2 < 25)
print(imc2>= 25 and imc2 < 30)
print(imc2>30)