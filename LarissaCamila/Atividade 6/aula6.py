'''
listaNomes = ['André', 'Felipe', 'Oliveira']

for nome in listaNomes:
    print(nome)

from numpy import random

listaDeValores = random.rand(10)
for valor in listaDeValores:
    print(valor)

listaNomes = ['André', 'Felipe', 'Oliveira']

for nome in listaNomes:
    print(nome)
else:
    print('Todos os nomes foram escritos com sucesso!')



for key,value in enumerate(['p','y','t','h','o','n']):
    print(key,value)


for i in range(5):
    print(i)


for i in range(9,-2,-1):
    print(i)


linguagens = ['Python', 'PHP', 'C#', 'Cobol', 'C++']
tam = len(linguagens)
indices = range(tam)
for item in indices:
    print(linguagens[item])

lista1 = ['bacon', 'fritas', 'picanha']
lista2 = ['cerveja', 'refri','suco']

#for alimento,bebida in zip(lista1,lista2):
#   print(alimento,bebida)

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
    contador = int(input('Digite um numero menor que 100 e maior que zero'))
else:
    print('o numero digitado não está na faixa pedida')
    


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
'''

tocouNaBarra = 0
mostrarOValorDoCOntador = 0
for contador in range(5):
    tocouNaBarra = int(input('O animal tocou em pelo menos 1 das barras'))
    if(tocouNaBarra):
        print('O animal tocou na barra')
        break

    mostrarOValorDoCOntador = int(input('Deseja mostrar o contador'))
    if(not mostrarOValorDoCOntador):
        continue
    print(contador)