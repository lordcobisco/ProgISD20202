#Demonstrando a criação de funções

def apresentarInterface():
    print('Este programa realiza a aquisão de dadoss para análise cinemática')
    print('Digite 1 para acessar a área de análise de dado, 2 para realizar outra função')



apresentarInterface()

#Definindo uma função que somará listas

def somaDeListas(lista1,lista2):
    "comentário"
    for elemento in zip(lista1, range(0,len(lista1))):
        lista2[elemento[1]] = lista2[elemento[1]]+elemento[0]
    return lista2

lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]

print(somaDeListas(lista1,lista2))

print(somaDeListas.__doc__) #mostra o que ta escrito abaixo da função

def lerLista():
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10):
        lista[i] = float(input('Digite os elementos da lista'))
    return lista
print(lerLista())

def arbitrario(x,y,*restante):
    print(x+y)
    print(restante)

arbitrario(3,6,"João Paulo", 5,7,8)

##sobrescrevendo parametros

def lerLista(lista = [0,0,0,0,0,0,0,0,0]):
    return lista
print(lerLista("sdçn"))


class Point:
    def __init__(self,initX,initY)
        self.x = initX
        self.y = initY
    def getPointValue(self):
        return[self.x, self.y]
    def hipo():
        return(self.x**2 + self.y**2)**.5
    def half(Self,target):
        return 
a = Point(34,85)