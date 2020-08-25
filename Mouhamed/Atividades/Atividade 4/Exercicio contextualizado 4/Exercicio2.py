print('Seja bem vindo ao treinamento de sagui')

#Animal habituado
var1 = (input('O animal está habituado? Responda "s" para sim ou "n" para não \n' ))
if var1 == "s":
    resposta1 = var1  

distancia = 30

dist_usuario = float(input('Qual a distância do animal? \n'))

if dist_usuario < distancia:
    print ("Liberar 0.5ml de recompensa") 

tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
if tocar_barra == "s":
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento ainda esta na mesma etapa")
    print ( "O experimento passou para a próxima etapa") # vigésimo toque, se fosse um laço


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

quantidade = input("O experimento foi realizado 50 vezes em 30 minutos? (Responda n para não e s para sim) \n ")

if quantidade == "s":
    print ("O experimento seguirá para a próxima fase") # foi feita dessa forma apenas para simplificar, visto que acima já repeti 20x.


