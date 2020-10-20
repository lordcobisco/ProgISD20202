
import csv
import numpy as np

fileObject = open('coletaFlexJoelho.csv', 'r')

sensores1 = []
sensores2=[]


##limpando os dados e salvando-os na lista de sensores
def limpa():
    for linhas in fileObject:
        valores = linhas.split('],""[') #removendo os caracteres entre os sensores
        valores_sensor1 = valores[0].split('[')[1] #removendo colchete inicial das linhas
        valores_sensor2 = valores[1].split(']"""')[0] #removendo colchetes finais das linhas

        for sensor1 in valores_sensor1.split(","): #removendo as vírgulas entre os valores do sensor 1
            sensores1.append(float(sensor1))
            
        for sensor2 in valores_sensor2.split(","): #removendo as vírgulas entre os valores do sensor 1
            sensores2.append(float(sensor2))
            
    return sensores1,sensores2


def valor_a (sensor):
    return np.arctan(sensor[0]/(np.sqrt(sensor[1]**2 + sensor[2]**2))) * 180/np.pi

def valor_w (sensor):
    return np.arctan(sensor[3]/(np.sqrt(sensor[4]**2 + sensor[5]**2))) * 180/np.pi

def angulacao(anterior,sensor):

    M = 0.98
    dt = 0.05

    return M * (anterior + valor_w(sensor) * dt) + (1 - M) * valor_a(sensor)

def contas(angulacao):
    print("Somatório dos angulos:", np.sum(angulacao))
    print("Média dos angulos:", np.mean(angulacao))
    print("Menor angulo:", np.min(angulacao))
    print("Maior angulo:", (np.max(angulacao)))

    diff = []
    for a in angulacao:
        diff.append((np.mean(angulacao)-a)**2/len(angulacao))
    print("Diferença da média", diff)

    va = []
    for i in range(1,len(angulacao)):
        va.append(angulacao[i]-angulacao[i-1])
    print("Variação Angular:", va)

    print("Angulos arredondados:", np.round(angulacao))


def calculo(sensor):
    angs = [0]
    for linha in sensor:
        angs.append(angulacao(angs[-1],linha))
    angs = np.array(angs)
    return angs

sensores1,sensores2 = np.array(limpa())
sensores1 = np.reshape(sensores1,(int(len(sensores1)/6),6))
sensores2 = np.reshape(sensores2,(int(len(sensores2)/6),6))

impares = calculo(sensores1)
pares = calculo(sensores2)
contas (impares)

       





