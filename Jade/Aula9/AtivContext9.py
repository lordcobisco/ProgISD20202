import numpy as np
import csv
def CalculoAngulo(dadow, dadoa):
    M=0.98
    dt=0.05
    ang=0
    ang= M *(ang + dadow * dt) + (1- M) * (dadoa)
    return ang

def Somatorio(angsensor):
    somatorio= angsensor.sum()
    print("Somatorio: ", somatorio)

def Media(angsensor):
    media= angsensor.mean()
    print("Media: ", media)

def MenorAngulo(angsensor):
    menorangulo= angsensor.min()
    print("Menor Angulo: ", menorangulo)

def MaiorAngulo(angsensor):
    maiorangulo= angsensor.max()
    print("Maior angulo: ",maiorangulo)

def SomaAcumulada(angsensor):
    somaacumulada= angsensor.cumsum()
    print("Soma Acumulada: ", somaacumulada)

def Variancia(angsensor):
    variancia= angsensor.var()
    print("Variancia: ", variancia)

def VariacaoAngular(angsensor):
    variacao= np.diff(angsensor)
    print("Variação Angular: ", variacao)

def Arredondamentos(angsensor):        
    arredondamento=np.around(angsensor, decimals=3)
    print("Arredondamento: ", arredondamento)


s1=[]
s2=[]
filePath= 'coletaFlexJoelho.csv'
with open(filePath, 'r') as fileObject:
    for line in fileObject:
        dadosSensor= line.split('],""[')
        sensor1 = dadosSensor[0].split('[')[1]
        sensor2 = dadosSensor[1][:-5]
        
        for dadosSensor1 in sensor1.split(','):
            s1.append(float(dadosSensor1))
        for dadosSensor2 in sensor2.split(','):
            s2.append(float(dadosSensor2))
    

    n = 2000
    splited1 = []
    splited2 = []
    angulos_s1= []
    angulos_s2= []
    len_l = len(s1)
    for i in range(n):
        start = int(i*len_l/n)
        end = int((i+1)*len_l/n)
        splited1.append(s1[start:end])
        splited2.append(s2[start:end])
        
        angulos_s1.append(CalculoAngulo(splited1[i][4], splited1[i][1]))
        angulos_s2.append(CalculoAngulo(splited2[i][4], splited2[i][1]))

    angs1=np.array(angulos_s1)
    angs2=np.array(angulos_s2)

    Somatorio(angs1)
    Somatorio(angs2)

    Media(angs1)
    Media(angs2)

    MenorAngulo(angs1)
    MenorAngulo(angs2)

    MaiorAngulo(angs1) 
    MaiorAngulo(angs2)

    SomaAcumulada(angs1)
    SomaAcumulada(angs2)

    Variancia(angs1)
    Variancia(angs2)

    VariacaoAngular(angs1)
    VariacaoAngular(angs2)

    Arredondamentos(angs1)
    Arredondamentos(angs2)  



