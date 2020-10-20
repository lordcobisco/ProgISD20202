
# Atividade Contextualizada 8

#1º Importando a possibilidade de trabalhar com arquivos csv e math

import csv
import math

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

for x in sensor1:
    angulo.append(AnguloCalculo(x,angulo))

arquivoTXT.write('Sensor 2:\n')
for x in sensor2:
    angulo.append(AnguloCalculo(x,angulo))

for i in angulo:
    print(i)
    arquivoTXT.write(str(i))
    angwriter.writerow(str(i))

print('Arquivos e Resultados gerados.')
arquivoTXT.close()
arquivoCSV.close()

