from os import system
system ('clear')

variaveis = ('ax','ay','az','gx','gy','gz')
sensor1 = list()
sensor2 = list()

with open ('coletaFlexJoelho.csv','r') as fileObject:
    for line in fileObject:
        dadosEsp = line.split('],""[')
        listaTemp = dadosEsp[0].split('[')[1].split(',')
        listaTemp2 = dadosEsp[1].split(']')[0].split(',')
        for x in range(len(listaTemp)):
            listaTemp[x] = float (listaTemp[x])
            listaTemp2[x] = float (listaTemp2[x])
        sensor1.append(listaTemp)
        sensor2.append(listaTemp2)

    print ('Senror 1:')
    for x in sensor1:
        print (x, "\n")
    print ('Sensor 2:')
    for x in sensor2:
        print (x, "\n")

#Buscar cada posição da lista
print (sensor1[0][0])
print (sensor1[0][1])
#Assim por diante

#Tive MUUUITA dificuldade em conseguir fazer a função que realize o calculo dos valores. Então deixei aqui até onde consegui abstrair
def ang(sensor, angulo, M=0.98, dt=0.05):
    dadoa = (sensor['ax']/(sensor['ay']**2 + sensor['az']**2)*180/3.141592)
    print (dadoa)
    angulo = M*(angulo['gx'] + angulo['gy']*dt) + (1 - M)*dadoa
    print (angulo)

arquivoTxt = open('anguloProcessado.txt','w')
arquivoCsv = open('anguloProcessado.csv', 'w', newline='')
spamwriter = csv.writer(arquivoCsv, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
arquivoTxt.close()
arquivoCsv.close()

