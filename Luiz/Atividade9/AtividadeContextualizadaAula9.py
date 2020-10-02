# Vetor Angulo é o vetor produzido na atividade 8
# Ele tem um formanto de array ([0.04. 0.043. ..., 0.5])

import math

lista = list


def lerDadosEsp(filePath='C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv'):
    lista = []
    with open(filePath, 'r') as fileObject:
        for line in fileObject:
            saidaFloat = list()
            dadosEsp = line.split('],"[')
            esp1 = dadosEsp[0].split('[')[1]
            esp1 = esp1.split('],')
            esp1 = esp1[0].split(',')
            for x in esp1:
                saidaFloat.append(float(x))
            lista.append(saidaFloat)
    return lista

M = 0.98
dt = 0.05

lista = lerDadosEsp('coletaFlexJoelho.csv')
lista = lerDadosEsp()
ang = list()
for linha in lista:
    dadoa = (linha[0]/(linha[1]**2 + linha[2]**2)**0.5)*180/math.pi
    dadow = linha[4]
    ang.append(M * (linha[5] + dadow*dt) + (1 - M)*dadoa)
for a in ang:
    print(a)
print(math.pi)

with open('anguloProcessado.txt', 'w') as arquivo:
	for valor in ang:
	    arquivo.write('Angulo Processado: ')
	    arquivo.write(str(valor)+'\n')

with open('anguloProcessado.csv', 'w') as arquivo:
	for valor in ang:
	    arquivo.write('Angulo Processado: ')
	    arquivo.write(str(valor)+'\n')

import numpy as np

#somatório
np.sum(vetor_angulo)

#média
np.mean(vetor_angulo)

#menor ângulo
np.min(vetor_angulo)

#maior Ângulo
np.max(vetor_agulo)

#Integral ou soma acumulada
np.cumsum(vetor_angulo)

#Diferença da médica e cada valor...
#Calcular para cada balor de 
vetor_angulo (valor - media(vetor_angulo))/n

#Variação Angular
np.diff(vetor_angulo)

#Valores arredondados
np.round(vetor_angulo)