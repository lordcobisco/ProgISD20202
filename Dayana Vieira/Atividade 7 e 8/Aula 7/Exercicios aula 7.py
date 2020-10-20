def mensagemDeErro():
    """Não retorna nada, mas mostra na tela uma mensagem de erro clássica"""
    print ("Tudo o que você colocou no programa está errado desde o começo. \n")
    print ("Favor começar tudo do zero.")

mensagemDeErro()



def arbitrary(x,y, *more):
    """Criando uma função que recebe mais parâmetros"""
    print ("x=*", x, ", y=", y)
    print("arbitrary:", more)

arbitrary(3,4)
arbitrary(3,4, "Hello World", 3, 4)

def my_func():
    x=10
    print("Value outside function",x)

x=20
my_func()
print("Value outside function",x)

def my_function (country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana", "cherry"]

my_function(fruits)

def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\zRecursion Example Result")
tri_recursion(6)


cube = lambda x: x*x*xprint(cube(7))

class Point:

    def  _init_(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

def distanceFromOrigin(self):
    return((self.x ** 2)+(self.y ** 2)) ** 0.5

def _str_self(self):
    return "x="+str (self.x)+", y=" + str (self.y)

def halfway (self, target):
    mx = (self.x + target.x)/2
    my = (self.y + target.y)/2
    return Point(mxm,my)



p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)

print (mid)
print(mid.getX())
print (mid.getY())
