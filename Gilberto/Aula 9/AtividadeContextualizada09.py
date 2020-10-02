# Atividade Contextualizada 9

# 1º - Vamos importar a o numpy e a possibilidade de trabalhar com arquivos csv

import csv
import math
import numpy as np

#2º - Vamos criar as listas para armazenar os dados e as variáveis 

sensor1 = list()
sensor2 = list()
angulo = list()
variaveis = ('ax','ay','az','wx','wy','wz')

#3º - Agora iremos criar uma função para calcular os ângulos.

def AnguloCalculo(sensor, angulo, M=0.98, dt=0.05):
    "Calculo do ângulo"
    dado_a = (sensor['ax']/(sensor['ay']**2 + sensor['az']**2)*180/math.pi)
    if len(angulo):
        return M*(angulo[-1] + sensor['wy']*dt) + (1-M) * dado_a
    else: 
        return M*(sensor['ax'] + sensor['wy']*dt) + (1-M)* dado_a

#4º - Vamos abrir o arquivo CSV e realizar as alterações necessárias

with open('C:\\Users\\gilbe\\Documents\\Mestrado\\Programação\\Aula 08\\coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    angreader = csv.reader(arquivo, delimiter="'", quotechar='|')

    n = 0
    for linha in angreader:
        resultado = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        sensor1.append(dict())
        for i in range(len(resultado)):
            sensor1[n][variaveis[i]] = float(resultado[i])
        n+=1
    for linha in angreader:
        resultado = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        sensor2.append(dict())
        for i in range(len(resultado)):
            sensor2[n][variaveis[i]] = float(resultado[i])
        n+=1

arquivoTXT = open('anguloProcessado.txt','w')
arquivoCSV = open('anguloProcessado.csv','w',newline='')
angwriter = csv.writer(arquivoCSV, delimiter= ' ', quotechar='|',quoting=csv.QUOTE_MINIMAL)

arquivoTXT.write('Sensor 1:\n')

for a in sensor1:
    angulo = np.append(angulo, np.around(AnguloCalculo(a,angulo), decimals=3))

arquivoTXT.write('Sensor 2:\n')
for a in sensor2:
    angulo = np.append(angulo, np.around(AnguloCalculo(a,angulo), decimals=3))

for i in angulo:
    print(i)
    arquivoTXT.write(str(i))
    angwriter.writerow(str(i))


# 5º usando a biblioteca do numpy

print('Somatório: ',np.around(angulo.sum(), decimals=3))
print('Média: ', np.around(angulo.mean(), decimals=3))
print('Menor Ângulo: ', np.around(angulo.min(), decimals=3))
print('Maior Ângulo: ', np.around(angulo.max(), decimals=3))
print('Integral do vetor de ângulos: ', np.around(np.trapz(angulo), decimals=3))
DiferencaMedia = [] 
for b in angulo:
    DiferencaMedia.append((np.mean(angulo)-b)**2/len(angulo))
    print('Diferença da média:', DiferencaMedia)
print('Ângulos arredondados:', np.round(angulo),decimal=2)
print('Diferença entre angulos: ', np.around(np.diff(angulo), decimals=3))
variacaoAng = []
for i in range(1,len(angulo)):
    variacaoAng.append(angulo[i]-angulo[i-1])
    print('Variação Angular:', variacaoAng)

print('Arquivos e Resultados gerados.')
arquivoTXT.close()
arquivoCSV.close()
