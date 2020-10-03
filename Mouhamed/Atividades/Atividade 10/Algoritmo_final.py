import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import pandas as pd

with open("fes_arduino.csv", "w") as saida:
    f = csv.writer(saida)
    f.writerow('Bem vindo a sessão de estimulação elétrica funcional - Neurobots')


class FES():  #Funcionalidades do FES

    def acionarFes():
        #rele = low  #abre o circuito no normalmente aberto
        return ('FES LIGADO') 
    
    def desligarFes():
        #rele = hight #circuito no comum
        return ("FES DESLIGADO")

from Algoritmo_final import FES #importando classe

print('Bem vindo a sessão de estimulação elétrica funcional - Neurobots')

ativacao = input("Deseja iniciar a sessão de estimulação elétrica funcional? s ou n ") #duas variaveis para nao usar a condição no gráfico abaixo
ativacao1 = ativacao #para usar no while

while(ativacao1 == "s"):
    controle = input("Pensar em iniciar movimento ou parar: ") #m - mover  p - parar - Imagética motora. Chega M
    if (controle == "m"):
        modo = FES.acionarFes() #chama a função, FES ligado. No caso, o relé foi ativo
        print(modo)
        
        time.sleep(1) # ajustado para receber a resposta do icm a cada segundo. 

    else:
        modo = FES.desligarFes() #relé desligado
        print(modo)
        time.sleep(1)
    
    ativacao1 = input("Deseja continuar a sessão de estimulação elétrica funcional? s ou n ")



tempo = []
corrente = []
tempo2 = []
corrente2 = []

filePath = 'teste.csv'
with open(filePath, 'r') as fileObject:
    for linhas in fileObject:
        valores1 = linhas.split(';') #pegando o ponto virgula
        tempo1 = valores1[0].split(';') #recebe tudo antes do ;
        corrente1 = valores1[1].split(';') #recebe tudo que tem depois do ;

        tempo.append(tempo1) #acrescenta os valores de tempo na lista
        corrente.append(corrente1) #acrescenta os valores de corrente na lista
       

        for linha in tempo1:
           tempo2.append(float(linha)) #manipulado e criado vetor de tempo - float

        for linha in corrente1:
          corrente2.append(float(linha)) #manipulado e criado vetor de corrente - float
    
if ativacao == 's': #condição para, caso não deseje iniciar o FES la em cima, nao plote o gráfico
    print("Relatório gráfico da sessão")
    
    #dados para plotar gráfico

    fig, ax = plt.subplots()
    ax.plot(tempo2,corrente2)
    plt.ylabel('Corrente (mA)')
    plt.xlabel('Tempo (s)')
    plt.title('Estimulação elétrica funcional - Dorsiflexão')
    plt.show()

