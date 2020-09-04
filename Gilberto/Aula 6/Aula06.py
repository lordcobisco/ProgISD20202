'''

for i in range(6):
    print(i)



for item in range(9, -1,-1):
    print(item)



for caractere in "Gilberto Martins":
    print(caractere)


listaNomes = ['Gilberto', 'Martins', 'Filho']

for nome in listaNomes:
    print(nome)



linguagens = ['PHP', 'Python', 'C#', 'PowerBuilder', 'Cobol']
tamanho = len(linguagens)
indices = range(tamanho)

for i in indices:
    print(linguagens[i])

for key, value in enumerate(["p","y","t","h","o","n"]):
    print(key, value)

linguagens = ['PHP', 'Python', 'C#', 'PowerBuilder', 'Cobol']

for i, valor in enumerate(linguagens):
    print("Linguagem: " + valor)
    print("Índice: " + str(i))

from numpy import random

listaValores = random.rand(10)

for valorIndividual in listaValores:
    print(valorIndividual, "\n")

lista_1 = ["Fritas", "Bacon", "Picanha"]
lista_2 = [ "Cerveja", "refrigerante", "Cachaça"]

for alimento, bebida in zip(lista_1, lista_2):
    print(alimento, bebida)

listaNomes = ['Pedro', 'Letícia', 'Thomas']
for nome in listaNomes:
    print(nome)
else:
    print('Todos os nomes foram listados.')

contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1

condicao = True
while(condicao):#<1>
    print('Bloco while() e condicao ==True')#<2>
    condicao = False #<2>
else:
    print("Bloco ELSE e condicao==false")

count = 0
while count <= 15:
    print(count)
    count += 1

count = -1
while count < 6:
    count += 1
    if count ==3: continue
    print(count)
'''

print('Entrada: \nPeso: \nQuantidade:')