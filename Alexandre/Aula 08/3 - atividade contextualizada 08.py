import csv 
import math 

# Função que cumpre o seguinte:  a)	Leia os arquivos em csv de forma a separar os dados dos dois sensores e ficar acessível os dados de aceleração e velocidade angular de cada sensor
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
                   

  

# FUNÇÃO que cumpre o seguinte: 

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

        

 #SALVAR O RESULTADO EM DOIS ARQUIVOS 
 # ÂNGULO PROCESSADO CSV
def anguloProcessado(lista_angulos_sensores1, lista_angulos_sensores2): 
    with open('angulo_processado.csv', 'w', newline= '') as csvFile:
        spamWriter= csv.writer(csvFile, delimiter= ' ',
        quotechar ='|', quoting= csv.QUOTE_MINIMAL)

        spamWriter.writerow (["Ângulos do sensor 1: "]) 
        spamWriter.writerow ([lista_angulos_sensores1])
        spamWriter.writerow (["Ângulos do sensor 2: "])
        spamWriter.writerow ([lista_angulos_sensores2])
    
    with open('angulo_processado.txt', 'w') as arquivo:
        arquivo.write ("Ângulos do sensor 1: ")
        arquivo.write (str(lista_angulos_sensores1))
        arquivo.write (str(lista_angulos_sensores1))








 #ANGULO PROCESSADO TXT       

#EXECUÇÃO       

anguloProcessado(Calcular_angulo(separa_sensores_1()),Calcular_angulo(separa_sensores_2()))





    
