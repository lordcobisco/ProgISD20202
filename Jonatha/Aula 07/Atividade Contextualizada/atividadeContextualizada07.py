from os import system
import math
import time
system('clear')

# Variáveis
Dispositivos = dict()


class Dispositivo:
    def __init__(self):
        self.ligado = False
        self.azul = 0.0
        self.verde = 0.0
        self.vermelho = 0.0

    def ledRGB(self, eletrodos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ligado=False):
        self.azul = sum(eletrodos[:10])
        self.verde = sum(eletrodos[10:20])
        self.vermelho = sum(eletrodos[20:])
        return self.azul, self.verde, self.vermelho

    def liga(self):
        self.ligado = True
        return 'Dispositivo ligado: ' + str(self.ligado)

    def desliga(self):
        self.ligado = False
        return 'Dispositivo ligado: ' + str(self.ligado)


#tempoLimite = float(input('Informe o tempo do experimento: '))
tempoLimite = 2
numDispositivos = int(
    input('Informe quantos dispositivos terão no experimento: '))

for i in range(Dispositivos):
    tag = 'dispositivo' + str(i+1)
    dictDispositivos[tag] = Dispositivo()
    x = input('Informe quantas vezes o dispositivo ' + str(i+1) +
              'irá acender durante o tempo do experimento: ')
    print('Entendi. O dispositivo'+str(i+1)'acenderá '+str(x)+'x.')
    print('Por favor, informe os segundos, de 0 a' +
          str(tempoLimite)+' que o led ')
    for i in range(x):
