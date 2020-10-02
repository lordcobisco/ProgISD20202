from threading import Thread
import time
import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np

print('Atividade Contextualizada 10')

class semEstimulo:
    def __init__ (self, ledBSE, tempoSE, qtdSE, sesaoSE, diaSE):
        self.tempoSE = tempoSE
        self.qtdSE = qtdSE
        self.sessaoSE = sessaoSE
        self.diaSE = diaSE

class prolongEstimulo:
    def __init__ (self, ledBPE, tempoPE, qtdPE, sessaoPE, diaPE):
        self.ledBPE = ledBPE
        self.tempoPE = tempoPE
        self.qtdPE = qtdPE
        self.sessaoPE = sessaoPE
        self.diaSE = diaSE

class delayedEstimulo:
    def __init__ (self, ledBDE, tempoDE, qtdDE, sessaoDE, diaDE):
        self.ledBDE = ledBDE
        self.tempoDE = tempoDE
        self.qtdDE = qtdDE
        self.sessaoDE = sessaoDE
        self.diaSE = diaSE

def sEstimulo(qtdSE, diaSE, sessaoSE, tempoSE, recSE):
    with open('dadossEstimulo.txt', 'w') as fileObject:
        fileObject.write("Dados sem estimulo. \n")
        fileObject.write("Quantidade de animais \n")
        fileObject.write(str(qtdSE))
        fileObject.write("\n")
        fileObject.write("Numero de dias de teste \n")
        fileObject.write(str(diaSE))
        fileObject.write("\n")
        fileObject.write("Numero de sessoes feitas \n")
        fileObject.write(str(sessaoSE))
        fileObject.write("\n")
        fileObject.write("Tempo de cada sessao feita \n")
        fileObject.write(str(tempoSE))
        fileObject.write("\n")
        fileObject.write("Recompensas: \n")
        fileObject.write(str(recSE))

def pEstimulo(qtdPE, diaPE, sessaoPE, tempoPE, ledBPE, recPE):
    with open('dadospEstimulo.txt', 'w') as fileObject:
        fileObject.write("Dados com estimulo prolongado. \n")
        fileObject.write("Quantidade de animais: \n")
        fileObject.write(str(qtdPE))
        fileObject.write("\n")
        fileObject.write("Numero de dias de teste: \n")
        fileObject.write(str(diaPE))
        fileObject.write("\n")
        fileObject.write("Numero de sessoes feitas: \n")
        fileObject.write(str(sessaoPE))
        fileObject.write("\n")
        fileObject.write("Tempo de cada sessao feita: \n")
        fileObject.write(str(tempoPE))
        fileObject.write("\n")
        fileObject.write("Intensidade do LED azul: \n")
        fileObject.write(str(ledBPE))
        fileObject.write("\n")
        fileObject.write("Recompensas: \n")
        fileObject.write(str(recPE))

def dEstimulo(qtdDE, diaDE, sessaoDE, tempoDE, ledBDE, delayDE, recDE):
    with open('dadosdEstimulo.txt', 'w') as fileObject:
        fileObject.write("Dados com estimulo atrasado. \n")
        fileObject.write("Quantidade de animais: \n")
        fileObject.write(str(qtdDE))
        fileObject.write("\n")
        fileObject.write("Numero de dias de teste: \n")
        fileObject.write(str(diaDE))
        fileObject.write("\n")
        fileObject.write("Numero de sessoes feitas: \n")
        fileObject.write(str(sessaoDE))
        fileObject.write("\n")
        fileObject.write("Tempo de cada sessao feita: \n")
        fileObject.write(str(tempoDE))
        fileObject.write("\n")
        fileObject.write("Intensidade do LED azul: \n")
        fileObject.write(str(ledBDE))
        fileObject.write("\n")
        fileObject.write("Tempo de atraso: \n")
        fileObject.write(str(delayDE))
        fileObject.write("\n")
        fileObject.write("Recompensas: \n")
        fileObject.write(str(recDE))

def OutboundSE(BEO,BDO,comp,recSE):
    print('Teste Outbound.')
    if(comp == BDO):
        print('Recompensa liberada.')
        recSE = recSE + 1
    elif(comp == BEO):
        print('Recompensa liberada.')
        recSE = recSE + 1
    else:
        print('Recompensa negada.')
    SE.append(recSE)    
    return recSE

