
def apresentaarInterface():
    """ Esta função apresenta a interface"""

    print('Este rpgramarealiza a aquisição de dados para análise cinemática')
    print('digite 1 para acessar a área de ánalise de dados, 2 para ....')

apresentaarInterface()
apresentaarInterface()
apresentaarInterface()
apresentaarInterface()
apresentaarInterface()



def somaDeListas(lista1,lista2):
    """ essa função soma duas listas """
    for elemento in zip(lista1,range(0,len(lista1)-1))):
        lista2[elemento[1]] = lista2[elemento[1]] + elemento[0]
    return lista2

lista1 = [1, 2, 3, 4, 5]; lista2 = [1, 2, 3, 4, 5]
print(somaDelistas(lista1,lista2)[1])
print(somaDeListas.__doc__)



def lerLista():
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range( 0,10 ):
        lista[i] = float(input('Digite 10 elementos para a lista'))
    return lista

print(lerLista())

def arbitrary(x,y,*restanteDasVaariaveis):
    print(x+y)
    print(restanteDasVaariaveis)

arbitrary(2,4,"Andre Feelipe",2,3,4)


def lerLista():
    lista = [0,0,0,0,0,0,0,0,0,0]
    
    return lista

print(lerLista())

def recursao(k):
    if(k > 0):
        resultado = k+recursao(k-1)
        print(result)
    else:
        result = 0
    return result

recursao(10)


cube = lambda x: x*x*x
print(cube(2))


class Point:
    def__init__(self,initx,inity):
    self.x = initx
    self.y = inity

    def getPointValue():
        return [self.x, self.y]

    def hipo(sef):
        return (self.x**2 + self.y**2)**0.5
        
    def half(self,target):
        return (sel.x+target.x)/2 +(self.y+target.y)/2

    a = Point(34,85)
    b = Point(3,9)

print(a.getPointValue())
print(a.hipo())

print(a.half(b))


