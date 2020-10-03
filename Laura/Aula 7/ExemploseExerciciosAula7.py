#Funções e classes

def apresentarInterface(): #criar bloco de instruções para apresentar a interface
    """Esta função apresenta a interface"""

    print('Este programa realiza a quisição de dados para análise cinemática')
    print('Digite 1 para acessar a área de análise de dados, 2 para...')

apresentarInterface() #chamando a função
apresentarInterface()
apresentarInterface()
apresentarInterface()
apresentarInterface()


def somaDeListas(lista1,lista2):
    for elemento in zip(lista1,range(0,len(lista1))):
        lista2[elemento[1]]= lista2[elemento[1]] + elemento[0]
    return lista2

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
print(somaDeListas(lista1,lista2))


def lerLista(): #não passou nada como parâmetro de entrada
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10):
        lista[i] = float(input('Digite 10 elementos para a lista: '))
    return lista

print(lerLista())


def arbitrary(x, y, *restanteDasVariaveis):
    print(x+y)
    print(restanteDasVariaveis)

arbitrary(2,4,"André Felipe", 2, 3, 4)


def lerLista(lista = [0,0,0,0,0,0,0,0,0,0]): 
   
    return lista

print(lerLista([1,2,3,4]))


#Recursão - fazer um loop sem usar for e while
def recursao(k):
    if(k > 0): #condição que ele vai parar de fazer a recursão
        result = k+recursao(k-1)
        print(result)

    else:
        result=0
    return result

recursao(10)


cube = lambda x: x*x*x

print(cube(7))


#Classe

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getPointValue(self):
        return [self.x, self.y]

    def hipo(self): #hipotenusa
        return (self.x**2 + self.y**2)**0.5

    def half(self,target):
        return (self.x+target.x)/2 + (self.y+target.y)/2

a = Point(34,85)
b = Point(3,9)
print(a.getPointValue())
print(a.hipo())
print(a.half(b)) #passou um objeto do tipo ponto como parâmetro


#Exercício slide 30: condicionamento operante
def aproximacaosucessiva(contador, tocarBarra):
    if(tocarBarra):
        contador+=1
    return contador

def recomp(som,barra):
    if(som==1 and barra==1):
        print("Liberar 0,5ml de recompensa")
    elif(som==2 and barra==2):
        print("Liberar 0,5ml de recompensa")
    else:
        print("Como o animal não executou a tarefa esperada, não liberar a recompensa")


habituado = int(input("O animal está habituado? (Responda 0 para não e 1 para sim) "))
print("Abaixo, verificaremos se o experimento poderá passar para a próxima fase.")
habituacao(habituado)
tocarBarra=0
contador=0
contador2=0
tocarBarra = int(input("O animal tocou na barra? (Responda 0 para não e 1 para sim) "))
while (contador <=20):
    tocarBarra = int(input("O animal tocou na barra? (Responda 0 para não e 1 para sim) "))
    contador = aproximacaosucessiva(contador, tocarBarra)

#Tocar na barra esquerda ou direita conforme o som emitido
print("Para esta etapa será acionado 50 vezes o som, do tipo 1 ou 2, esperando-se que o animal toque na barra correta.")

contador2=0
while (contador2 <= 50):
    som = int(input("Qual o som foi emitido? (Digite 1 para som1 e 2 para som2) "))
    barra = int(input("Qual a barra que foi tocada pelo animal? (Digite 1 se tocou na barra esquerda e 2 se tocou na direita)  "))
    recomp(som,barra)
    contador2+=1
    
#Verificar se o experimento foi realizado 50x em 30min
tempo=30
qntdExperimento=50

experimento=int(input("Quantas vezes o experimento foi realizado? "))
tempo2=int(input("Em quanto tempo, em minutos, o experimento foi realizado? "))

if(experimento==qntdExperimento and tempo2<=tempo):
    print("Seguir para a próxima fase.")
else:
    print("O experimento não poderá seguir para a próxima fase, pois não foi executado 50 vezes em até 30 minutos.")



#Exercício slide 31: IMC
def indice(peso,altura):
    imc = peso / (altura**2) 
    return imc

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em m: "))
print("Seu IMC é: ", indice(peso,altura))
