import csv
import numpy as np

def angulo(dw, da):
    M = 0.98
    dt = 0.05
    ang = 0
    angulo = []
    ang = M * (ang + dw * dt) + (1 - M) * (da)
    return calc_ang

def Angulosprocessados(Sensor_1, Sensor_2):
    with open('Arquivoprocessado.csv', 'w', newline= '') as csvFile:
        spamWriter= csv.writer(csvFile, delimiter= ' ',
        quotechar ='|', quoting= csv.QUOTE_MINIMAL)

        spamWriter.writerow(["sensor 1:\n"]+[Sensor_1]) 
        spamWriter.writerow(["sensor 2:\n"]+[Sensor_2])
    with open('ArquivoProcessado.txt', 'w') as fileObject:
        fileObject.write("sensor 1:\n")
        fileObject.write(str(Sensor_1)) 
        fileObject.write("sensor 2:\n")
        fileObject.write(str(Sensor_2))

Sensor_1 = list()
Sensor_2 = list()

Angulosprocessados(Sensor_1, Sensor_2)

def Soma(angulosensor):
    soma = angulosensor.sum()
    print("Soma: ", soma)

def Menorangulo(angulosensor):
    menorangulo= angulosensor.min()
    print("< Angulo: ", menorangulo)

def Maiorangulo(angulosensor):
    maiorangulo= angulosensor.max()
    print("> angulo: ",maiorangulo)

def Media(angulosensor):
    media= angulosensor.mean()
    print("Media: ", media)

def Variancia(angulosensor):
    variancia= angulosensor.var()
    print("Variancia: ", variancia)

def VariacaoAngular(angulosensor):
    variacao= np.diff(angulosensor)
    print("Variação Angular: ", variacao)

def SomaAcumulada(angulosensor):
    somaacumulada= angulosensor.cumsum()
    print("Soma Acumulada: ", somaacumulada)

def Arredondamentos(angulosensor):        
    arredondamento=np.around(angulosensor, decimals=3)
    print("Arredondamento: ", arredondamento)