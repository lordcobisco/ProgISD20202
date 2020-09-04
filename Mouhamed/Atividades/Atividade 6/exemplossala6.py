
listaNomes = ['Pedro', 'João', 'Leticia']

for nome in listaNomes:
    print(nome)



listaNomes = ['Pedro', 'João', 'Leticia']
for nome in listaNomes:
    print(nome)
else:
    print("Todos os nomes foram listados com sucesso")


for key, value in enumerate(["p", "y", "t", "h", "o", "n"]): 
    print (key, value)


for i in range(5): 
    print(i)


for caractere in "André Felipe":
    print(caractere)


for item in range(9, -1, -1): 
    print(item) 

linguagens = ['Python', 'PHP', 'C#', 'PowerBuilder', 'Cobol']
tamanho = len(linguagens)
indices = range(tamanho)
 
for i in indices:
    print(linguagens[i])
    

linguagens = ['Python', 'PHP', 'C#', 'PowerBuilder', 'Cobol']
 
for i, valor in enumerate(linguagens):
    print("Linguagem: " + valor)
    print("Indice: " + str(i))

lista_1 = [ "bacon", "fritas", "picanha" ]
lista_2 = [ "cerveja", "refri", "suco" ]

for alimento, bebida in zip(lista_1, lista_2):
    print(alimento, bebida)
    
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1  
    
condicao = True
while(condicao):#<1>
    print("BLOCO while() e condicao==True")#<2>
    condicao = False#<2>
else:
    print("BLOCO ELSE e condicao==False")


count = 0
while count <= 5:
    print(count)
    count += 1
    if count > 3: break


count = -1
while count < 5:
    count += 1
    if count == 3: continue
    print(count)
    
    