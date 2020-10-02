'''
def mensagemDeErro():
Não se retorna nada, mas mostra na tela uma mensagem clássica de erro
print ("Tudo que você colocou no programa está errado desde o início!!!\n")
print ("Favor começar tudo do zero!!!\n")

mensagemDeErro()

def add(x, y):
    """Return x plus y"""
    return x + y
primeiroParametro = int (input("Digite o primeiro número: "))
segundoParametro = int (input("Digite o segundo número: "))
print (add(primeiroParametro, segundoParametro))

#Criando uma função que recebe mais parâmetros
def arbitrary(x, y, *more):
    print ("x=", x, ", y=", y)
    print ("arbitrary: ", more)

arbitrary (3,4)
arbitrary (6,7)
arbitrary (3,4, "Hello world", 3, 4)
arbitrary (6,9, "Hello world", 6, 7)

#Escopo e tempo de vida das variáveis em uma função
def my_funcao ():
    x = 10
    print ("Value inside function:", x)
x = 20
my_funcao()
print ("Value outside function:", x)
x = 34
my_funcao()
print ("Value outside function:", x)

#Com parâmetros opicionais
def my_function (country = "Norway"):
    print ("I am from " + country)
pais = input("Digite qual é o seu país: ")
my_function ("Sweden")
my_function ("Índia")
my_function ()
my_function ("Brazil")


#Passando lista como parâmetro
def my_funcao(food):
    for x in food:
        print (x)
fruits = [input("Qual nome da fruta? ")]
my_funcao(fruits)

def teste(algo):
    print (nome)
nome = input("Digite qual é o seu país: ")  
teste(nome)

#Recursão - Uma função chamando a si mesma
def tri_recursion (k):
    if (k>0):
        result = k+tri_recursion(k-1)
        print (result)
    else:
        result = 0
    return result
print ("\n\nRecursion Example Results")
tri_recursion(6)

#Função cúbica
cube = lambda x: x*x*x
print (cube(7))

def somaDeListas (lista1, lista2):
    for elemento in zip (lista1,range(0,len(lista1))):
        lista2[elemento[1]] = lista2[elemento[1]] + elemento[0]
    return lista2

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]

print (somaDeListas(lista1,lista2))

def lista():
    Numeros = [0, 0, 0, 0]
    for i in range(0,10):
        Numeros[i] = float(input("Digite um número para a lista: "))
    return Numeros

print(lista())

def arbitrary (x, y, *algumaCoisaMais):
    print (x*y)
    print (algumaCoisaMais)

arbitrary(2, 3, "Daniel Hosken", "Blablabla", 3.5)

#classe
class Point:
    def __init__ (self, initX, initY):
        self.x = initX
        self.y = initY
    def getPointValue(self):
        return[self.x, self.y]

    def hipo(self):
        return (self.x**2 + self.y**2)**0.5

a = Point (34, 85)
print (a.getPointValue())
print (a.hipo())
'''