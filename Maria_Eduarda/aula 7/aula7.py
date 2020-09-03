#Definindo função
def apresentaInterface():
    print("Mostro coisas")
def somar(x,y):
     """soma lista"""
     w=x+y
     print("Essa função soma")
     print("Winx! Sei que você vai querer ser uma de nós")
     return w

print(somar(1,2))

def somaDeListas(lista,lista2):
    for elemento in zip(lista,range(0,len(lista))):
         lista2[elemento[1]]=lista2[elemento[1]]+elemento[0]
         return lista2

u=[1,8,9,4,5]
k=[1,2,3,4,5]
print(somaDeListas(u,k))
print(somar.__doc__)
def lerlista():
     lista=[]
     for i in range(0,10):
         res=float(input("digite"))
         lista.insert(i,res)
     return lista

print(lerlista())

def lerlista2(lista=[0,0,0]):
     return lista

print(lerlista2())

#função recursiva
def recursivo(k):
     if(k>0):
         result=k + recursivo(k-1)
         print(result)
     else:
         result=0
     return result

recursivo(5)


#função anonima
cube=lambda x: x*x*x
print(cube(7))
class point:
    def __init__(self,initX,initY):
        self.x=initX
        self.y=initY
    def getpoint(self):
        return[self.x, self.y]
    def hipo(self):
        return (self.x**2 + self.y**2)**0.5
    def half(self,target):
        return (self.x+target.x)/2 + (self.y+target.y)/2
a=point(3,5)
print(a.getpoint())
b=point(2,6)
c=point(2,6)
print(b.hipo())
print(b.half(c))
print(a['x'])