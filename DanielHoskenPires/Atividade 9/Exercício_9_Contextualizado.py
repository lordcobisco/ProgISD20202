from os import system
system('clear')
import csv
import math
import numpy as np
sensor1 = np.array([])
sensor2 = np.array([])
variaveis = ('ax','ay','az','gx','gy','gz')
angulo = np.array([])



def ang(sensor, angulo, M=0.98, dt=0.05):
  dadoa = (sensor[0]/(sensor[1]**2 + sensor[2]**2)*180/math.pi)
  #try:
  #  return M*(ang(sensor,angulo) + sensor['gy']*dt) + (1 - M)*dadoa
  #except:
  #  return M*(sensor['ay'] + sensor['gy']*dt) + (1 - M)*dadoa
  if len(angulo): return M*(angulo[-1] + sensor[4]*dt) + (1 - M)*dadoa
  else: return M*(sensor[0] + sensor[4]*dt) + (1 - M)*dadoa

with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
  spamreader = csv.reader(arquivo, delimiter="'", quotechar='|')
  j = 0

  for linha in spamreader:
    saida = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
    lista = list()
    for i in range(len(saida)):
      lista.append(float(saida[i]))
    lista = np.array(lista)
    if j == 0:
      sensor1 = np.array(lista)
    else: sensor1 = np.vstack((sensor1,lista))
    j+=1

arquivoTxt = open('anguloProcessado.txt','w')
arquivoCsv = open('anguloProcessado.csv', 'w', newline='')
spamwriter = csv.writer(arquivoCsv, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)

arquivoTxt.write('Sensor 1:\n')

for x in sensor1:
  angulo = np.append(angulo, np.around(ang(x,angulo), decimals=2))

for i in angulo:
  #print(i)
  arquivoTxt.write(str(i))
  spamwriter.writerow(str(i))

print('Saidas geradas')
arquivoTxt.close()
arquivoCsv.close()


print('Somatório: ',np.around(angulo.sum(), decimals=2))
print('Média: ', np.around(angulo.mean(), decimals=2))
print('Angulo menor: ', np.around(angulo.min(), decimals=2))
print('Angulo maior: ', np.around(angulo.max(), decimals=2))
print('Integral: ', np.around(np.trapz(angulo), decimals=2))
print('Variancia: ', np.around(angulo.var(), decimals=2))
print('Diferença entre angulos: ', np.around(np.diff(angulo), decimals=2))