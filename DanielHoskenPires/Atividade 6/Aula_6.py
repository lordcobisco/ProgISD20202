
for contador in range(5):
    if (contador >4):
        break
    print (contador)

#range
for contador1 in range(9, -20, -3):
    print (contador1)

#string
for caractere in "Daniel Hosken Pires":
    print (caractere)

#lista
ListaNomes = ['Daniel', 'André', 'João', 'Mariana']

for nome in ListaNomes:
    print (nome)

#range/lista
linguagens = ['Python', 'PHP', 'C#', 'PowerBuider', 'Cobol']
tamanho = len(linguagens)
indices = range(tamanho)

for i in indices:
    print (linguagens[i])

#enumerate

for key, value in enumerate (["p", "y", "t", "t", "h", "o", "n"]):
    print (key, value)

linguagens = ['Python', 'PHP', 'C#', 'PowerBuider', 'Cobol']
for i, valor in enumerate (linguagens):
    print ('Linguagem: ' + valor)
    print ('Indice ' + str(i))

#geração de números aleatórios para experimentos

from numpy import random

listaValores = random.rand(10)
for valorIndividual in listaValores:
    print (valorIndividual, "\n")

#Duas ou mais listas

lista1 = ['bacon', 'fritas', 'picanha', 'salada']
lista2 = ['cerveja', 'refrigerante', 'suco', 'ice']

for alimento, bebida in zip (lista1, lista2):
    print (alimento, bebida)

#For/else

ListaNomes = ['Daniel', 'André', 'João', 'Mariana']
for nome in ListaNomes:
    print(nome)
else:
    print ('Todos os nomes foram listados com sucesso')

#while simples
contador = 0 
while contador <5:
    print (contador)
    contador = contador +1

#while/else

condicao = True
while (condicao):
    print ("BLOCO while() e condição == True")
    condicao = False
else:
    print ("BLOCO else e condição == False")

#break: interromper repetição
count = 0
while count <= 5:
    print (count)
    count +=1
    if count >3: break

#break: interromper ciclo
count = -1
while count <5:
    count +=1
    if count == 3: continue
    print (count)

