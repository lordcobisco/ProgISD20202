import numpy as np

vetor = np.array([[1.,0.,0.,],[0.,1.,2]])
print(vetor)
print(type(vetor))



import numpy as np

vetor = np.arange(15).reshape(3,5)
print(vetor)
print(vetor.shape)
print(vetor.ndim)
print(vetor.itemsize)
print(vetor.size)
print(type(vetor))

import numpy as np
vetor = np.array(6,7,8)#numero de clase
print(vetor)#sobrecarga de função
print(vetor.dtype,"\n")#atributos da classe

vetor = np.array([1.,0.,0],(0.,1.,2)), dtype=complex # métodos da clase
print(vetor)


import numpy as np
print(np.zero((3,4)))
print(np.ones((2,3,4)+1, dtype = np.int16))
print(np.empty(2,3)))
print(np.arange(10,30,5))
print(np.arange(0,20.3), '\n')
print(np.random(15))
print(np.random.random(15).rashape(3,5))

import numpy as np
from numpy import pi

#x = np.linspace
x = np.linspace
f = np.sin(x)
print  (x)
print(f)

import numpy as np
vetor = np.arange(6).reshape(2,3,4)
print(vetor)
vetor = np.lispace(2,3,4)
print(vetor)

import numpy as np
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

import numpy as np
A = np.array([[1,1],
                [0,1]])
B = np.array([2,0],
                [3,4]

print(A*B)
print(A@B)
print(A.dot(B))

impor numpy as np
a = np.ones((2,3)),dtype = int
b = np.radom,random((2,3))
print(a);print(b)

a *=3
print(a)
b *= a 
print(b)
b -= a 
print(b)
b += a 
print(b)
b /= a
print(b)

import numpy as np
from numpy import pi
a = np.ones(3,dtype = np.int32)
b = np.linespace(0,pi,3)
b = (b.dtype.name)
print(a,b) 
c = a+b
d = np.exp(c*1j)

import numpy as np
a = np.random.random((2,3))
print("a = ", a, '\n')
print(somatório de a = ", a.sum(), '\n')
print(menos valor de a = ", a.min(), '\n')
print(maior valor de a = ", a.max(), '\n')
b = np.arange(12).reshape(3,4)
print("b = ", b, '\n')
print("somatório o primeiro eixo b = ", b.sum(axis=0),'\n')
print(menor valor do segundo eixa b = ", b.min(axis=1))
print("soma acumulada do segundo eixo b = ", b.cumsum(axis=1), '\n')

import numpy as np
a = np.arange(10)**3
print("a = ",a '\n')
print("a[2] = ", a[2], '\n')
print("a[2:5 = ",a[2:5], '\n')
a[ :6:2] = 1000
print("a = ",a,'\n')
print("a[: :-1 = ", a [ : : ])

for i in a :
    print(i**(1/3.))

import numpy as np
def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4), dtype=int)
print("b = ",b, '\n')
print("b[2,3]) = "b,[2,3],'\n')
print("b[0:5,1] = ",b[0:5]), '\n')

import numpy as np
c = np.array([[[0, 1, 2],
            [10, 12, 13]]
            [[100, 101, 102]]
            [110, 112, 113]]])
print(c)
print(c[-1])
print(c.shape)
print(c[1,...])
print(c[...,2])

 for row in c:
     print(row)

for element in c.flat:
    print(element)

import numpy as np
a = np.random.random((2,3))
print("a = ",a, '\n')
print("aT = ", a.T, '\n')

print(a.resize(1,6))
print(a)

import numpy as np
from numpy import newaxis

a= np.floor(10*np.random.random(2,2))
print("a = ",a, '\n')
b = np.floor(10*np.random.random(2,2))
print("b = ",b,'\n')

print(vstack((a,b))) =. np.vstack((a,b)),'\n')
print("hstack(((a,b)) = ", np.hstack((a,b)),'\n')

print("column_stack((a,b))," '\n')

import numpy as np

a = np.floor(10*np.random.random((2,12)))
print ("a = ",a,'\n')
print("hsplit(a,3) = ,np.hsplit(a,3)'\n')
print("hsplit(a,(3,4)) = ", np.hsplit(a(3,4)),'\n')
