#Exemplos realizados pelo Prof. André enquanto ministrava a aula 4

logicValue = int(input('Você é uma pessoa inteligente? (Responda 0 para não e 1 para sim)'))

if(logicValue):
    print("Não deixe o trabalho para depois!")
    print("Não deixe o trabalho para depois!")
    print("Não deixe o trabalho para depois!")
    print("Não deixe o trabalho para depois!")

print("Depois do IF")

'''
#Operadores logicos not, and, or

not
0 -> 1
1-> 0

and
b1 b2 R
0  0  0
0  1  0
1  0  0 
1  1  1 

or
0  0  0
0  1  1
1  0  1
1  1  1
'''

botao1Apertado = int(input("O rato apertou o botão 1? (Responda 0 para não e 1 para sim) "))
botao2Apertado = int(input("O rato apertou o botão 2? (Responda 0 para não e 1 para sim) "))

if(botao1Apertado):
    print("O botão 1 foi apertado")
if(not botao1Apertado):
    print("O botão 1 não foi apertado!")

if(botao2Apertado):
    print("O botão 2 foi apertado")
if(not botao2Apertado):
    print("O botão 2 não foi apertado!")

if(botao1Apertado and botao2Apertado):
    print("Os dois botões foram apertados")
if(not botao1Apertado and botao2Apertado):
    print("Somente o botão 2 foi apertado")
if(not botao1Apertado and not botao2Apertado):
    print("Os dois botões não foram apertados")
if(botao1Apertado and not botao2Apertado):
    print("Somente o botão 1 foi apertado")

if(botao1Apertado or botao2Apertado):
    print("O botão 1 foi apertado ou o botão 2 foi apertado")
if(not botao1Apertado or botao2Apertado):
    print("O botão 1 não foi apertado ou botão 2 foi apertado")
if(not botao1Apertado or not botao2Apertado):
    print("O botão 1 ou o botão 2 não foram apertados")
if(botao1Apertado or not botao2Apertado):
    print("O botão 1 foi apertado ou botão 2 não foi apertado")



botao1Apertado = int(input("O rato apertou o botão 1? (Responda 0 para não e 1 para sim) "))

if(botao1Apertado):
    print("O botão 1 foi apertado")
else:
    print('O botão não foi apertado')

