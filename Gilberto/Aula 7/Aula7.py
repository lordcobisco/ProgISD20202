# Programas da aula 07

def mensagemDeErro():
    """Não retornar nada, mas mostra na tela uma mensagem de erro clássica"""
    print('Tudo o que foi escrito está errado. \n')
    print('Por favor, comece tudo do zero.')

mensagemDeErro()

def add(x, y):
    """Retorne x mais y"""
    return x + y

primeiroParamentro = int(input("Digite o primeiro número"))
SegundoParamentro = int(input("Digite o segundo número"))
print(add(primeiroParamentro, SegundoParamentro))


def arbitrary(x, y, *more):
    """Criando uma função que recebe mais parâmetros"""
    print("X=",x,", y=",y)
    print("arbritary: ",more)

arbitrary(3,4)
arbitrary(3,4, "Hello word", 3, 4)

def func():
    x = 10
    print("Valor dentro da função: ", x)

x = 20
func()
print("Valor fora da função:", x)

def func(country = "Norway"):
    print('I am from '+country)

func("Sweden")
func('Brazil')
func()
func("Japan")


def func(food):
    for x in food:
        print(x)
frutas = ["Maçã", "Banana", "Morango"]

func(frutas)



def recursao(k):
    if(k>0):
        result = k+recursao(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursao exemplos")
recursao(20)


cube = lambda x: x*x*x
print(cube(7))



def somaDeListas(lista1,lista2):
    """Essa função soma duas listas"""
    for elementos in zip(lista1,range(0,len(lista1))):
        lista2[elementos[1]] = lista2[elementos[1]] + elementos[0]
    return lista2

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
print(somaDeListas(lista1,lista2))
print(somaDeListas.__doc__)

def lerlista():
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10):
        lista[i] = float(input('Digite 10 elementos para lista \n'))
    return lista

print(lerlista())


class Point:
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY

    def getPointValue(self):
        return [self.x, self.y]

    def hipo(self):
        return (self.x**2 + self.y**2)**0.5
    
    def half(self, target):
        return (self.x+target.x)/2 + (self.y+target.y)/2

a = Point(34,85)
b = Point(3,9)

print(a.getPointValue())
print(a.hipo())
print(a.half(b))


class Point:

        def __init__(self, initX, initY):
            self.x = initX
            self.y = initY
        
        def getX(self):
            return self.x
        
        def getY(self):
            return self.y
        
        def distanceFromOrigin(self):
            return ((self.x ** 2)+ (self.y ** 2)) ** 0.5
        
        def __str__(self):
            return "x=" + str(self.x) + ", y=" + str(self.y)
        
        def halfway(self, target):
            mx = (self.x + target.x)/2
            my = (self.y + target.y)/2
            return Point(mx, my)
p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())
print(mid.distanceFromOrigin())        


