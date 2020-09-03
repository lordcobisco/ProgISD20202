
lista = ['Gato', 'Cachorro', 'Papagaio']

for palavra in lista:
    print(palavra)

from numpy import random

listanumeros = random.rand(10)
for valor in listanumeros:
    print(valor)

lista = ['Gato', 'Cachorro', 'Papagaio']

for palavra in lista:
    print(palavra)

else:
    print('Todas as palavras foram escritas!')




for key,value in enumerate(['v','i','o','l','a','o']):
    print(key,value)


for key,value in enumerate(['e','n','g','e','n','h','a', 'r', 'i', 'a']):
    print(key,value)


for x in range(5):
    print(x)


for x in range(9,-2,-1):
    print(x)


linguagens = ['Python', 'PHP', 'C#', 'Cobol', 'C++']
tam = len(linguagens)
indices = range(tam)
for item in indices:
    print(linguagens[item])

lista1 = ['bacon', 'fritas', 'picanha']
lista2 = ['cerveja', 'refri','suco']

#for para alimento e bebida 
# print alimento e bebida

for alimento in lista1:
    for bebida in lista2:
        print(alimento,bebida)

lista3 = ['cinema', 'teatro', 'musica']
lista4 = ['matematica', 'fisica','programacao']

for atividadesdelazer in lista3:
    for ciencia in lista4:
        print(atividadesdelazer,ciencia)

contador = 0
while contador < 5:
    print(contador)
    contador = contador +1

'''
contador2 = 0
while contador2 < 30:
    print(contador2)
    contador2 = contador +1

contador3 = 0
while contador3 < 10000:
    print(contador3)
    contador3 = contador +1
'''

for contador in range(5):
    if(contador > 3):
        break
    print(contador)

for contador in range(10):
    if(contador > 5):
        break
    print(contador)

for contador in range(8):
    if(contador > 6):
        break
    print(contador)

contador = 1
while contador < 100 and contador > 0:
    contador = int(input('Digite um numero menor que 100 e maior que zero'))
else:
    print('o numero digitado não está na faixa pedida')

contador = 1
while contador < 5 and contador > 0:
    contador = int(input('Digite um numero menor que 5 e maior que zero'))
else:
    print('o numero digitado não está na faixa pedida')

contador = 26
while contador < 50 and contador > 25:
    contador = int(input('Digite um numero menor que 50 e maior que 26'))
else:
    print('o numero digitado não está na faixa pedida')
    

#######



animaldormindo = 0
while not animaldormindo:
    animaldormindo = int(input('Informe se o animal está dormindo: '))
else:
    print('O animal está acordado')


aperteumatecla = 0
while not aperteumatecla:
    apertouoX = int(input('Deseja continuar no programa ou sair? '))
    
else:
    print('você saiu do programa')


''''

for/while
    break
    continue

# Utilizando esses comandos em um experimento em que o animal pisca os olhos

pisca = 0
mostrarOValorDoCOntador = 0
for contador in range(5):
    pisca = int(input('O animal piscou'))
    if(pisca):
        print('O animal piscou')
        break

    mostrarOValorDoCOntador = int(input('Deseja mostrar o contador'))
    if(not mostrarOValorDoCOntador):
        continue
'''