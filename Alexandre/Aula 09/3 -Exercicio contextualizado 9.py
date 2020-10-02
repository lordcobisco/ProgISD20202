import csv
import numpy as np
import math 


def separa_sensores_1():
    arquivo = open ("coletaFlexJoelho.csv","r")

    lista_dados_sensor_1 = []
    lista_dados_sensor_2 = []

    for line in arquivo:
        dados_dos_sensores = line.split('],""[')
      
        sensor_1 = dados_dos_sensores[0].split('[')[1]
        sensor_2 = dados_dos_sensores[1].split("]")[0]

        sensor_1 = sensor_1.split(",") 
        sensor_2 = sensor_2.split(",")
        
        for i in range (len(sensor_1)):
            sensor_1[i] = float (sensor_1[i])
        for i in range (len(sensor_2)):
            sensor_2[i] = float (sensor_2[i])
       
        lista_dados_sensor_1.append(sensor_1)
        lista_dados_sensor_2.append(sensor_2)
    
    return (lista_dados_sensor_1)
        
def separa_sensores_2():
    arquivo = open ("coletaFlexJoelho.csv","r")

    lista_dados_sensor_1 = []
    lista_dados_sensor_2 = []

    for line in arquivo:
        dados_dos_sensores = line.split('],""[')
      
        sensor_1 = dados_dos_sensores[0].split('[')[1]
        sensor_2 = dados_dos_sensores[1].split("]")[0]

        sensor_1 = sensor_1.split(",") 
        sensor_2 = sensor_2.split(",")
        
        for i in range (len(sensor_1)):
            sensor_1[i] = float (sensor_1[i])
        for i in range (len(sensor_2)):
            sensor_2[i] = float (sensor_2[i])
       
        lista_dados_sensor_1.append(sensor_1)
        lista_dados_sensor_2.append(sensor_2)
    
    return (lista_dados_sensor_2)
                   

  
def Calcular_angulo(lista_dados_sensor):
    angulo_lista = []
    for item in lista_dados_sensor:
        M = 0.98
        dt = 0.05
        dado_w = item[4]
        dado_a = (math.atan((item[0])/math.sqrt((item[1])**2 + (item[2])**2)))* (180/math.pi)
        angulo = (M*(dado_w * dt) + (1- M) * (dado_a))/(1-M)
        angulo_lista.append(angulo)
    return angulo_lista

#Funções com o Numpy

def Somatorio(angulos):
    somatorio= angulos.sum()
    print("Somatorio: ", somatorio)

def Media(angulos):
    media= angulos.mean()
    print("Media: ", media)

def Menor_angulo(angulos):
    menorangulo= angulos.min()
    print("Menor Angulo: ", menorangulo)

def Maior_angulo(angulos):
    maiorangulo= angulos.max()
    print("Maior angulo: ",maiorangulo)

def Integral(angulos):
    somaacumulada= angulos.cumsum()
    print("Soma Acumulada: ", somaacumulada)

def variancia(angulos):
    variancia= angulos.var()
    print("Variancia: ", variancia)

def Variacao_angular(angulos):
    variacao= np.diff(angulos)
    print("Variação Angular: ", variacao)

def graus_arredondados(angulos):        
    arredondamento=np.around(angulos, decimals=3)
    print("Arredondamento: ", arredondamento)
    



      

#EXECUÇÃO DO PROGRAMA    

lista_angulos_sensores1 = Calcular_angulo(separa_sensores_1())
lista_angulos_sensores2 = Calcular_angulo(separa_sensores_2())

#ARRAY
angulo_1_array = np.array(lista_angulos_sensores1)
angulo_2_array = np.array(lista_angulos_sensores2)

#EXECUÇÃO DAS FUNÇÕES
Somatorio(angulo_1_array)
Somatorio(angulo_2_array)

Media(angulo_1_array)
Media(angulo_2_array)

Menor_angulo(angulo_1_array)
Menor_angulo(angulo_2_array)

Maior_angulo(angulo_1_array) 
Maior_angulo(angulo_2_array)

Integral(angulo_1_array)
Integral(angulo_2_array)

variancia(angulo_1_array)
variancia(angulo_2_array)

Variacao_angular(angulo_1_array)
Variacao_angular(angulo_2_array)

graus_arredondados(angulo_1_array)
graus_arredondados(angulo_2_array)

