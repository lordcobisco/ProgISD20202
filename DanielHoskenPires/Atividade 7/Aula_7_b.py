'''
def apresentarinterface():
    """ Essa função apresenta a interface"""
    print("Análise cinemática")
    print("Digite 1 para isso, 2 para aquilo...")

apresentarinterface()
apresentarinterface()
apresentarinterface()
apresentarinterface()

def somadelista (lista1, lista2):
    """Essa função soma duas listas"""
    for elemento in zip (lista1, range(0,len(lista1))):
        lista2[elemento[1]] = lista2[elemento[1]] + elemento[0]
    return lista2

lista1 = [1, 2, 3, 4, 5]; lista2 = [1, 10, 20, 30, 40]
print (somadelista(lista1,lista2)) 
print (somadelista.__doc__)

def lerlista():
    lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,10):
        lista[i] = float(input("Digite os 10 elementos de sua lista:\n"))
    return lista

print(lerlista())

def variosparametros(a, b, *segueobaile):
    "Criando funções que recebem vários parâmetros"
    print(a+b)
    print("O restante dos parâmetros são: ", segueobaile)

variosparametros(3, 4, "Daniel", 4.5, "Bão também", "Está rolando", 7.7)

def valordentroeforadafuncao():
    x = 15
    print("O valor dentro da função é: ", x)

x = 33
valordentroeforadafuncao()
print("O valor fora da função é: ", x)

def valordeeegpadraoouinput(frequencia = 50):
    print("A frequência escolhida foi de ", frequencia, "Hz")

valordeeegpadraoouinput()
valordeeegpadraoouinput(60)
valordeeegpadraoouinput(12.6)
valordeeegpadraoouinput()

def recursao(n):
    if(n > 0):
        result = n+recursao(n-1)
        print (result)
    else:
        result = 0 
    return result
recursao(3)
funcaocubica = lambda x: x*x*x

print (funcaocubica(1))
print (funcaocubica(2))
print (funcaocubica(3))
print (funcaocubica(4))
print (funcaocubica(0))


class Point:
    def __init__(self,initx,inity):
        self.x = initx
        self.y = inity
    
    def getpointvalue(self):
        return [self.x, self.y]

    def hipo(self):
        return (self.x**2 + self.y**2)**0.5

    def half(self, target):
        return (self.x+target.x)/2 + (self.y+target.y)/2


a = Point(34,85)
b = Point(3,9)
print (a.getpointvalue()) 
print (a.hipo())
print (a.half(b))
'''
