#Função toque na barra e toque na barra mediante a estímulo
def toque ():
     print("\n Reforço do comportamento de se aproximar da barra")
     aproximacao2=int(input("Quantos cm o animal se aproximou da barra: "))
     distanciaatual= aproximacao2-distancia
     if (distanciaatual<30):
         print("Liberar 0.5 de rec")
########TOCAR A BARRA
     print("\n Reforço do comportamento de tocar a barra")
     contador=0
     while(contador<=20):
         Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 0 para não: "))#1
         if (Tocar):
             contador=contador+1
             print("Liberar 0.5 de rec")
             if(contador==20):
                 print("****O experimento passou para proxima etapa****") 
                 print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
                 while(contador<50):
                     contador=contador+SOM()
                     if (contador==50):
                         tempo= int(input("Qual foi o tempo de duração do experimento?"))
                         if (tempo<=30):
                             print("*****O experimento seguirá para a próxima fase*****")
def SOM():
    som=int(input("Qual som foi emitido 1 ou 2: "))
    barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
    if (som==1 and barra==1):
        print("Liberar 0.5ml de rec")
        contador=1
    elif(som==2 and barra==2):
        print("Liberar 0.5ml de rec")
        contador=1
    else:
        print("Não liberar recompensa!")
        contador=0
    return contador

#Habituação
print("********FASE DE HABITUAÇÃO ********")
habituacao=int(input("O animal está habituado, 1 para sim  e 0 para não?"))
distancia=30 #R2: i
if (habituacao==1):
    print("Prossiga com os experimentos comportamentais")
    habituado=True   
else:
     print("\n ********Regime de aproximações sucessivas********")
#R2: ii 
     toque()