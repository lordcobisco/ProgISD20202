'''
Esses codigos são referentes aos programas da aula 3 de programção
os exercicios de IMC 1 e 2 estão em um arquivo separado .py

Aluna: Carolina Karla de Souza Evangelista
Matricula 202002003

'''

print("hello world!") # comentario em linha

varstring = "carolina evangelista"
varint = "27"
varfloat = "2.7"

print(varstring, varint, varfloat)

import math
print(math.sqrt(100))

print(10+10) #soma
print(10-5) #subtração
print(10/5) #divisão
print(10*10) #multiplicação
print(10**2) #exponenciação
print(10//3) #parte inteira da divisão
print(10%3) #resto da divisão 

varLogica = True
print("valor de 'not varLogica':", not varLogica)

varLogica1 = True
varLogica2 = False
print("valor de 'varLogica1 and varLogica2:", varLogica1 and varLogica2)

print(2==2)
print(2!=2)
print(2>2)
print(2<2)
print(2<=2)

#entradas e saidas

num = input("digite um numero:")
print(num)

login = input("Login:")
senha = input("Senha:")

print("O usuário digitado foi %s e a senha digitada foi %s" %(login, senha))




