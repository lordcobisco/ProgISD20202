import random
import math
import time

class Eletrodos:
  ''' Classe utilizada para gerar a entrada dos eletrodos da Atividade Contextualizada 07 '''

  def __init__(self):
    #self.num = int(input('Informe o número de eletrodos fixados: '))
    self.num = 32
    arquivo = open('leituraEletrodos.txt', 'w')
    arquivo.close()
    self.leitura()

  def leitura(self):
    lista = list()
    for j in range(self.num):
      lista.append(random.randint(0,255))
    self.dados = lista
    self.armazenaEmArquivo()
    print('\nLeitura dos eletrodos realizada.')

  def armazenaEmArquivo(self):
    arquivo = open('leituraEletrodos.txt', 'r')
    conteudo = arquivo.readlines()
    conteudo.append('\nLeitura: '+str(self.dados))
    arquivo = open('leituraEletrodos.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()


class Dispositivo:
  ''' Classe que criar um dispositivo utilizado na Atividade Contextualizada 07 '''

  def __init__(self, entradaEletrodos, tempo):
    print('\nConfigurando Dipositivo:')
    self.entrada = entradaEletrodos.dados
    self.ledRGB = dict()
    self.ledRGB['R'] = self.configRGB('Vermelho', tempo)
    self.ledRGB['G'] = self.configRGB('Verde', tempo)
    self.ledRGB['B'] = self.configRGB('Azul', tempo)
    print('Dipositivo criado e eletrodos conectados ao dispositivo.')

  def configRGB(self, cor,tempoExperimento):
    tempoExperimento = int(tempoExperimento)
    saida = list()
    saida = [0.0]*tempoExperimento
    num = int(input('\nInforme quantas vezes o RGB('+ str(cor)+ ')irá acender: '))
    for i in range(num):
      tempoInicial = int(input('\nApós iniciado o experimento, informe com quantos segundos o RGB('+ str(cor) +') irá acender ['+str(i+1)+' de '+str(num)+']: '))
      duracao = int(input('Informe quantos segundos o RGB('+ str(cor) +') irá permanecer aceso: '))
      tempoFinal = tempoInicial + duracao
      if tempoFinal > tempoExperimento: tempoFinal = tempoExperimento
      w = float(input('De 0 a 1, informe a potência que o led irá acender nesse período: '))
      for i in range(tempoExperimento):
        if tempoInicial<=i<tempoFinal: saida[i] = w
      print('Saida PWM: ',saida)
    return saida

  def lerEletrodos(self, entradaEletrodos):
    self.entrada = entradaEletrodos.dados


class Experimento:

  def __init__(self):
    print('Iniciando novo experimento...')
    self.eletrodos = Eletrodos()
    self.tempoLimite = float(input('Informe o tempo do experimento: '))
    #self.tempoLimite = 2
    self.numDispositivos = int(input('Informe quantos dispositivos terão no experimento: '))
    self.listaDispositivos = self.criaDispositivos(self.tempoLimite)

  def dispositivosLeemEletrodos(self):
    for dispositivo in self.listaDispositivos:
      dispositivo.lerEletrodos(self.eletrodos)
    #return dispositivos

  def criaDispositivos(self, tempo):
    lista = list()
    for i in range(self.numDispositivos):
      lista.append(Dispositivo(self.eletrodos, tempo))
    return lista

  def execucao(self, passo):

    if(passo > self.tempoLimite):
      print('Fim do experimento!')
      exit()

    i = 0
    for dispositivo in self.listaDispositivos:
      print('\nDISPOSITIVO ',i+1)
      print('ledRGB(Vermelho):',dispositivo.ledRGB['R'][passo])
      print('ledRGB(Verde):', dispositivo.ledRGB['G'][passo])
      print('ledRGB(Azul):', dispositivo.ledRGB['B'][passo])
      i+= 1
    self.eletrodos.leitura()
