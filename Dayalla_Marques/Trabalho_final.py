# Esse programa gera dados de um roedor durante uma cirurgia

import pandas as biblio
import time
import random


def sensorRespiracao():
    min = 0
    max = 30
    x = random.randint(min, max)
    return x


def sensorTemperatura():
    min = 35
    max = 40
    x = random.uniform(min, max)
    return x


def sensorBatimentosCardiacos():
    min = 55
    max = 190
    x = random.randint(min, max)
    return x

dados = dict()
dados['temperatura'] = list()
dados['batimentos'] = list()
dados['respiracao'] = list()

num = int(input('Informe o número de leituras: '))
for i in range(num):
    dados['temperatura'].append(sensorTemperatura())
    dados['batimentos'].append(sensorBatimentosCardiacos())
    dados['respiracao'].append(sensorRespiracao())
    print('Temperatura: ', dados['temperatura'][i])
    print('Respiração: ', dados['respiracao'][i])
    print('Batimentos Cardíacos: ', dados['batimentos'][i])

data = biblio.DataFrame(dados)
data.to_csv('resultado.csv')

'''


sensorRespiracao = open('respir.txt', 'r')
for line in sensorRespiracao:
    print(line)
sensorRespiracao.close()

sensorBatimentosCardiacos = open('bati.txt', 'r')
for line in sensorBatimentosCardiacos:
    print(line)
sensorBatimentosCardiacos.close()

sensorTemperatura = open('temp.txt', 'r')
for line in sensorTemperatura:
    print(line)
sensorTemperatura.close()
'''
