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

    while (contador1 <20):
        tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
        if tocar_barra == "s":
            contador1 = contador1 + 1

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

    while contador1 <50:
        quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") #contador começa no 20
        if quantidade == "s":
            print ("O experimento segue para a mesma fase") 
            contador1 = contador1 + 1
    condicao = input("O experimento que foi realizado, 50x, foi em 30minutos?")

    if condicao == "s":
        print( "O experimento seguirá para a próxima fase")





