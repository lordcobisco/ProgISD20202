# O Código a baixo gera a importação do dado de forma bruta, realizar ele me ajudou a compreender e realizar a atividade
# por isso quis colocar ele ai mas de uma forma não executavel.

import math

fileObject = open('C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv', 'r')
for line in fileObject:
	print(line)
fileObject.close()


def lerDadosEsp(filePath = 'C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv'):
    lista = []
    with open(filePath, 'r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],"[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                    print(float(dadosEsp1))
                    lista.append(float(dadosEsp1))
    return lista


lista = lerDadosEsp('C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv')
print(lista)


# Já nesse ponto o código foi "limpo" e por gerar muitos dados evitei de colocar novamente para executar



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

# Aqui já está de acordo como pede na atividade Conteztualizada 8
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