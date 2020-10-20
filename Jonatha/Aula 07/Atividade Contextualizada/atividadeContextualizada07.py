from os import system
import math
import time
import keyboard
from biblioteca07 import Dispositivo
from biblioteca07 import Eletrodos
from biblioteca07 import Experimento

system('clear')
experimento = list()
experimentoInicio = list()
experimentoTempo = list()

numExperimentos = int(input('Informe o número de experimentos: '))
for i in range(numExperimentos):
    print('\nEXPERIMENTO ', i+1)
    experimento.append(Experimento())
    experimentoInicio.append(int(input('Informe o tempo de inicio que esse experimento irá começar: ')))
    experimentoTempo.append(0)

tempoGlobal = 0
divisor = 1000
print('INICIANDO EXECUÇÃO DO EXPERIMENTO.')
while(True):
    print('#'*70)
    print('\nTEMPO DESDE A GÊNESE: ', tempoGlobal, ' segundos.')
    print("Caso aconteça algo errado, pressione 'a' ou CTRL + 'z'.")
    for i in range(numExperimentos):
        if tempoGlobal >= experimentoInicio[i]:
            print('_'*50)
            print('EXPERIMENTO[',i+1,']:')
            experimento[i].execucao(experimentoTempo[i])
            experimentoTempo[i] += 1
    tempoGlobal += 1

    for i in range(divisor):
        time.sleep(1/divisor)
        if(keyboard.is_pressed('a')):
            print('Interrupção gerada. Saindo do programa...')
            break
