# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:26:13 2020

@author: seidi
"""

# função sem parâmetros de entrada e saída
def mensagemDeErro():
    """Não retorna nada, mas mostra na tela uma mensagem de erro clássica"""
    print("Tudo o que você colocou no programa está errado desde o começo.\n")
    print("Favor começar tudo do zero.")

mensagemDeErro()


# função com parâmetros de entrada e saída
def add(x, y):
    """Return x plus y"""
    return x + y

primeiroParametro = int(input("Digite o primeiro numero: "))
segundoParametro  = int(input("Digite o Segundo numero: "))
print(add(primeiroParametro,segundoParametro))


# função com número flexível de parâmetros de entrada
def arbitrary(x, y, *more):
    """Criando uma função que recebe mais parâmetros"""
    print("x=", x, ", y=", y )
    print("arbitrary: ", more)

arbitrary(3,4)
arbitrary(3,4, "Hello World", 3 ,4)

# docstring
print(arbitrary.__doc__)


# escopo e tempo de vida das variáveis em uma função
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)


# função com parâmetro opcional
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

# lista como parâmetro da função
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# recursão
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# funçã anônima
cube = lambda x: x*x*x  
print(cube(7))  

# definição de classe em python
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