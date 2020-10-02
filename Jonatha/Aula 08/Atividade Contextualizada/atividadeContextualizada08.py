from os import system
system('clear')
import csv
import math
sensor1 = list()
sensor2 = list()
variaveis = ('ax','ay','az','gx','gy','gz')
angulo1 = list()
angulo2 = list()

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
    saida1 = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
    saida2 = linha[0].split(',""')[1].split('""')[0].split('[')[1].split(']')[0].split(',')
    sensor1.append(dict())
    sensor2.append(dict())
    for i in range(len(saida1)):
      sensor1[j][variaveis[i]] = float(saida1[i])
      sensor2[j][variaveis[i]] = float(saida2[i])
    j+=1

arquivoTxt = open('anguloProcessado.txt','w')
arquivoCsv = open('anguloProcessado.csv', 'w', newline='')
spamwriter = csv.writer(arquivoCsv, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)

arquivoTxt.write('\n\nSensor 1:\n')

for x in sensor1:
  angulo1.append(ang(x,angulo1))

for i in angulo1:
  print(i)
  arquivoTxt.write(str(i))
  spamwriter.writerow(str(i))

for x in sensor2:
  angulo2.append(ang(x, angulo2))


arquivoTxt.write('\n\nSensor 2:\n')
for i in angulo2:
  print(i)
  arquivoTxt.write(str(i))
  spamwriter.writerow(str(i))

print('Saidas geradas')
arquivoTxt.close()
arquivoCsv.close()
