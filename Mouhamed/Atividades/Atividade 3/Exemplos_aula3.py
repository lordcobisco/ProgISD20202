# exemplo 1
print("hello word") 

'''
variavel1 = 0
Tudo que está aqui fica apenas como comentário
este é um comentário em bloco

'''

#Variáveis e tipo

varString = "Mouhamed"
print(varString)


varInt = 8
print(varInt)
print(type(varInt))

varfloat = 5.6
print(varfloat)
print(type(varfloat))


variavel = int()
print(type(variavel))

import math
print(math.sqrt(25))

from math import sqrt
print(sqrt(25))



num1 = 5
num2 = 7
resultadoSoma = num1 + num2
print(resultadoSoma)


#Operações

soma = 2.5+3
subtracao = 5-9
multiplicacao = 2*3
divisao = 3/2
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)

print(2**10) #eponienciação
print(10//9) #parte inteira da divisao
print(11%10) #resto da divisão

maisIgual = 9
menosIgual = 9
vezesIgual = 9
divididoigual = 9
moduloigual = 0

maisIgual += 1 #soma o valor com mais 1
menosIgual -= 1 #subtrai
vezesIgual *= 1 #multiplica
divididoigual /= 1 #divide
moduloigual %= 2


a,b,c = 1,2,3
a,b,c = a*2,a+b+c,a*b*c
(x,y) = (1,2)

varLogica = True
print("Valor de 'not varLogica' : ", not varLogica) #ou seja, aparece falso

varLogica1 = True
varLogica2 = False
print ("Mostre os 2: ", varLogica1 and varLogica2) #vai ser falso, pela tabela de lógica

varLogica1 = True
varLogica2 = False
print ("Mostre os 2: ", varLogica1 or varLogica2) #vai ser positivo, pela tabela de lógica. um OU outro

print (2==2)
print (2!=2)
print (2>2)
print (2>=2)
print (2<2)
print (2<=2)

