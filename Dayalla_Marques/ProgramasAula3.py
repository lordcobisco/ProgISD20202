from math import sqrt
#print(sqrt(25))
import math


print("Olá, usuário. Esse programa vai imprimir a raiz quadrada de um número.")
numero = int(input("Digite um número: "))
print(math.sqrt(numero))

nome = 'Aluno do ISD'
print("Isso é o que tem guardado na variável: ", nome)
print(type(nome))

numeroInteiro = 50
print("Isso é o que tem guardado na variável: ", numeroInteiro)
print(type(numeroInteiro))

varFloat = 3.6
print("Isso é o que tem guardado na variável: ", varFloat)
print(type(varFloat))

# Operações matemáticas

variavel = 100 + 100 #Atribuição
print("Esse é o resultado: ", variavel)

print("Aqui irá ser mostrado o resultado de 50 + 50: ")
print(50+50) #Soma

print("Aqui irá ser mostrado o resultado de 30-25: " )
print(30-25) #Subtração

print("Aqui irá ser mostrado o resultado de 20*50: " )
print(20*50) #Multiplicação

print("Aqui irá ser mostrado o resultado de 100/25: ")
print(100/25) #Divisão

print("Aqui irá ser mostrado o resultado de 20 elevado a 10: ")
print(20**10) #exponenciação

print("Aqui irá ser mostrado a parte inteira da divisão de 20 por 9: ")
print(20//9) #Parte inteira da divisão

print("Aqui irá ser mostrado o resto da divisão de 11 por 10: ")
print(11%10) #resto da divisão

# Boleanos
resultado = True
print("O rato roeu a roupa do rei de Roma? ", resultado)
print(type(resultado))


resultado = True
print("O rato roeu a roupa do rei de Roma? ", not resultado)

# Exibindo na tela se é true ou false:

print(45==45)

print(2!=3)

print(2>1)

print(2>=2)

print(25<24)

print(1<=1)
