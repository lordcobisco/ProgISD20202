import math
def mensagemDeErro():

    print('Esta tudo errado')
    print('Começa do inicio')


mensagemDeErro()

def add(x, y):
    return x + y

a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))

print(add(a,b))

# mais parametros

def arbitrary(x, y, *more):
    print("x" , x, ", y=", y)
    print("arbitrary: ", more)

arbitrary(3,4)
arbitrary(3,4, "Hello World!", 3, 4)

def my_func():
    x = 10
    print("valor: ", x)

x = 20
my_func()
print("valor: ", x)


def my_function( country = "Norway"):
    print("I am from" + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function( food):
    for x in food:
        print(x)
fruit = ["apple", "banana", "cherry"]
my_function(fruit)


def tri_recursion(k):
    if(k > 0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Exemple Results")
tri_recursion(6)

cube = lambda x: x*x*x

print(cube(7))


class Point:
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x
    def gety(self):
        return self.y
    
    def distOrig(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y)

    def half(self,target):
        mx = (self.x + target.x)/2
        my= (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point (5,12)
mid = p.half(q)

print(mid)
print(mid.getX())
print(mid.gety())