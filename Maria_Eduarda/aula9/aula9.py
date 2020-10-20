import numpy as np 
from numpy import pi
from numpy import newaxis
import math

"""vetor=np.array([[1.,0.,0.],[0.,1.,2.]]).reshape(3,2)
print(vetor)
print(type(vetor))
vetor=np.arange(15).reshape(3,5)#Formatar o vetor
print(vetor)
print(vetor.shape)#retorna o shape
print(vetor.ndim)#retorna a dimensão
print(vetor.itemsize)#retorna o tamnho em bytes
print(vetor.size)#Return the size 

vetor=np.append(2,3)
print(vetor.dtype)#Tipos dos valores

vetor=np.array(((2,1,3),(4,5,0)),dtype=complex)#coordenada polar
print(vetor)
print(np.zeros((3,4)))
print(np.ones((2,3,4),dtype=np.int16))
print(np.arange(10,30,5))#de 10 até 30 com passo de 5 pode ser um número decimal o passo
print(np.random.random(15))

x=np.linspace(0,2,9)#contém 9 pontos igualmente espaçados
x=np.linspace(0,2*math.pi,10)
f=np.sin(x).reshape(2,3,4)
print(x)
print(f)
a=np.array([20,30,40,50])
b=np.arange(4)
print(a)
print(b)
c=a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)
print(a+35)
print(a-35)
A=np.array([[1,1],[0,1]])
B=np.array([[2,0],[3,4]])
print(A*B)
print(A@B)#Multiplicação matricial
print(A.dot(B))
a=np.ones((2,3),dtype=int)
b=np.random.random((2,3))
a*=3 #multiplicação ponto a ponto
print(a)
b*=a
print(b)
b/=a
print(b)
b-=a
print(b)
b+=a
print(b)
a=np.ones(3,dtype=np.int32)
b=np.linspace(0,pi,3)
print(b.dtype.name)
print(a,b)
c=a+b
d=np.exp(c*1j)
print(d)
a=np.random.random((2,3))
print("Soma",a.sum())
print("Min",a.min())
print("Max",a.max())
b=np.arange(12).reshape(3,4)
print("Somatorio do primeiro eixo",b.sum(axis=0))
print("min do segundo eixo",b.min(axis=1))
print("Somatorio acumulado do primeiro eixo",b.cumsum(axis=0))#integração
a=np.arange(10)**3
print(a[2])
print(a[2:5])
a[:6:2]=-1000#susbtitui
print(a)
print(a[::-1])#inverte a posição

for i in a:
    print(i**(1/3))

def f(x,y):
    return 10*x+y
b=np.fromfunction(f,(5,4),dtype=int)
print(b)
print(b[2,3])
print(b[0:5,1])
c=np.array([[[0, 1, 2],[10, 12, 13]],[[100, 101, 102],[110, 112, 113]]])
print(c)
print(c[-1])
print(c[1,...])#pegar tudo na linha 1

#Pegar toda uma linha
for row in c:
    print(row)
for element in c.flat:
    print(element)

a=np.random.random((2,3))
print(a.T)#transposta
print(a.resize(3,2))#reshape que n retorna nada
print(a)
a=np.floor(10*np.random.random((2,2)))
print("A:",a)
b=np.floor(10*np.random.random((2,2)))
print("B:",b)
print("Vstack:",np.vstack((a,b)))#Concatenação logo após
print("hstack:",np.hstack((a,b)))
print("colum_stack:",np.column_stack((a,b)))"""

a=np.floor(10*np.random.random((2,12)))
print(a)
print("hsplit:",np.hsplit(a,3))
print("hsplit:",np.hsplit(a,(3,4)))#Fzer 4 array de 3 posições