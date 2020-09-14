from os import system
system('clear')
import csv
import math
sensor1 = list()
sensor2 = list()
variaveis = ('ax','ay','az','gx','gy','gz')
angulo = list()


def ang(sensor, angulo, M=0.98, dt=0.05):
  dadoa = (sensor['ax']/(sensor['ay']**2 + sensor['az']**2)*180/math.pi)
  #try:
  #  return M*(ang(sensor,angulo) + sensor['gy']*dt) + (1 - M)*dadoa
  #except:
  #  return M*(sensor['ay'] + sensor['gy']*dt) + (1 - M)*dadoa
  if len(angulo): return M*(angulo[-1] + sensor['gy']*dt) + (1 - M)*dadoa
  else: return M*(sensor['ax'] + sensor['gy']*dt) + (1 - M)*dadoa

with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
  spamreader = csv.reader(arquivo, delimiter="'", quotechar='|')

  j = 0
  for linha in spamreader:
    saida = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
    sensor1.append(dict())
    for i in range(len(saida)):
      sensor1[j][variaveis[i]] = float(saida[i])
    j+=1

arquivoTxt = open('anguloProcessado.txt','w')
arquivoCsv = open('anguloProcessado.csv', 'w', newline='')
spamwriter = csv.writer(arquivoCsv, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)

arquivoTxt.write('Sensor 1:\n')

for x in sensor1:
  angulo.append(ang(x,angulo))



for i in angulo:
  print(i)
  arquivoTxt.write(str(i))
  spamwriter.writerow(str(i))

print('Saidas geradas')
arquivoTxt.close()
arquivoCsv.close()








