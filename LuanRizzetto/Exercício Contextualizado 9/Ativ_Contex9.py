import numpy as np
import csv

def orgDados():
    with open('C:\\Users\\lupc9\\Desktop\\Programação\\coletaFlexJoelho.csv', 'r') as fileObject:
        lista=[]
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp2 = dadosEsp[1].split(']""')[0]
            esp1 = dadosEsp[0].split("[")[1]
            for dadosEsp1 in esp1.split(","):
                lista.append(float(dadosEsp1))
            for dadosEsp2 in esp2.split(","):
                lista.append(float(dadosEsp2))
    return lista

def calcAngulo(W, A):
    M = 0.98
    dt = 0.05
    ang = 0
    ang = M * (ang + W * dt) + (1- M) * (A)
    return ang

def Somatorio():
    somatorio = lista.sum()
    print("Somatorio: ", somatorio)

def Media():
    media = lista.mean()
    print("Media: ", media)

def menorAngulo():
    menorAngulo = lista.min()
    print("Menor Angulo: ", menorAngulo)

def maiorAngulo():
    maiorAngulo = lista.max()
    print("Maior angulo: ",maiorAngulo)

def somaAcumulada():
    somaAcumulada = lista.cumsum()
    print("Soma Acumulada: ", somaAcumulada)

def Variancia():
    variancia = lista.var()
    print("Variancia: ", variancia)

def variacaoAngular():
    variacao = np.diff()
    print("Variação Angular: ", variacao)

def Arredondamento():        
    arredondamento = np.around(lista, decimals=3)
    print("Arredondamento: ", arredondamento)
 
orgDados()
Somatorio()
Media()
menorAngulo()
maiorAngulo()
somaAcumulada()
Variancia()
variacaoAngular()
Arredondamento()
