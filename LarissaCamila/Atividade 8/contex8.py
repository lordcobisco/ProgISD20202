import csv

Sensor_1 = list()
Sensor_2 = list()

def sensores():
    documento = open("coletaFlexJoelho.csv", "r")
    for line in documento:
        dados = line.split('],""[')

      
        sensor_1 = dados[0].split('[')[1]
        sensor_2 = dados[1].split("]")[0]

        sensor_1 = sensor_1.split(",") 
        sensor_2 = sensor_2.split(",")
        
        for i in range (len(sensor_1)):
            sensor_1[i] = float (sensor_1[i])
        for i in range (len(sensor_2)):
            sensor_2[i] = float (sensor_2[i])
       
        Sensor_1.append(sensor_1)
        Sensor_2.append(sensor_2)
    
    return (Sensor_1, Sensor_2)

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

Angulosprocessados(Sensor_1, Sensor_2)