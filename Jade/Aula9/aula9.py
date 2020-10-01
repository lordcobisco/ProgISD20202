import numpy as np
'''
vetor = np.array([[1., 0., 0.],[0., 1., 2.]]) # métodos da classe
print(vetor)
print(type(vetor))#sobrecarga de função

vetor = np.arange(15).reshape(3,5) # métodos da classe
print(vetor) #sobrecarga de função
print(vetor.shape) # atributos da classe
print(vetor.ndim)# atributos da classe
print(vetor.itemsize)# atributos da classe
print(vetor.size)# atributos da classe

vetor = np.array([6,7,8]) # métodos da classe
print(vetor) #sobrecarga de função
print(vetor.dtype,"\n")# atributos da classe

#vetor = np.array(1,2,3) #wrong

vetor = np.array(((1., 0., 0.),(0., 1., 2.)), dtype=complex) # métodos da classe
print(vetor)

print(np.zeros((3,4)))
print(np.ones((2,3,4), dtype = np.int16))
print(np.empty((2,3)))
print(np.arange(10,30,5))
print(np.arange(0,2,0.3),'\n')
print(np.random.random(15))
print(np.random.random(15).reshape(3,5))

from numpy import pi

#x = np.linspace(0,2,9)
x = np.linspace(0,2*pi,100)
f = np.sin(x)
print(x)
print(f)

vetor = np.arange(24).reshape(2,3,4)
print(vetor)
vetor = np.linspace(0,2,24).reshape(2,3,4)
print(vetor)

a = np.array([20,30,40,50])
b = np.arange(4)
print(a)
print(b)

c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)
print(a+35)
print(a-35)
print(35-a)
c = a+b
print(c)


A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
print(A)
print(B)

print(A*B)
print(A@B)
print(A.dot(B))



a = np.ones((2,3),dtype = int)
b = np.random.random((2,3))
print(a);print(b)

a *= 3
print(a)
b *= a
print(b)
b -= a
print(b)
b += a
print(b)
b /= a
print(b)

a = np.ones(3,dtype = np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
print(a,b)
c = a+b
d = np.exp(c*1j)
print(d)


a = np.random.random((2,3))
print("a = ", a, '\n')
print("somatório de a = ", a.sum(), '\n')
print("menor valor de a = ", a.min(), '\n')
print("Maior valor de a = ", a.max(), '\n')
b = np.arange(12).reshape(3,4)
print("b = ", b, '\n')
print("somatório o primeiro eixo de b = ", b.sum(axis=0), '\n')
print("menor valor do segundo eixo de b = ", b.min(axis=1), '\n')
print("soma acumulada do segundo eixo de b = ", b.cumsum(axis=1), '\n')

a = np.arange(10)**3
print("a = ",a,'\n')
print("a[2] = ",a[2],'\n')
print("a[2:5] = ",a[2:5],'\n')

a[:6:2] = -1000
print("a = ",a,'\n')
print("a[: :-1] = ",a[: :-1],'\n')

for i in a:
    print(i**(1/3.))


def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print("b = ",b,'\n')
print("b[2,3] = ",b[2,3],'\n')
print("b[0:5,1] = ",b[0:5,1],'\n')


import numpy as np
c = np.array( [[[ 0,    1,     2],
               [ 10,   12,    13]],
              [[100, 101,   102],
               [110, 112,   113] ] ] )
print(c)
print(c[-1])
print(c.shape)
print(c[1,...])
print(c[...,2])
print("\n\n\n\n")
for row in c:
    print(row)

for element in c.flat:
    print(element)

import numpy as np
a = np.random.random((2,3))
print("a = ",a,'\n')
print("aT = ",a.T,'\n')

print(a.resize(1,6))
print(a)

from numpy import newaxis

a = np.floor(10*np.random.random((2,2)))
print("a = ",a,'\n')
b = np.floor(10*np.random.random((2,2)))
print("b = ",b,'\n')

print("vstack((a,b)) = ",np.vstack((a,b)),'\n')
print("hstack((a,b)) = ",np.hstack((a,b)),'\n')

print("column_stack((a,b)) = ",np.column_stack((a,b)),'\n')


a = np.floor(10*np.random.random((2,12)))
print("a = ",a,'\n')
print("hsplit(a,3) = ",np.hsplit(a,3),'\n')
print("hsplit(a,(3,4)) = ",np.hsplit(a,(3,4)),'\n')

'''