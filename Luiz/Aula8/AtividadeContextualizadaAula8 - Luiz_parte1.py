

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


lista = lerDadosEsp()
for linha in lista:
    print(linha)

import math

dadoa = (lista[0]/(lista[1]*2 + lista[2]*2)*0.5)*180/math.pi
M = 0.98
dt = 0.05
dadow = lista[4]
ang = M * (lista[5] + dadow*dt) + (1 - M)*dadoa
