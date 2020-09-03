# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:12:01 2020

@author: seidi
"""

# range
for i in range(5):
  print(i)
  
for item in range(9, -1, -1): 
    print(item) 
    
# string
for caractere in "André Felipe":
    print(caractere)
  
# lista
listaNomes = ['Pedro', 'João', 'Leticia']

for nome in listaNomes:
    print(nome)

# range/lista
linguagens = ['Python', 'PHP', 'C#', 'PowerBuilder', 'Cobol']
tamanho = len(linguagens)
indices = range(tamanho)

for i in indices:
  print(linguagens[i])

# enumerate
for key, value in enumerate(["p", "y", "t", "h", "o", "n"]): 
    print (key, value)

for i, valor in enumerate(linguagens):
  print('linguagem: ' + valor)
  print('indice: ' + str(i))

# geração de números aleatórios
from numpy import random
lista_valores = random.rand(10)

for valor_individual in lista_valores:
  print(valor_individual, '\n')


# uas ou mais listas
lista_1 = [ "bacon", "fritas", "picanha" ]
lista_2 = [ "cerveja", "refri", "suco" ]

for alimento, bebida in zip(lista_1, lista_2):
    print(alimento, bebida)
    
# bloco de código executado ao final da iteração
lista_nomes = ['Pedro', 'João', 'Letícia']
for nome in lista_nomes:
  print(nome)
else:
  print('Todos os nomes foram listados com sucesso')

# while simples
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1  
    
# while/else
condicao = True
while(condicao):#<1>
    print("BLOCO while() e condicao==True")#<2>
    condicao = False#<2>
else:
    print("BLOCO ELSE e condicao==False")

# break
count = 0
while count <= 5:
    print(count)
    count += 1
    if count > 3: break

# continue
count = -1
while count < 5:
    count += 1
    if count == 3: continue
    print(count)