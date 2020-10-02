import numpy as np
'''
array = np.array([[1., 0., 0.],[0., 1., 2.]])
print(array)
print(type(array))

array_1 = np.arange(15).reshape(3, 5)
print(array_1)
print(array_1.shape)
print(array_1.ndim)
print(array_1.dtype.name)
print(array_1.itemsize)
print(array_1.size)
print(type(array_1))

array_2 = np.array([6, 7, 8])
print (array_2)
print (type(array_2))

#criação
array_1 = np.array([2, 3, 4])
print (array_1)
print (array_1.dtype, '\n')

array_2 = np.array([1.2, 3.5, 5.1])
print(array_2)
print(array_2.dtype)

array_1 = np.array([1,2,3,4])

array_2 = np.array([(1.5,2,3), (4,5,6)])
print(array_2, '\n')

array_3 = np.array([[1,2],[3,4]], dtype=complex)
print(array_3, '\n')

print(np.zeros ( (3,4) ))
print(np.ones( (2,3,4), dtype=np.int16 ))
print(np.empty( (2,3) ))
print(np.arange( 10,30,5 ))
print(np.arange(0,2,0.3), '\n')

from numpy import pi
print (np.linspace (0, 2, 5))

x = np.linspace(0,2*pi, 100)
print(x, '\n')
f = np.sin(x)
print (f, '\n')

#impressão
array_1 = np.arange(6)
print(array_1, '\n')

array_2 = np.arange(12).reshape(4,3)
print(array_2, '\n')

array_3 = np.arange(24).reshape(2,4,3)
print(array_3, '\n')

print (np.arange(10000), '\n')
print (np.arange(10000).reshape(100,100),'\n')

a = np.array ([20,30,40,50])
b = np.arange (4)
print (b)
c = a-b
print (c)
print (b*2)
print(10*np.sin(a))
print(a<35)

A = np.array ([[1,1],[0,1]])
B = np.array ([[2,0],[3,4]])

print(A*B)
print(A@B)
print(A.dot(B))

a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
print (a)
b += a
print (b)

from numpy import pi

a = np.ones(3, dtype=np.int32)
print (a)
b = np.linspace(0,pi,3)
print (b)
print(b.dtype.name)
c = a+b
print (c)
print (c.dtype.name)
d = np.exp(c*1j)
print (d)
print (d.dtype.name)
'''
