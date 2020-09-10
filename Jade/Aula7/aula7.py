'''
def apresentarInterface():
    """Esta função apresenta a interface """
    print('Este programa realiza a aquisição de dados para analise cinemática')
    print('Digite 1 para acessar a área de analise de dados')

apresentarInterface()
apresentarInterface()
apresentarInterface()

def somadelistas(lista1, lista2):
    """Essa função soma duas listas"""
    for elemento in zip(lista1, range(0, len(lista1))):
        lista2[elemento[1]]= lista2[elemento[1]] +elemento[0]
    return lista2

lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]

print(somadelistas(lista1, lista2))
print(somadelistas.__doc__)


def lerLista():
    lista = [0,0,0,0,0,0,0,0,0,0] 
    for i in range(0,10):
        lista[i]= float(input('Digite 10 elementos para a lista'))
    return lista

print(lerLista())

def arbitrary(x,y,*restantedasvariaveis):
    print(x+y)
    print(restantedasvariaveis)

arbitrary(5, 10, "Jade", 50)

def recursao(k):
    if(k>0):
        result= k +recursao(k-1)
        print(result)
    else:
        result =0

    return result
recursao(10) 

cube= lambda x: x*x*x
print(cube(2))

class Point:
    def __init__(self, initX, initY):
        self.x= initX
        self.y= initY
    def getPointValue(self):
        return [self.x, self.y]
    def hipo(self):
        return (self.x **2 + self.y**2)**0.5
    def half(self, target):
        return (self.x + target.x)/2 + (self.y + target.y)/2

a= Point(34,85)
b= Point(3,9)

print(a.getPointValue())
print(a.hipo())
print(a.half(b))
'''
#Exercício Método de discriminação de estímulos auditivos para primatas através do condicionamento operante usando função
def habituacao(habituado):
    if (habituado):
        print("O animal está habituado. Pode iniciar o experimento")
    else:
        print("O animal não está habituado.")
def aproximacoesucessivas(contador, toque):
    if(toque):
        contador= contador +1

    return contador
def Reward(som, barra):
    if (som==1 and barra==1):
        print("Liberar 0.5ml de recompensa")
    elif(som==2 and barra==2):
        print("Liberar 0.5ml de recompensa")
    else:
        print("Não liberar recompensa!")


habituado = int(input("O rato está habituado? (Digite 1 para sim, 0 para não)"))
habituacao(habituado)
toque=0
contador=0
cont=0
while(contador<20):
    toque=int(input("Animal tocou na barra?"))
    contador= aproximacoesucessivas(contador, toque)
while(cont<50):
    som= int(input("Qual som foi emitido(1 ou 2)?"))
    barra= int(input("Qual barra foi acionada(1, para esquerda ou 2, para direita)?"))
    Reward(som, barra)
    cont= cont +1


######## Exercício IMC adaptado para o uso de funções
def calculoIMC(peso, altura):
    imc= peso/ (altura**2)
    return imc
def apresentarIMC(imc):
    if (imc<17):
        print("Você está muito abaixo do peso, IMC: ", imc)
    elif(imc>= 17 and imc <18.5):
        print("Você está abaixo do peso normal, IMC: ", imc)
    elif(imc>= 18.5 and imc < 25):
        print("Você está dentro do peso normal, IMC: ", imc)
    elif(imc>= 25 and imc < 30):
        print("Você está acima do peso normal, IMC: ", imc)
    elif(imc>30):
        print("Você está muito acima do peso, IMC: ", imc)

deseja= 1
while(deseja==1):
    peso=float(input("Digite seu peso:"))
    altura=float(input("Digite sua altura:"))

    imc= calculoIMC(peso,altura)
    apresentarIMC(imc)
    deseja = int(input("Deseja calcular o seu imc novamente?"))  

