def habituacao():
    habituacao=int(input("O animal está habituado?"))
    distancia=30
    if (habituacao==True):
        print("Prossiga com experimentos")  
    else:
        aproximacao=int(input("O animal se aproximou da barra quantos centímetros? "))
        distancia2= aproximacao-distancia 
        if (distancia2<30):
            print("Liberar 0.5 de recompensa")
        contador=0
        while contador<=20: # utilizando while #
            barra=int(input("O animal tocou na barra?")) 
            if (barra==1):
                contador=contador+1
                print("Liberar 0.5 de recompensa")
            else:
                print("Não liberar recompensa!")
                if (contador==20):
                    print("próxima etapa")

def treino():
    print("Etapa de discriminação auditiva")
    som=int(input("Qual som foi emitido? Digite 1 ou 2:"))
    barra=int(input("Qual barra foi apertada? Digite 1 para esquerda e 2 para direita"))
    if (som==1 and barra==1):
        print("Liberar 0.5ml de recompensa")
    elif(som==2 and barra==2):
        print("Liberar 0.5ml de recompensa")
    else:
        print("Não liberar nada")
    tempo=int(input("Quanto tempo durou o experimento?"))
    quantidade=int(input("Quantas vezes o animal apertou a barra?"))
    if(tempo>30 and quantidade==50):
        print("Iniciar proxima fase!")
    else:
        print("Não passou para a proxima fase!")

habituacao()
treino()