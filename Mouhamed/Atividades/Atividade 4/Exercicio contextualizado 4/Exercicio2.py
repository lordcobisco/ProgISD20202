print('Seja bem vindo ao treinamento de sagui')

#Animal habituado
var1 = (input('O animal está habituado? Responda "s" para sim ou "n" para não \n' ))
if var1 == "s":
    resposta1 = var1  

distancia = 30
contador1 = 0

dist_usuario = float(input('Qual a distância do animal? \n'))

if dist_usuario < distancia:
    print ("Liberar 0.5ml de recompensa") 

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    contador1 = contador1 + 1

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n') # 20ª vez
if tocar_barra == "s":
    contador1 = contador1 + 1
    if contador1 == 20:
        print ( "O experimento passou de etapa")
    







barra_esquerda = input("O animal tocou a barra esquerda? (Responda n para não e s para sim) \n ")
barra_direita = input("O animal tocou a barra direita? (Responda n para não e s para sim) \n ")
som1 = input("O som1 foi tocado quando tocou a barra esquerda? (Responda n para não e s para sim) \n ")
som2 = input("O som2 foi tocado quando tocou a barra direita? (Responda n para não e s para sim) \n ")


if som1 == "s" and barra_esquerda == "s":
    print ("Liberar 0.5ml de recompensa") 
else:
    print ("Não liberar recompensa")



if som2 == "s" and barra_direita == "s":
    print ("Liberar 0.5ml de recompensa") 
else:
    print ("Não liberar recompensa")

#até o momento será considerado que o experimento foirealizado 20 vezes, visto que passou para a proxima fase

contador1 = 20

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") #contador começa no 20
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 1
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") 
if quantidade == "s":
    print ("O experimento segue para a mesma fase") # 29
    contador1 = contador1 + 1

quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") #experimentoo 50
if quantidade == "s":
    contador1 = contador1 + 1
    if contador1 == 50:
        print ("O experimento seguirá para a próxima fase") 
    








