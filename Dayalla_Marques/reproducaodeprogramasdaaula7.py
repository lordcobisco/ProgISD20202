'''
# Reproduzindo programas básicos de funções

def add(x, y):
    """return x plus y"""
    return x + y

a = int(input("Digite o primeiro número: "))
b  = int(input("Digite o segundo número: "))
print(add(a,b))

def mensagemDeErro():
    """Não retorna nada"""
    print("Tudo o que você colocou no programa está errado.\n")
    print("começar de novo.")

mensagemDeErro()

def arbitrary(x, y, *more):
    """Criando uma função que recebe outros parâmetros"""
    print("x=", x, ", y=", y )
    print("arbitrary: ", more)

arbitrary(100,4)
arbitrary(100,4, "Dayalla", 100 ,4)

print(arbitrary.__doc__)


def my_func():
	w = 15
	print("Value inside function:",w)

w = 15
my_func()
print("Value outside function:",w)


def my_function(cidade = "Natal"):
  print("Eu sou do " + cidade)

my_function("Macaíba")
my_function("Mossoró")
my_function("Goianinha")
my_function("Brejinho") 

def my_function(comidas):
  for x in comidas:
    print(x)

frutas = ["maçã", "banana", "pêra"]

my_function(frutas)

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

cube = lambda x: x*x*x  
print(cube(7))  

# Classes

class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

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