
import csv

fileObject = open('coletaFlexJoelho.csv', 'r')

sensores = []


##limpando os dados e salvando-os na lista de sensores

for linhas in fileObject:
    valores = linhas.split('],""[') #removendo os caracteres entre os sensores
    valores_sensor1 = valores[0].split('[')[1] #removendo colchete inicial das linhas
    valores_sensor2 = valores[1].split(']"""')[0] #removendo colchetes finais das linhas

    for sensor1 in valores_sensor1.split(","): #removendo as vírgulas entre os valores do sensor 1
        sensores.append(float(sensor1))
    for sensor2 in valores_sensor2.split(","): #removendo as vírgulas entre os valores do sensor 1
        sensores.append(float(sensor2))

print(sensores)

#Criando função para realizar o cálculo da angulação

def calcular():
    ang = 0 #angulação inicial
    valores_calculados = [] #vetor para armazenar respostas do cálculo

    for i in range(4,len(sensores),4): #correr o vetor de 4 em 4 posições, pois é onde ele vaiobter o valor de velocidade angula y
        ang = 0.98*(ang+sensores[i]*0.05)+(1-0.98)*sensores[i-3] #fórmula dada na questão
        valores_calculados.append(ang)#armazenando os valores calculados no vetor
    return valores_calculados

#Salvando os arquivos em dois 

with open('anguloprocessado.csv',  'w', newline = '') as csvfile:
    wr = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting =  csv.QUOTE_MINIMAL) #criando uma planilha que separará os dados

    #criando vetores auxiliarem que armazenaram dados de cada sensor. Os sensores estão agrupados na mesma linha, logo o primeiro é o 1 e o segundo o 2, portanto, as linhasde índice par são do sensor 1 e as linhas de índice impar são do sensor 2.
    sensor1_final = []
    sensor2_final = []

    valores_calculados = calcular()

    for i in range(0,len(valores_calculados),1):#percorre todos os dados ja "limpos" de 1 em 1
        if(i%2 == 0):
            sensor1_final.append(valores_calculados[i]) #indices pares = sensor1
        else:
            sensor2_final.append(valores_calculados[i])  
    wr.writerows(['Sensor 1: ']+ [sensor1_final]) 
    wr.writerows(['Sensor 2: ']+ [sensor2_final]) 

with open('anguloprocessado.txt',  'w', newline = '') as wr:

    sensor1_final = []
    sensor2_final = []
    valores_calculados = calcular()

    for i in range(0,len(valores_calculados),1):#percorre todos os dados ja "limpos" de 1 em 1
        if(i%2 == 0):
            sensor1_final.append(valores_calculados[i]) #indices pares = sensor1
        else:
            sensor2_final.append(valores_calculados[i])  
    wr.writelines(['Sensor 1: ']+ [str(sensor1_final)]) #escrevendo em linhas no txt
    wr.writelines(['Sensor 2: ']+ [str(sensor2_final)]) 