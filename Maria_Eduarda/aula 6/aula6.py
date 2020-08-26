#Repetição
import numpy as random
"""listanome=['Maria','Dudu','Franklin']

for nome in listanome:
    print(nome)
else:
    print("PlatformIO paraa de me bugaarrrrrr")

for key,value in enumerate(['d','u','d','a']):
    print(key,value)

for i in range(9,-2,-1): # de 9 a -2 decrementando de -1
    print(i)

churras=['cerveja','beats','suco']
comidas=['frango','queijo','farrofa']

#for alimento,bebida in zip(churras,comidas):
    #print(alimento,bebida)
for alimento in churras:
    for bebida in comidas:
        print(alimento,bebida)"""

#select=Div(text=selecao)

contador=1
#while contador <5:
    #print(contador)
    #contador=contador+1
    
for contador in range(5): # de 9 a -2 decrementando de -1
     if (contador>3):
         print("contador")
         break
     contador=contador+1



"""habituado=int(input("tá"))
while habituado==0:
     habituado=int(input("tá"))
     print("e agora")
     if (habituado==1):
        print("vai q é tua")
        break"""

deseja=int(input("Deseja mostrar o contador"))
contador1=0
for contador1 in range(5):
     if (not deseja):
         continue
     print("duda")
     contador1=contador1+1