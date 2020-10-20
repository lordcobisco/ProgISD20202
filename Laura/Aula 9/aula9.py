'''
import numpy as np

vetor = np.array([[1., 0., 0.],[0., 1., 2.]])
print(vetor)
print(type(vetor))


import numpy as np
vetor = np.arange(15).reshape(3,5) #métodos de classe #criando um vetor com 15 elementos para ele ficar com 3 linhas e 5 colunas
print(vetor) #sobrecarga de função
print(vetor.shape) #shape será o número de linhas e colunas #atributos da classe (todos os que tem o .)
print(vetor.ndim) #o número de dimensões
print(vetor.itemsize) #tamanho em bytes de cada elemento da matriz
print(vetor.size) #número de elementos da matriz
print(type(vetor)) #o tipo do vetor = numoy.ndarray

#numpy é uma classe. E toda classe tem métodos e atributos

import numpy as np
vetor = np.array([6,7,8]) #método da classe
print(vetor) #sobrecarga de função
print(vetor.dtype,'\n') #tipo dos elementos do vetor = inteiro 32 #atributo da classe

#vetor = np.array(6,7,8)    não pode criar o vetor assim, sem o []


import numpy as np
vetor = np.array([(1., 0., 0.),(0., 1., 2.)]) #a entrada agora é uma tupla. Pode ser tudo ((()))
print(vetor)

import numpy as np
vetor = np.array(((1., 0., 0.),(0., 1., 2.)), dtype=complex) #a entrada agora é uma tupla
print(vetor)


#Criação de vetores
import numpy as np
print(np.zeros((3,4)))
print(np.ones((2,3,4)))
print(np.ones((2,3,4), dtype=np.int16))
print(np.empty((2,3))) #vetor vazio (na resposta e^309 - próximo de zero)
print(np.arange(10,30,5))
print(np.arange(0,2,0.3),'\n')
print(np.random.random(15)) #gerar números aleatórios
print(np.random.random(15).reshape(3,5))


import numpy as np
from numpy import pi

#x = np.linspace(0,2,9)
x = np.linspace(0,2*pi,100)
f = np.sin(x)
print(x)
print(f)


import numpy as np
vetor = np.arange(6)
print(vetor)

vetor = np.arange(24).reshape(2,3,4)
print(vetor)

vetor = np.linspace(0,2,24).reshape(2,3,4)
print(vetor)


#Operações básicas
import numpy as np
a = np.array([20,30,40,50])
b = np.arange(4)
print(a)
print(b)

c = a-b
print(c)
print(b**2) #b^2
print(a+35)
print(10*np.sin(a))

#Operações lógicas
print(a<35)


#Outras operações com vetores
import numpy as np
A = np.array([[1,1],[0,1]]) #normalmente se dá letras maiúsculas pra matrizes
B = np.array([[2,0],[3,4]])
print(A)
print(B)

print(A*B) #operações entre matrizes - Produto ponto a ponto
print(A@B) #produto matricial
print(A.dot(B)) #mesmo produto de cima, mas com a sintaxe diferente

#Operações acumulativas
import numpy as np
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
print(a)
print(b)

a *= 3
print(a)
b *= a
print(b)
b += a
print(b)
b -= a
print(b)
b /= a
print(b)


#Operações com números complexos
import numpy as np
from numpy import pi
a = np.ones(3,dtype = np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
print(a,b)
c = a+b
d = np.exp(c*1j) #1j é um número complexo
print(d)


import numpy as np
a = np.random.random((2,3))
print("a = ", a, '\n')
print("somatório de a = ", a.sum(), '\n')
print("menor valor de a = ", a.min(), '\n')
print("maior valor de a = ", a.max(), '\n')
b = np.arange(12).reshape(3,4)
print("b = ", b, '\n')
print("somatório do primeiro eixo de b = ", b.sum(axis=0), '\n')
print("menor valor do segundo eixo de b = ", b.min(axis=1), '\n')


import numpy as np
a = np.arange(10)**3
print("a = ", a, '\n')
print("a[2] = ", a[2], '\n')
print("a[2:5] = ", a[2:5], '\n') #acessando um conjunto de posições

a[:6:2] = -1000
print("a = ", a, '\n') #alterar vários valores do vetor
print("a[: :-1] = ", a[: :-1], '\n')

for i in a: #acessar elemento a elemento do vetor a e colocar em i
    print(i**(1/3.))


#Utilizando funções
import numpy as np

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4), dtype=int)
print("b = ", b, '\n')
print("b[2,3] = ", b[2,3], '\n')
print("b[0:5,1] = ", b[0:5,1], '\n') #pegou todos os elementos da segunda coluna


import numpy as np
c = np.array( [[[0,   1,   2],
               [10,  12,   13]],
               [[100, 101,   102],
               [110, 112,   113] ] ] )
print(c)
print(c[-1])
print(c.shape)
print(c[1,...])
print(c[...,2])
print("\n\n\n\n")

for row in c:
    print(row) #elementos de uma submatriz

for element in c.flat:
    print(element)


import numpy as np
a = np.random.random((2,3))
print("a = ", a, '\n')
print("aT = ", a.T, '\n')

print(a.resize(3,2)) #não retorna nada, mas modifica a variável
print(a)
'''

import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random((2,2)))
print("a = ", a, '\n')
b = np.floor(10*np.random.random((2,2)))
print("b = ", b, '\n')

print("vstack((a,b)) = ", np.vstack((a,b)), '\n')
print("hstack((a,b)) = ", np.hstack((a,b)), '\n')

print("column_stack((a,b)) = ", np.column_stack((a,b)), '\n')



