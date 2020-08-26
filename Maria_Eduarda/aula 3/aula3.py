
import math #Importando Math
print("Python") 

#Declarando variaveis
varString="maria"
p,l=9,4
escolha=True
variavel=list()

#printando type e variavel na tela
print(varString)
print(type(variavel))
print(type(varString))
print(type(p))
print(str(p) + "top" + str(escolha))
#Captando informações e usando a biblioteca math
x=input('entre com a matriz')
print(x)
k=25
print (math.sqrt(k))

#Operadores
res=5+5
print(res)
print(1+1)
print(1-1)
print(1*1)
print(1//1)
print(1**1)
print(1%1)

p+=1
p-=1
p*=1
p/=1
p%=1

#logico
print(p!=l)
print(p==l)
print(p<=l)
print(p>=l)
print(p>l)
print(p<l)
logic= int(input('tu se acha inteligente'))
log= int(input('tu se acha inteligente'))

if (not logic and not log):
    print("debug breakpoint e f10")
elif (logic or log):
    print("pega else if")
else:
    print("pega else if")
