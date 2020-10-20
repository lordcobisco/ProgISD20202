# inicio da aula hello world 
print("este é o meu primeiro programa") # Esta instrução faz com que a frase escrita entre aspas apareça na tela do terminal  
# cerquilha serve para escrever um comentario e não altera no programa
'''
3 aspas simples também serve para comentar e nada do que for colocado entre as aspas nao aparecerá no programa 
# fim da aula hello world
'''

print("não mostra o print de cima")

# String guarda uma palavra

String = "Andre Felipe"
print(String)
print(String)
print(String)

String = "Não tem mais o nome André"
print(String)
print(String)
print(String)

# varInt guada número inteiro e varRel númeor rel

varInt = 800000
print(varInt)
print(type(varInt))

varReal = 1.2
print(varReal)
print(type(varReal))

# verBool decisão lógica

varBool = True
print("A vida é muito difícil ? ")
print(varBool)

variavel = list()
print(type(variavel))

variavel = varInt
print(type(variavel))

resultadocalculovelocidadelokomat = 50

import math
print(math.sqrt(25))

from math import sqrt
print(sqrt(25))

cinco = 5
cincoNovamente = 5 
resultadoSoma =  5+5
print(resultadoSoma)

resultadodaSoma = cinco + cincoNovamente
print(resultadoSoma)

#Quatro operações 

soma = 2.5+3
subtraçao =  5-9
multiplicaçao = 2*3
divisao = 3/2
print(soma)
print(subtraçao)
print(multiplicaçao)
print(divisao)

# Exponenciação 
print(2**10)
# Parte inteira da divisao
print(10//9)
# Resto da divisao
print(11%10)

#Operadores compostos

variavel9 = 9
somaAcumulada = 0

somaAcumulada += variavel9
print(somaAcumulada)
somaAcumulada += variavel9
print(somaAcumulada)
somaAcumulada += variavel9
print(somaAcumulada)
somaAcumulada += variavel9
print(somaAcumulada)

# Como também pode ser feito 

somaAcumulada = somaAcumulada + variavel9

# o operador resulta em soma acumulada também usando as quatros operações +, -, *, /

a,b,c, = 1,2,3 
a = 1
b = 2
c = 3

# expressoes logicas e operadores relacionados 

verdadeiro = False
print(not verdadeiro)

#expressoes logicas

nome = "Andre Felipe"
print(nome == "Amanda")
print(nome == "Luiz")
print(nome == "Andre Felipe")



nun = input("digite um numero")


print("o numero foi",num)