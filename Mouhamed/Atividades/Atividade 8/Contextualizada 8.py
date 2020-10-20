import csv
import numpy

n = 2000 #excel
info_arq = input("Qual arquivo vocÊ quer abrir? Digite 'coletaFLexJoelho.csv'")

# para armazenar o arquivo que quer abrir : 'coletaFLexJoelho.csv'

print("Abrindo arquivo para separar os dados de cada sensor")

dados_sensor1 = [] #vetores para armazenar os dados dos sensores
dados_sensor2 = []
resultado_final1 = []
resultado_final2 = []
geral = []

with open(info_arq, 'r') as res1:  #arquivo aberto e iniciando manipulação de dados
    for l in res1:
        dados= l.split('],""[') #separando de acordo com a condição
        sensor_1 = dados[0].split('[')[1] # Separando dados do sensor 1. 
        sensor_2 = dados[1][:-5] #sensor2


        for info1 in sensor_1.split(','):
            dados_sensor1.append(float(info1))  # separando e acrescentando os dados nas listas
            geral.append(float(info1))
        for info2 in sensor_2.split(','):
            dados_sensor2.append(float(info2))
            geral.append(float(info2))


def equacao():
    dt=0.05 #dados do exercicio
    M=0.98
    ang=0
    calculo = []
    for i in range(4,len(geral),4):
        ang= M *(ang + geral[i] * dt) + (1- M) * (geral[i-3])  #equação do arquivo
        calculo.append(ang)
    return calculo

with open('Valorfinal.csv',  'w', newline = '') as csvfile:
    wr = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting =  csv.QUOTE_MINIMAL)

    resultado_final1 = []
    resultado_final2 = []
    respostas = equacao()

    for i in range(0,len(respostas),1):
        if(i%2 == 0):
            resultado_final1.append(respostas[i]) #para pegar os pares, que sao do sensor 1
        else:
            resultado_final2.append(respostas[i])  
    wr.writerows(['Sensor 1: ']+ [resultado_final1]) 
    wr.writerows(['Sensor 2: ']+ [resultado_final2]) 

with open('Valorfinal.txt',  'w', newline = '') as wr:

    resultado_final1 = []
    resultado_final2 = []

    respostas = equacao()

    for i in range(0,len(respostas),1):
        if(i%2 == 0):
            resultado_final1.append(respostas[i]) 
        else:
            resultado_final2.append(respostas[i])  
    wr.writelines(['Sensor 1: ']+ [str(resultado_final1)])
    wr.writelines(['Sensor 2: ']+ [str(resultado_final2)]) 