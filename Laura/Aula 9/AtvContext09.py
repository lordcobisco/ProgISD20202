#Atividade Contextualizada 09

import csv
import numpy as np

def lerDadosEsp(filePath = 'coletaFlexJoelho.csv'):
    listaSensores = []
    with open('coletaFlexJoelho.csv','r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                listaSensores.append(float(dadosEsp1))
    return (listaSensores)

listaSensores = lerDadosEsp('coletaFlexJoelho.csv')
print(listaSensores)

#Trazendo os dados do csv e inserindo em uma array:
sensores = np.array(listaSensores)
print(sensores)

listaAngulo = [] 
def calculoAngulo(listaAngulo):
    ang = 0
    M = 0.98
    dt = 0.05

    for n in range(4,len(sensores),4): #o dadow está na quarta posição do vetor, logo, percorrer a cada quatro
        ang = M*(ang+sensores[n]*dt)+(1-M)*sensores[n-3] 
        listaAngulo.append(ang)
    return listaAngulo

angulos = calculoAngulo(listaAngulo)
print(angulos)
angulosN = np.array(angulos)
print(angulosN)

#Cálculo das métricas dos ângulos obtidos

def somatorio(angulosN):
    print("O somatório dos ângulos corresponde a: ", np.sum(angulosN))
somatorio(angulosN)

def media(angulosN):
    print("A média dos ângulos corresponde a: ", np.mean(angulosN))
media(angulosN)

def menorAngulo(angulosN):
    print("O menor ângulo é: ", np.min(angulosN))
menorAngulo(angulosN)

def maiorAngulo(angulosN):
    print("O maior ângulo é: ", np.max(angulosN))
maiorAngulo(angulosN)

def integral(angN):
    integral = angN.cumsum()
    print("A integral do vetor de ângulos (soma acumulada) é: ", integral)
integral(angulosN)

#A diferença da média e cada valor do vetor ao quadrado dividida pelo tamanho do vetor corresponde a variância
def variancia(angN):
    variancia = angN.var()
    print("A diferença da média e cada valor do vetor ao quadrado dividida pelo tamanho do vetor é: ", variancia)
variancia(angulosN)

def variacaoAngular(angulosN):
    print("A variação angular é: ", np.diff(angulosN))
variacaoAngular(angulosN)

def angulosArredondados(angulosN):        
    print("Todos os ângulos em graus arredondados: ", np.around(angulosN, decimals=3))
angulosArredondados(angulosN)
