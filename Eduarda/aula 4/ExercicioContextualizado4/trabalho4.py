#Habituação
print("********FASE DE HABITUAÇÃO ********")
habituacao=input("O animal está habituado, sim ou não?")
distancia=30 #R2: i

if (habituacao=="SIM" or habituacao== "sim"):
    print("O animal está habituado")
    habituado=True
    
else:
    print("Prossiga com os experimentos até ele está habituado")

print("\n ********Regime de aproximações sucessivas********")
#R2: ii 
print("\n Reforço do comportamento de se aproximar da barra")
aproximacao2=int(input("Quantos cm o animal se aproximou da barra: "))
distanciaatual= aproximacao2-distancia
if (distanciaatual<30):
    print("Liberar 0.5 de rec")
Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
if (Tocar==1):
   print("Liberar 0.5 de rec")

#R2:iii
toque=int(input("Quantas vezes o animal tocou na barra: "))
if (toque>=20 and toque<50):
     print("****O experimento passou para proxima etapa****")
#R2:iv ~ vii
print("\nReforço do comportamento de tocar a barra")
som=int(input("Qual som foi emitido 1 ou 2: "))
barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
if (som==1 and barra==1):
    print("Liberar 0.5ml de rec")
elif(som==2 and barra==2):
    print("Liberar 0.5ml de rec")
else:
    print("Não liberar recompensa!")

#vii
toque=input("Quantas vezes o experimento foi repetido?")
tempo= int(input("Qual foi o tempo de duração do experimento?"))
if(int(toque)>=50 and tempo <=30):
    print("*****O experimento seguirá para a próxima fase*****")

        


