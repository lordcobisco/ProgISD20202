habituacao=int(input("O animal está habituado?"))
distancia=30
if (habituacao==True):
    print("Prossiga com experimentos")  
else:
    aproximacao=int(input("O animal se aproximou da barra quantos centímetros? "))
    distancia2= aproximacao-distancia 
    if (distancia2<30):
        print("Liberar 0.5 de rec")
    contador=0
    barra=int(input("O animal tocou na barra?")) #01
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #02
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #03
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #04
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #05
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #06
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #07
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #08
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #09
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #10
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #11
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #12
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #13
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #14
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #15
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #16
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #17
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #18
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #19
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    barra=int(input("O animal tocou na barra?")) #20
    if (barra==1):
        contador=contador+1
        print("Liberar 0.5 de rec")
    if (contador==20):
        print("próxima etapa")
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