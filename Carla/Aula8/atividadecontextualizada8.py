
import csv

fileObject = open('coletaFlexJoelho.csv', 'r')

sensor = []


for linhas in fileObject:
    valores = linhas.split('],""[') 
    valores_sensor_a = valores[0].split('[')[1] 
    valores_sensor_b = valores[1].split(']"""')[0] 

    for sensora in valores_sensor_a.split(","): 
        sensor.append(float(sensora))
    for sensorb in valores_sensor_b.split(","): 
        sensor.append(float(sensorb))

print(sensor)



def calcular():
    ang = 0 
    calculo_ang = [] 

    for i in range(4,len(sensor),4): 
        ang = 0.98*(ang+sensor[i]*0.05)+(1-0.98)*sensor[i-3] 
        calculo_ang.append(ang)
    return calculo_ang



with open('anguloprocessado.csv',  'w', newline = '') as csvfile:
    wr = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting =  csv.QUOTE_MINIMAL) 

    
    sensora_novo = []
    sensorb_novo = []

    calculo_ang = calcular()

    for i in range(0,len(calculo_ang),1):
        if(i%2 == 0):
            sensora_novo.append(calculo_ang[i]) 
        else:
            sensorb_novo.append(calculo_ang[i])  
    wr.writerows(['Sensor a: ']+ [sensora_novo]) 
    wr.writerows(['Sensor b: ']+ [sensorb_novo]) 

with open('angulofinal.txt',  'w', newline = '') as wr:

    sensora_final = []
    sensorb_final = []
    calculo_ang = calcular()

    for i in range(0,len(calculo_ang),1):
        if(i%2 == 0):
            sensora_final.append(calculo_ang[i]) 
        else:
            sensorb_final.append(calculo_ang[i])  
    wr.writelines(['Sensor a: ']+ [str(sensora_final)]) 
    wr.writelines(['Sensor b: ']+ [str(sensorb_final)]) 