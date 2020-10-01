###### AULA 7 #######
#### CAROLINA KARLA DE SOUZA EVANGELISTA ####


######### FUNÇÕES ##########

# soma aaaaa #
def add(x, y):
    return x + y

primeiroparametro = int(input("Digite o prim numero: "))
segundoparametro  = int(input("Digite o seg numero: "))
print(add(primeiroparametro,segundoparametro))

# mensagem #
def erro():
    """mostra uma msg de erro"""
    print("msg de erro\n")

erro()


def funcao():
	x = 10
	print("Value inside function:",x)

x = 20
funcao()
print("Value outside function:",x)


def funcao1(country = "Norway"):
  print("I am from " + country)

funcao1("Sweden")
funcao1("India")
funcao1()
funcao1("Brazil") 

def funcao2(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

funcao2(fruits)

#### classes ####
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