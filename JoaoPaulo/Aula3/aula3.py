#Inicio da aula Hello World 

print("este é o meu primeiro programa") #é assim que se comenta o programa

#Importando biblioteca

import math
print(math.sqrt(64))

#Para saber qual o tipo daquela variável, utilizamos o comando type
a = 3.14569
print(type(a))

#operações básicas no python

print(2+2) #soma
print(2-1) #subtraçao
print(2*2) #multiplicação
print(2/2) #divisão
print(2**2) #potenciação
print(10%2) #resto da divisão

#operações lógicas úteis

print(5==5)
print(5!=5)
print(5>3)
print(5>=3)
print(5<3)
print(5<=3)


#questao 1 - IMC

print("Bem vindo ao sistema de cálculo de IMC")

peso = 85
altura = 1.8

IMC = peso/(altura**2)

print(IMC<17)
print(IMC>=17 and IMC<18.5)
print(IMC>=18.5 and IMC< 25)
print(IMC>= 25 and IMC <30)
print(IMC>=30)




#questão 2 com atualização
print("Bem vindo ao sistema de cálculo de IMC")

peso2 = float(input("Digite o seu peso: "))
altura2 = float(input("Digite sua altura: "))

IMC2 = peso2/(altura2**2)

print(IMC2<17)
print(IMC2>=17 and IMC2<18.5)
print(IMC2>=18.5 and IMC2< 25)
print(IMC2>= 25 and IMC2 <30)
print(IMC2>=30)
