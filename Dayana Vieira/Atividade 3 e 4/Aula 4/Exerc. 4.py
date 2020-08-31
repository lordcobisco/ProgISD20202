##################################################################################################################
#Liberei recompensa para o animal a cada toque na barra para servir como estimulado para próximos toques,ou seja,#
#induzir o aprendizado.Além disso, só será realizao o regime de aproximações sucessivas em caso de animais não   #
#habituado.Repeti estimulação mediante ao som por ser um mecanismo, como o toque da barra  em qualque lugar,     #
#primordial para o aprendizado do comportamento,ou seja, necessita de repetição.                                 #
##################################################################################################################

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
     print("\n Reforço do comportamento de se aproximar da barra")
     aproximacao2=int(input("Quantos cm o animal se aproximou da barra: "))
     distanciaatual= aproximacao2-distancia
     if (distanciaatual<30):
         print("Liberar 0.5 de rec")
########TOCAR A BARRA
     print("\n Reforço do comportamento de tocar a barra")
     contador=0
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#1
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#2
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#3
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#4
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#5
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#6
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#7
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
         Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#8
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#9
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#10
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#11
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#12
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#13
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#14
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#15
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#16
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#17
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#18
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#19
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
     Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))#20
     if (Tocar==1):
         contador=contador+1
         print("Liberar 0.5 de rec")
    #21
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))  
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=1
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             if(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
     if (Tocar==1):
         if(contador==20):
             print("****O experimento passou para proxima etapa****") 
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
         elif (contador<20):
             contador=contador+1
             print("Liberar 0.5 de rec")
             Tocar=int(input("O animal tocou em alguma das barras, 1 para sim e 2 para não"))
     else:
         if(contador>=20):
             print("****Reforço do comportamento de tocar a barra mediante a estimulo sonoro****")
             som=int(input("Qual som foi emitido 1 ou 2: "))
             barra=int(input("O animal tocou a barra 1 (esquerda) ou na 2 (direita): "))
             if (som==1 and barra==1):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             elif(som==2 and barra==2):
                 print("Liberar 0.5ml de rec")
                 Tocar=1
                 contador=contador+1
             else:
                 print("Não liberar recompensa!")
                 Tocar=2
#vii
     tempo= int(input("Qual foi o tempo de duração do experimento?"))
     if( contador>=50 and tempo <=30):
         print("*****O experimento seguirá para a próxima fase*****")