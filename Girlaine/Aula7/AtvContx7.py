'''
def apresentaarInterface():
    """ Esta função apresenta a interface """

    print('Este programa tem como objetivo automatizar e análisar o estudo optogenetico que será últilizado junto a outors dispositivos')

apresentaarInterface()

Inicio = int(input(" Iniciar o programa ? (Responda 0 para não e 1 para sim"))
if(Inicio):
    print('Sim')
else:
    print('Não')

print(' Definir a intensidade do LedRGB')

def ledRGB():
    """ Essa função define a intensidade do ledRGB """

    intensidade = [1,2,3]
    for i in range( 1 ):
        intensidade[i] = float(input('Digite a intensidade para o vermelho'))
        intensidade[i] = float(input('Digite a intensidade para o verde'))
        intensidade[i] = float(input('Digite a intensidade azul'))
    return ledRGB

print(ledRGB())

ledRGB = int(input(" Qual led deseja usar agora? ( Responda = 1 vermelho, 2 Verde, 3 azul)"))

if(ledRGB == 1 ):
    print('vermelho')
elif (ledRGB == 2):
    print('verde')
elif (ledRGB == 3):
    print('azul 3')

else:
    print('todos')

def MatrizEletrodo():
    """ Essa função determina as matrizes dos eletrodos """

    Canal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range( 32 ):
        Canal[i] = float(input('Canal correspondente'))
    return Canal

print(MatrizEletrodo()) 

class Point: 
    def __init__(self, initLedRGB,initMatrizEletrodo):
        
        self.LedRGB = initLedRGB
        self.MatrizEletrodo = initMatrizEletrodo
    
    def getLedRGB(self):
        return self.LedRGB

    def getMatrizEletrodo(self):
        return self.MatrizEletrodo
    
print('Tempo de experimento')

ledRGB = int(input(" Acionar lede? ( Responda = 1 vermelho, 2 Verde, 3 azul)"))

if(ledRGB == 1 ):
    print('vermelho')
elif (ledRGB == 2):
    print('verde')
elif (ledRGB == 3):
    print('azul 3')

else:
    print('todos')

ledRGB()
'''
AjustarTempoLedRGB = int(input(" Ajustar tempo ? (Responda 0 para não e 1 para sim"))
if(AjustarTempoLedRGB):
    print('Sim')
else:
    print('Não')

import time
import sys 

Momento = time.time()
tempo = time.time()-Momento

print('Fim do programa')