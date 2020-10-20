import numpy as np
import math



angulos = np.array(angulo_lista)
print(angulos)

lista = []
for linha in angulos:
    soma = linha[0] + linha[1]
    lista.append(soma)
print(lista)
print(sum(lista))

lista2 = []
for linha in angulos:
    listaMedia = angulo.mean()
    lista2.append(listaMedia)

lista3 = []
for linha in angulos:
    menor_angulo = angulos.min()
    lista3.append(menor_angulo)
print(lista3)

lista4 = []
for linha in angulos:
    maior_angulo = angulos.max()
    lista4.append(maior_angulo)
print(lista4)

lista5 = []
for linha in angulos:
    integral = angulos.sum()
    lista5.append(integral)
print(lista5)

lista6 = []
for linha in angulos:
    diferenca = listaMedia - angulos**2
    divisao = diferenca/len(angulos)
    lista6.append(divisao)
print(lista6)

lista7 = []
for linha in angulos:
    variacaoAngular = np.diff(angulos)
    lista7.append(variacaoAngular)
print(lista7)

lista8 = []
for linha in angulos:
    arredondamento = np.around(angulos, decimals = 3)
    lista8.append(arredondamento)
print(lista8)
