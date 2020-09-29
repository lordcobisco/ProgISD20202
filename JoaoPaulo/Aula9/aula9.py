
#importando a biblioteca numpy
import numpy as np 

vetor = np.array([[1., 0.,0.],[0.,1.,2.]])

print(vetor)
print(type(vetor))


'''
import numpy as np 

vetor = np.arrange(15).reshape(3,5) #obriga o vetor a ficar em  um  padrao, nesse caso, 3 linhas e 5 colunas

print(vetor)
print(vetor.shape)#mostra a estrutura escolhida
print(vetor.ndim) #mostra o numero de dimensões
print(vetor.itemsize) #mostra tamanho em bytes para cada elemento
print(vetor.size) #quantos elementos ele possui
#shape é imutável

'''
'''
import numpy as np 
vetor = np.array([6,7,8]) #método de classe
print(vetor) #sobrecarga de função
print(Vetor.dtype, "\n") #atributos de classe
'''
'''
#também podemos entrar com uma tupla

vetor = np.array((1.,0.,0.),(1.,2.,3.,)))
print(vetor)
'''
'''
import numpy as np 

print(np.zero((3,4))) #vetor com 3 linhas e 4 colunas preenchido com zeros
print(np.ones((3,4,4), dtype = np.int16)) #vetor com 3 linhas e 4 colunas e 4 profundidas preenchido com ones
print(np.empty((2,3)))
print(np.arange(10,30,5))
print(np.arange(0,2,0.3),'\n' )
print(np.random.random(15))
print(np.random.random(15).reshape(3,5))

'''
'''
import numpy as np
from numpy import pi

#x = np.linspace(0,2,9)
x = np.linspace(0,2*pi, 100)
f = np.sin(x)
print(x)
print(f)
'''
'''
import numpy as np
vetor = np.arange(12).reshape(2,3) #a partir do zero, entrega 6 valores em dua linhas e 3 colunas

print(vetor)
'''

'''
import numpy as np
a = np.array([20,30,40,50])
b = np.arange(4)

print(a)
print(b)

#operações com vetores e escalar

c1 = a-b
print(c1)
print(b**2)# b ao quadrado, cada elemento
print(10*np.sen(a)) #tira seno de cada elemento de a e multiplica um a um por 10
print(a<35) #operação lógica, returna true e false
print(a+10)#adiciona 10 aos elemento de a
c2 = a+b
print(c2)
'''
'''
#operações entre vetores
import numpy as np
A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])

print(A)
print(B)

print(A*B) #multiplica elementos ponto a ponto
print(A@B) #produto matricial, linha por coluna
print(A.dot(B)) #produto matricial com sintaxe diferente

'''
'''
import numpy ass np

a = np.ones((2,3), dtype = int)
b = np.random.random((2,3))

print(a)
print(b)

a *=3 #multiplica o vetor todo por um escalar
b*= a #multiplica ponto a ponto todos os elementos de b por a
print(b)
b -= a
print(b)
b /= a
print(b)
'''
'''
#Operações com números complexos

import numpy as np
from numpy import pi 
a
'''
'''
import numpy as np
a = np.arange(10)**3
print("a = ", a, '\n')
print("a[2] = ",a[2], '\n') #acessando posição específica
print("a[2:5] = ",a[2:5], '\n') #acessando 5 posições do começo(posicao2) ao fim

a[:6:2] = -1000 #alterar valores das posições
print("a = ", a, '\n')

for i in a:
    print(i**(1/3.))

def f(x,y):
    return 10*x+y
b = np.fromfunction(f,(5,4), dtype=int)
print("b = ",b,'\n')    
print("b[2,3]= ", b[2,3], '\n')
print("b[0:5,1]= ", b[0:5,1], '\n') #pega todos os elementos da segunda coluna
'''
'''
c = np.array([[ [0 , 1, 2],
                [10, 12, 13],
                [100, 101, 102],
                [110, 112, 113] ] ] )


print(c)
print(c[-1]) #de tras pra frente
print(c[1,...])
print(c[...,2])

for row in c:
    print(row) #pega toda linha de c
'''  
'''
import numpy as no

a = np.random.random((2,3))
print("at ", a.T) #transposta
'''
'''
import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random(2,2)))
print("a = ",a,'\n')

b = np.floor(10*np.random.random(2,2)))
print("b = ",b,'\n')

print("vstack((a,b)) = ",np.vstack((a,b)), '\n') #concatena verticalmente
print("hstack((a,b)) = ",np.hstack((a,b)), '\n') #concatena horizontalmente

#para fazer corte

d = np.floor(10*np.random.random(2,12)))
print("hsplit(d,3 = ", np.hsplit(d,3), '\n' ) #divide a matriz em 3 subvetores, fazendo corte horizontal

'''