def OutboundPE(BEO,BDO,comp,recPE): 
        print('Teste Outbound.')
        if(comp == BDO):
            print('Recompensa liberada.')
            recPE = recPE + 1
        elif(comp == BEO):
            print('Recompensa liberada.')
            recPE = recPE + 1
        else:
            print('Recompensa negada.')
        PE.append(recPE)
        return recPE

def OutboundDE(BEO,BDO,comp,recDE):
        print('Teste Outbound.')
        if(comp == BDO):
            print('Recompensa liberada.')
            recDE = recDE + 1
        elif(comp == BEO):
            print('Recompensa liberada.')
            recDE = recDE + 1
        else:
            print('Recompensa negada.')
        DE.append(recDE)
        return recDE

def Inbound(BDI,BEI,compI,recI):
    if(compI == 1):
        print('Recompensa liberada.')
    else:
        print('Recompensa negada.')


print('ETAPA SEM ESTÍMULO')
qtdSE = int(input("Quantos animais farão parte da etapa sem estímulo? "))
diaSE = int(input('Em quantos dias será feito o teste? '))
sessaoSE = int(input('Em quantas sessões serão feitas por dia? '))
tempoSE = int(input("Em quanto tempo cada sessão? "))

print('ETAPA COM ESTÍMULO PROLONGADO')
ondPE = int(input("Ondulação aconteceu? "))
if(ondPE == 1):
    qtdPE = int(input("Quantos animais farão parte da etapa com estímulo prolongado? "))
    diaPE = int(input('Em quantos dias será feito o teste? '))
    sessaoPE = int(input('Em quantas sessões serão feitas por dia? '))
    tempoPE = int(input("Em quanto tempo cada sessão? "))
    ledBPE = int(input('Qual a intensidade do LED azul? (em %) '))
    print('LED ON ', ledBPE, '%')

print('ETAPA COM ATRASO DE ESTÍMULO')
ondDE = int(input("Ondulação aconteceu? "))
if(ondDE == 1):
    qtdDE = int(input("Quantos animais farão parte da etapa com atraso de estímulo? "))
    diaDE = int(input('Em quantos dias será feito o teste? '))
    sessaoDE = int(input('Em quantas sessões serão feitas por dia? '))
    tempoDE = int(input("Em quanto tempo cada sessão? "))
    ledBDE = int(input('Qual a intensidade do LED azul? (em %) '))
    delayDE = randint(400,1000)
    delay = delayDE*0.001
    time.sleep(delay)
    print('LED ON ', ledBPE, '%')
    

recSE = 0
recPE = 0
recDE = 0
BEO = 0
BDO = 1
SE = []
PE = []
DE = []

for i in range(qtdSE):
    for j in range(sessaoSE):
        print('Rato', i, 'sessão', j, 'SEM ESTIMULO')
        comp = int(input('Entre com o braço do labirinto no qual o rato se dirigiu. (0 para esquerdo e 1 para direito) '))
        OutboundSE(BEO,BDO,comp,recSE)

for i in range(qtdPE):
    for j in range(sessaoPE):
        print('Rato', i, 'sessão', j, 'ESTIMULO PROLONGADO')
        comp = int(input('Entre com o braço do labirinto no qual o rato se dirigiu. (0 para esquerdo e 1 para direito) '))
        OutboundPE(BEO,BDO,comp,recPE)

for i in range(qtdDE):
    for j in range(sessaoDE):
        print('Rato', i, 'sessão', j, 'ATRASO DE ESTIMULO')
        comp = int(input('Entre com o braço do labirinto no qual o rato se dirigiu. (0 para esquerdo e 1 para direito) '))
        OutboundDE(BEO,BDO,comp,recDE)

somaSE = (sum(SE))
somaPE = (sum(PE))
somaDE = (sum(DE))

s = (range(diaSE))

plt.plot(s,SE) 
plt.plot(s,PE)
plt.axis([0, 10, 0, 2])
plt.title("Sem estímulo x Estímulo prolongado")
plt.grid(True)
plt.xlabel("Dias")
plt.ylabel("Recompensas")
plt.show()

plt.plot(s,DE)
plt.plot(s,SE)
plt.axis([0, 10, 0, 2])
plt.title("Sem estímulo x Estímulo com atraso")
plt.grid(True)
plt.xlabel("Dias")
plt.ylabel("Recompensas")
plt.show()


sEstimulo(qtdSE,diaSE,sessaoSE,tempoSE, somaSE)
pEstimulo(qtdPE,diaPE,sessaoPE,tempoPE,ledBPE, somaPE)
dEstimulo(qtdDE,diaDE,sessaoDE,tempoDE, ledBDE, delay, somaDE)
