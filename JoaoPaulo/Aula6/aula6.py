'''
listaNomes = ['João', 'Paulo', 'Bezerra', 'Fernandes']

for nome in listaNomes:
    print(nome)
'''

'''
para baixar uma nova biblioteca, digitar pip install numpy no console

'''
'''
from numpy import random

listaDeValores = random.ran(10)
for valor in listaDeValores:
    print(valor)

'''
'''
for i in range(5):
    print (i)
#vai de 9 ate -2 decrementando de 1 em 1
for i in range(9,-2,-1):
    print(i)
'''
'''
linguagens = ['Python', 'php', 'c++']
tam = len(linguagens)
indices = range(tam)
for item in indices:
    print(linguagens[item])
'''

'''
lista1 = ['bacon', 'fritas','picanha']
lista2 = ['cerveja','refri','suco']
'''
'''
for alimento, bebida in zip(lista1,lista2):
    print(alimento,bebida)
'''
'''
for alimento in lista1:
    for bebida in lista2:
        print(alimento)
        print(bebida)

'''
#exercicitando while
'''
contador = 0

while contador<5:
    print(contador)
    contador = contador +1

for contador in range(5):
    if(contador>4):
        break
    print(contador)

    #tanto faz um ou outro, fazem a mesma coisa
 '''
'''
contador = 1
while contador < 100 and contador>0:
     contador =  int(input("Digite um numero maior que 100 e menor que 0"))
else:  
    print("O numero digitado nao está na faixa pedida")   
'''
#break interrompe qualquer estrutura de repetição
