#variaveis

habituado = 0
recompensa = 0
distancia = 30 #centimetros
toques = 0
som1 = 0
barra_esquerda = 0
vezes = 0
tempo = 0
contador_barra_esquerda = 0
contador_vezes = 0
contador_toques = 0

print("Informe se o animal está habituado")
habituado = int(input("Se o animal estiver habituado, digite 1. Caso contrário, digite 0. \n"))

if(habituado == 1):
    print("O animal está habituado. Seguiremos para a próxima etapa do experimento\n")
    distancia = int(input("Informe a distancia entre o animal e as hastes (em centímetros) "))
    
    if(distancia<30):
        recompensa = 1
        if(recompensa == 1):
            print("Libere 0.5ml de recompensa")
        print("Agora precisaremos saber quando o animal tocou na barra (Digite 1 para sim e 0 para não)")
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1
        toques = int(input("O animal tocou  na barra? "))
        if(toques):
            contador_toques += 1



        if(contador_toques == 20):
            print("O experimento deve passar para a próxima etapa\n")

    if(distancia<30 and contador_toques ==20):

        print("Chegamos na próxima etapa do experimento. Aqui vamos investigar se o animal consegue aprender a tocar a \n barra esquerda quando ouve o som 1 e a direita  quando \n ouve o som 2")
        som1 = int(input("O som emitido foi Phee? (Digite 1 para sim e 0 para não) "))

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1
        
        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        barra_esquerda = int(input("O animal tocou a barra esquerda? (Digite 1 para sim e 0 para não) "))
        if(barra_esquerda):
            contador_barra_esquerda +=1

        if(som1 and contador_barra_esquerda == 20 ):
            recompensa = 1
            if(recompensa == 1):
                print("Libere 0.5ml de recompensa")

        elif(not som1 and not barra_esquerda): #se som1 = 0 e barra_esquerda = 0, então ele ouviu som2 e apertou barra direita
            recompensa = 1
            if(recompensa == 1):
                print("Libere 0.5ml de recompensa")
        else:
            print("Não libere nada e apague as luzes por 5s")

        print("Agora precisaremos saber quantas vezes o experimento foi realizado e o tempo de duração")

        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1
        vezes = int(input("O experimento foi realizado? (Digite 1 para sim e 0 para não)" ))
        if(vezes):
            contador_vezes += 1


        tempo = int(input("Há quanto tempo o experimento está sendo feito? "))

        if(contador_vezes >= 50 and tempo >= 30):
            print("O experimento deverá seguir para próxima etapa!")


else:
    print("O animal ainda não está habituado. Habitue-o e inicie novamente.\n")

