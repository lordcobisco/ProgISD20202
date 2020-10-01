# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:42:58 2020

@author: seidi
"""

import numpy as np

# Básico
array = np.array([[ 1., 0., 0.],[ 0., 1., 2.]])
print(array)
print(type(array))

import numpy as np
array_1 = np.arange(15).reshape(3, 5)
print(array_1)
print(array_1.shape)
print(array_1.ndim)
print(array_1.dtype.name)
print(array_1.itemsize)
print(array_1.size)
print(type(array_1))

array_2 = np.array([6, 7, 8])
print(array_2)
print(type(array_2))

# Criação e impressão de vetores
# Criação, parte 1
array_1 = np.array([2,3,4])
print(array_1)
print(array_1.dtype,"\n")

array_2 = np.array([1.2, 3.5, 5.1])
print(array_2)
print(array_2.dtype)

# Criação, parte 2
#array_1 = np.array(1,2,3,4)    # WRONG
array_1 = np.array([1,2,3,4])  # RIGHT

array_2 = np.array([(1.5,2,3), (4,5,6)])
print(array_2, "\n")

array_3 = np.array( [ [1,2], [3,4] ], dtype=complex )
print(array_3, "\n")

# Criação, parte 3
print(np.zeros( (3,4) ))
print(np.ones( (2,3,4), dtype=np.int16 ))
print(np.empty( (2,3) ))
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ), "\n")

# Criação, parte 4
from numpy import pi
print(np.linspace( 0, 2, 9 ))
x = np.linspace( 0, 2*pi, 100 )
print(x, "\n")
f = np.sin(x)
print(f, "\n")

# Impressão, parte 1
array_1 = np.arange(6)                         # 1d array
print(array_1,"\n")

array_2 = np.arange(12).reshape(4,3)           # 2d array
print(array_2,"\n")

array_3 = np.arange(24).reshape(2,3,4)         # 3d array
print(array_3,"\n")

# Impressão, parte 2
print(np.arange(10000),"\n")
print(np.arange(10000).reshape(100,100),"\n")

# Operações aritméticas por elemento
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)

# Outras operações
A = np.array( [[1,1],
              [0,1]] )
B = np.array( [[2,0],
              [3,4]] )
print(A * B,"\n")                       # elementwise product
print(A @ B,"\n")                       # matrix product
print(A.dot(B),"\n")                    # another matrix product


a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
print(a)
b += a
print(b)
#a += b                  # b is not automatically converted to integer type


a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
c = a+b
print(c)
print(c.dtype.name)
d = np.exp(c*1j)
print(d)
print(d.dtype.name)


a = np.random.random((2,3))
print("a = ",a,"\n")
print("sum a = ",a.sum(),"\n")
print("Min a = ",a.min(),"\n")
print("Max a = ",a.max(),"\n")
b = np.arange(12).reshape(3,4)
print("b = ",b,"\n")
print("sum b = ",b.sum(axis=0) ,"\n")                          # sum of each column
print("Min b = ",b.min(axis=1) ,"\n")                           # min of each row
print("cumsum b = ",b.cumsum(axis=1),"\n")

# Operações universais
B = np.arange(3)
print("B = ",B,"\n")
print("exp B = ",np.exp(B),"\n")
print("sqrt B = ", np.sqrt(B),"\n")
C = np.array([2., -1., 4.])
print("add B,C = ",np.add(B, C),"\n")

# Vetores Unidimensionais
a = np.arange(10)**3
print("a = ",a,"\n")
print("a[2] = ",a[2],"\n")
print("a[2:5] = ",a[2:5],"\n")
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; 
                  #from start to position 6, exclusive, 
                  # set every 2nd element to -1000
print("a = ",a,"\n")
print("a[: :-1] = ",a[ : :-1],"\n")                                 # reversed a
for i in a:
  print(i**(1/3.))

# Vetores Multidimensionais
def f(x,y):
  return 10*x+y
b = np.fromfunction(f,(5,4),dtype=int)
print("b = ",b,"\n")
print("b[2,3] = ",b[2,3],"\n")
print("b[0:5, 1] = ",b[0:5, 1],"\n")                       # each row in the second column of b
print("b[ : ,1] = ",b[ : ,1],"\n")                        # equivalent to the previous example
print("b[1:3, : ] = ",b[1:3, : ],"\n")


c = np.array( [[[  0,  1,  2],      # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])
print("c[-1]  = ",c[-1],"\n")       # the last row. Equivalent to b[-1,:]
print("c.shape = ",c.shape,"\n")
print("c[1,...] = ",c[1,...],"\n")  # same as c[1,:,:] or c[1]
print("c[...,2]  = ",c[...,2],"\n") # same as c[:,:,2]

for row in c:
  print(row)

for element in c.flat:
  print(element)

# Mudando o formato de um vetor
a = np.floor(10*np.random.random((3,4)))
print("a  = ",a,"\n")
print("a.shape  = ",a.shape,"\n")

print("a.ravel()  = ",a.ravel(),"\n")  # returns the array, flattened
print("a.reshape(6,2)  = ",a.reshape(6,2),"\n")  # returns the array with a modified shape
print("a.T  = ",a.T,"\n")  # returns the array, transposed
print("a.T.shape  = ",a.T.shape,"\n")
print("a.shape  = ",a.shape,"\n")


a = np.floor(10*np.random.random((3,4)))
print("a  = ",a,"\n")
print("a.resize((2,6))  = ",a.resize((2,6)),"\n")
print("a  = ",a,"\n")
print("a.reshape(3,-1)  = ",a.reshape(3,-1),"\n")

from numpy import newaxis

a = np.floor(10*np.random.random((2,2)))
print("a  = ",a,"\n")
b = np.floor(10*np.random.random((2,2)))
print("b  = ",b,"\n")
print("vstack((a,b))  = ",np.vstack((a,b)),"\n")
print("hstack((a,b))  = ",np.hstack((a,b)),"\n")

print("a  = ",np.column_stack((a,b)),"\n") # with 2D arrays
a = np.array([4.,2.])
b = np.array([3.,8.])
print("column_stack((a,b))  = ",np.column_stack((a,b)),"\n") # returns a 2D array
print("hstack((a,b))  = ",np.hstack((a,b)),"\n")       # the result is different
print("a[:,newaxis]  = ",a[:,newaxis],"\n")           # this allows to have a 2D columns vector
print("column_stack((a[:,newaxis],b[:,newaxis]))  = ",np.column_stack((a[:,newaxis],b[:,newaxis])),"\n")
print("hstack((a[:,newaxis],b[:,newaxis]))  = ",np.hstack((a[:,newaxis],b[:,newaxis])),"\n")  # the result is the same

# Dividindo vetores em vetores menores
a = np.floor(10*np.random.random((2,12)))
print("a  = ",a,"\n")
print("hsplit(a,3)  = ",np.hsplit(a,3),"\n")        # Split a into 3
print("hsplit(a,(3,4))  = ",np.hsplit(a,(3,4)),"\n")# Split a after the third and the fourth column

# Cópias e Visualizações
# Nenhuma cópia
a = np.arange(12)
b = a            # no new object is created
print(b is a)    # a and b are two names for the same ndarray object
b.shape = 3,4    # changes the shape of a
print(a.shape)

def f(x):
  print(id(x))
print(id(a))     # id is a unique identifier of an object
f(a)

# View ou shallow copy
a = np.arange(12)
c = a.view()
print(c is a,"\n")
print(c.base is a ,"\n")    # c is a view of the data owned by a
print(c.flags.owndata,"\n")
c.shape = 2,6               # a's shape doesn't change
print(a.shape,"\n")
c[0,4] = 1234               # a's data changes
print(a,"\n")
s = a[1:3]     # spaces added for clarity; could also be written "s = a[:,1:3]"
s[:] = 10      # s[:] is a view of s. Note the difference between s=10 and s[:]=10
print(a,"\n")

# Deep copy
a = np.arange(12)
d = a.copy()            # a new array object with new data is created
print(d is a,"\n")
print(d.base is a,"\n") # d doesn't share anything with a
d[0] = 9999
print(a,"\n")
a = np.arange(int(1e8))
b = a[:100].copy()
del a  # the memory of ``a`` can be released.