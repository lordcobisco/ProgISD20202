# Atividade Contextualizada 07

#Primeiramente vamos importar os módulos necessários

import time
import random

#Vamos criar uma classe para o Experimento, Eletrodo e Dispositivo. 


class Dispositivo:
    ''' Criação de um dispositivo que utilize RGB'''

    def __init__(self, entradaEletrodos, tempo):
        print('\nConfigurar Dipositivo:')
        self.entrada = entradaEletrodos.dados
        self.ledRGB = dict()
        self.ledRGB['R'] = self.configRGB('Vermelho', tempo)
        self.ledRGB['G'] = self.configRGB('Verde', tempo)
        self.ledRGB['B'] = self.configRGB('Azul', tempo)
        print('Dipositivo foi criado e os eletrodos conectados ao dispositivo.')

    def configRGB(self, cor,tempoExperimento):
        tempoExperimento = int(tempoExperimento)
        saida = list()
        saida = [0.0]*tempoExperimento
        num = int(input('\nInforme o número vezes o RGB('+ str(cor)+ ')irá acender: '))
        for i in range(num):
            tempoInicial = int(input('\nQuando o experimento for iniciado, informe com quantos segundos o RGB('+ str(cor) +') irá acender ['+str(i+1)+' de '+str(num)+']: '))
            duracao = int(input('Informe quantos segundos o RGB('+ str(cor) +') permanecerá aceso: '))
            tempoFinal = tempoInicial + duracao
            if tempoFinal > tempoExperimento: 
                tempoFinal = tempoExperimento
                w = float(input('De 0 a 1, informe a potência que o led irá acender nesse período: '))
            for i in range(tempoExperimento):
                if tempoInicial<=i<tempoFinal: saida[i] = w
            print('Saida PWM: ',saida)
        return saida

    def lerEletrodos(self, entradaEletrodos):
        self.entrada = entradaEletrodos.dados

class Eletrodos:
    '''Criação da classe para os eletrodos'''

    def __init__(self):
        self.num = int(input("Informe o número de eletrodos: "))
        self.num = 32 
        arquivo.open('DadosEletrodos.txt','w')
        arquivo.close()
        self.leitura()
    
    def leitura(self):
        lista = list()
        for j in range(self.num):
            lista.append(random.randint(0,255))
        self.dados = lista
        self.armazenaEmArquivo()
        print('\nA leitura dos eletrodos foi realizada.\n')
    def ArmazenarArquivo(self):
        arquivo = open('leituraEletrodos.txt', 'r')
        conteudo = arquivo.readlines()
        conteudo.append('\nLeitura: '+str(self.dados))
        arquivo = open('leituraEletrodos.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

class Experimento:
    '''Realizar o experimento'''

    def __init__(self):
        print('O experimento está sendo iniciado')
        self.eletrodos = Eletrodos()
        self.tempoLimite = float(input('Qual o tempo do experimento?:\n '))
        self.numDispositivos = int(input('Quantos dispositivos terá o experimento?\n '))
        self.listaDispositivos = self.criaDispositivos(self.tempoLimite)
    
    def dispositivosNosEletrodos(self):
        for dispositivo in self.listaDispositivos:
            dispositivo.lerEletrodos(self.eletrodos)
        return Dispositivo 

    def criandoDispositivos(self, tempo):
        lista = list()
        for i in range(self.numDispositivos):
            lista.append(Dispositivo(self.eletrodos, tempo))
        return lista  

    def realizarExperimento(self, passo):

        if(passo <= self.tempoLimite):
            i = 0
        for dispositivo in self.listaDispositivos:
            print('Dispositivo ',i+1)
            print('LedRGB(Vermelho):',dispositivo.ledRGB['R'][passo])
            print('LedRGB(Verde):', dispositivo.ledRGB['G'][passo])
            print('LedRGB(Azul):', dispositivo.ledRGB['B'][passo])
            i+= 1
        self.eletrodos.leitura()

experimento = list()
experimentoInicio = list()
experimentoTempo = list()

numExperimentos = int(input('Quantos experimentos serão realizados?\n '))
for i in range(numExperimentos):
    print('\nExperimento ', i+1)
    experimento.append(Experimento())
    experimentoInicio.append(int(input('Informe o tempo de inicio que esse experimento irá começar: ')))
    experimentoTempo.append(0)

tempoNoInicio = 0
valorini = 1000
print('Iniciando o experimento...')
while(True):
    print('#'*70)
    print('\nTempo desde a criação: ', tempoNoInicio, ' segundos.')
    print("Se desejar acabar o experimento, pressione 'z'.")
    for i in range(numExperimentos):
        if tempoNoInicio >= experimentoInicio[i]:
            print('_'*50)
            print('Experimento[',i+1,']:')
            experimento[i].execucao(experimentoTempo[i])
            experimentoTempo[i] += 1
    tempoNoInicio += 1

for i in range(valorini):
        time.sleep(1/valorini)
        if(keyboard.is_pressed('z')):
            print('Tecla de encerrar o programa pressionada e o programa será encerrado.')
            break