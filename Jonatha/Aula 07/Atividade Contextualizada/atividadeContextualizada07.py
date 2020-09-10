from os import system
import math
import time
import keyboard
from Auxiliar import Dispositivo
from Auxiliar import Eletrodos
from Auxiliar import Experimento

system('clear')
experimento = list()

numExperimentos = int(input('Informe o número de experimentos: '))
for i in range(numExperimentos):
    print('\nEXPERIMENTO ',i+1)
    experimento.append(Experimento())

tempo = 0
divisor = 1000
print('INICIANDO EXECUÇÃO DO EXPERIMENTO')
while(True):
    print('Tempo de Experimento: ',tempo,' segundos.')
    experimento[0].execucao(tempo)
    tempo+=1

    for i in range(divisor):
        time.sleep(1/divisor)
        if(keyboard.is_pressed('a')):
            print('Saindo do programa!')
            break
