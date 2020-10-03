import numpy as np
import csv

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

def Estatistica(x): 
    #Cálculos estatisticos obtidos com a biblioteca numpy
    print('O valor do somatório é:', np.sum(x))
    print('O valor da média é:', np.mean(x))
    print('O menor ângulo é:', np.min(x))
    print('O maior ângulo é:', np.max(x))

   
    # A diferença da média e cada valor do vetor ao quadrado dividida pelo tamanho do vetor
    diferenca_m = [] 
    for i in x:
        diferenca_m.append((np.mean(x)-i)**2/len(x))
    print('Diferença da média:', diferenca_m)

    # A variação angular (ângulo na posição i+1 – ângulo na posição i);
    variacao_angular = [] 
    for j in range(1,len(x)):
        variacao_angular.append(x[j]-x[j-1])
    print('A variação angular:', variacao_angular)

    #Todos os ângulos em graus arredondados (para cima e para baixo e usando como base a regra padrão de arredondamento);

    print('Ângulos em graus arredondados:', np.round(x))

    




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



var1 = np.array(resultado_final1)
var2 = np.array(resultado_final2)
var_total = np.array(respostas)
print(Estatistica(var1))
print(Estatistica(var2))
print(Estatistica(var_total))

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