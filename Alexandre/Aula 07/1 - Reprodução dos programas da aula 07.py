# REPRODUÇÃO DOS PROGRAMAS DAS AULA 07 

#DEFINIR FUNÇÃO SIMPLES E APRESENTARA FUNÇÃO 

def apresentar_interface():
    "Essa função é responsável por apresentar interface"
    print ("Esse programa irá realizar a obtenção de dados para análise do movimento")
    print ("\nDigite 1 para acessar a área da anákise dos dados e 2 para informações sobre os parâmetros")

apresentar_interface()

#FUNÇÃO MAIS COMPLEXA COM VALORES DE ENTRADA
def somaDeListas(lista1,lista2):
    "Essa função é responsável por somar duas listas nas respectivas posições"
    for elemento in zip(lista1,range(0,len(lista1))):
        lista2[elemento[1]] = lista2[elemento[1]] + elemento[0]
    return lista2


lista1 = [1, 2, 3, 4, 5]; lista2 = [1, 2, 3, 4, 5]
print("\n",somaDeListas(lista1,lista2))

#Comentários obre a função
print(somaDeListas.__doc__)

#FUNÇÃO COM INPUT
def lerLista():
    lista = [1,1,1,1,1,1,1,1,1,1]
    for i in range(0,10):
        lista[i] = float(input('\nDigite 10 elementos para a lista'))
    return lista

print(lerLista())

#fUNÇÃO RECURSÃO
def recursao(k):
    "Função que irá fazer um loop sem utilizar for ou while"
    if(k > 0):
        result = k+recursao(k-1)
        print(result)
    else:
        result = 0
    return result

recursao(8)

#FUNÇÃO ANÔNIMA 
cube = lambda x: x*x*x

print(cube(5))

#CLASSE
class Point:
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY
    
    def getPointValue(self):
        return [self.x, self.y]

    def hipo(self):
        return (self.x**2 + self.y**2)**0.5

    def half(self,target):
        return (self.x+target.x)/2 + (self.y+target.y)/2

a = Point(5,4)
b = Point (6,7)

print(a.getPointValue())
print(a.hipo())

print(a.half(b))