# Primeiro programa Python - Hello word
print ("Hello world , esse é o meu primeiro programa!")

# Definição de variáveis, print das variáveis e tipo das variáveis 
var_string = "Alexandre Chaves Fernandes"
print (var_string)
print (type(var_string))

var_real = 20.75
print (var_real)
print (type(var_real))

var_int = 50
print (var_int)
print (type(var_int))

var_bool = False
print (var_bool)
print (type(var_bool))

variavel = list()
print (type(variavel))

# Importando módulos em python
import math

# Operadores
soma = 5 + 5
print (soma)
print (5+7) #Soma
print (8-5) #Subtração
print (4*5) #Multiplicação
print (20/2) #Divisão
print (2**5) #Exponencial
print (10//9) #Parte inteira da divisão
print (10%9) #Resto da divisão

soma += 1
print (soma)
soma -= 1
print (soma)
soma *= 1
print (soma)
soma /= 1
print (soma)

x,y,z = 8,9,12
a = 8
b = 9
c = 12

#Expressões lógicas 
print(soma > 2)
print(soma< 2)
print(soma!=2)
print(soma==2)
print(soma<=2)
print(soma>=2)

#Operadores lógicos
variavel_logica1 = True
print ("Valor de not variavel_logica é: ",not variavel_logica1) #Operador not

variavel_logica2 = False
print ("O valor de variavel_logica1 and variavel_logica2 é: ", variavel_logica1 and variavel_logica2) #Operador And
print ("O valor de variavel_logica1 or variavel_logica2 é: ", variavel_logica1 or variavel_logica2) #Operador Or



# Entrada e saída
idade = input("Digite a sua idade em anos")
print (idade)
