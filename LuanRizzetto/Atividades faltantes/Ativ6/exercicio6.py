lista_nomes = ['Luan', 'André', 'Paulo']

for nome in lista_nomes:
    print(nome)

from numpy import random
lista = random.rand(10)
for valor in lista:
    print(valor)

lista_nomes = ['Luan', 'André', 'Paulo']
for nome in lista_nomes:
    print(nome)
else:
    print('todos os nomes foram escritos com sucesso')


for key,value in enumerate(['p','y','t','h','o','n']):
    print(key,value)

for i in range(5):
    print(i)


for i in range(9,-2,-1):
    print(i)

lgg = ['Python', 'PHP', 'C#', 'C++']
tam = len(lgg)
indices = range(tam)
for item in indices:
    print(lgg[item])

lista1 = ['bacon', 'fritas', 'picanha']
lista2 = ['cerveja', 'refrigerante','suco']

for alimento in lista1:
    for bebida in lista2:
        print(alimento,bebida)

contador = 0
while contador < 5:
    print(contador)
    contador = contador +1

for contador in range(5):
    if(contador > 3):
        break
    print(contador)

contador = 1
while contador < 100 and contador > 0:
    contador = int(input('digite um numero menor que 100 e maior que zero'))
else:
    print('o numero digitado não está na faixa')
    
    
animalambientado = 0
while not animalambientado:
    animalambientado = int(input('Informe se o animal está ambientado: '))
else:
    print('O animal está ambientado')


apertouoX = 0
while not apertouoX:
    apertouoX = int(input('Deseja apertar o X? '))
    print('O VS code está em execução')
else:
    print('O programa está finalizando')

for/while
    break
    continue

tocoubarra = 0
mostrarcontador = 0
for contador in range(5):
    tocoubarra = int(input('O animal tocou em pelo menos 1 das barras'))
    if(tocouNaBarra):
        print('O animal tocou na barra')
        break

    mostrarcontador = int(input('Deseja mostrar o contador'))
    if(not mostrarcontador):
        continue
    print(contador)
