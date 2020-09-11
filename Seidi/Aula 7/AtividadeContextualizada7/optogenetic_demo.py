# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:25:16 2020

@author: seidi
"""

from optogenetic import optogenetic_matrix as om
import optogenetic
import random
import time

def start_stimulation_sequence(matrix_list, list_inds, list_timing, end_time, emergency_time):
  """Função que recebe a estrutura de matrizes marix_list, executa a sequência 
  de ativação dos LEDs nos tempos definidos por list_timing e sequência de 
  matrizes definida por list_inds. Valor end_time indica o fim temporal da ativação
  e valor mergency_time simula um valor temporal em que ocorre interrupção de 
  emergência"""
  itime     = 0
  stop_now = False
  next_stim = list_timing[itime]
  
  
  initial_tic  = time.perf_counter() # começa a contar o tempo
  print('\nPróxima estimulação em', next_stim ,'s')
  
  while(True):
    tic = time.perf_counter() # tempo inicial da atual estimulação
    
    if(time.perf_counter() - initial_tic > emergency_time): # simulando parada de emergência
      stop_now = True
    
    if(stop_now): 
      print('Parada Acionada!')
      print('LEDs terão saída zeradas')
      for leds_matrix in matrix_list:
        leds_matrix.stop_leds()
      break
    elif(time.perf_counter() - initial_tic >= end_time):
      print('Fim da sequência de estimulação')
      break
    elif(time.perf_counter() - initial_tic >= next_stim):
      next_matrix_ind = list_inds[itime]
      print('Acionando matriz de LEDs', matrix_list[next_matrix_ind].get_name())
      R,G,B = matrix_list[next_matrix_ind].get_leds_sequence_value()
      matrix_list[next_matrix_ind].set_values_leds(R, G, B)
      matrix_list[next_matrix_ind].show_state()
      itime += 1
      if itime <= len(list_timing) - 1:
        next_stim = list_timing[itime]
        print('\nPróxima estimulação: ',next_stim ,'s')
      else:
        next_stim = end_time
        
    delta = time.perf_counter() - tic
    
    time.sleep(0.2 - delta) # o loop inteiro deve durar 0.2 sec
    
    
count_matrix = 0

# I. Criar estrutura de LEDs
print('_'*80)
print('Demo I - Criando estruturas de interação com matrizes de LEDs')
# instancia matrizes de leds com valor padronizado de número de leds 
leds_matrix_list = []

print('\nleds_matrix1')
leds_matrix_list.insert(count_matrix, om(name = 'leds_matrix1'))
count_matrix += 1

print('\nleds_matrix2')
leds_matrix_list.insert(count_matrix, om(name = 'leds_matrix2'))
count_matrix += 1

print('\nleds_matrix3')
leds_matrix_list.insert(count_matrix, om(name = 'leds_matrix3'))

print('\nAs próximas sessões introduzem operações sobre as estrutura leds_matrix')
pular_intro = int(input('Continuar para a introdução às operações da matriz de LEDs (NÃO 0 | SIM 1)?: '))

if pular_intro == 1:
  # II. Mostrar valor dos LEDs
  print('_'*80)
  print('Demo II - Mostrar valores atuais dos LEDs')
  # mostra na tela os valores iniciais
  dict_leds1 = leds_matrix_list[0].get_values_leds()
  print('\nValores da matriz',leds_matrix_list[0].get_name())
  print('Valores R:',dict_leds1['R'])
  print('Valores G:',dict_leds1['G'])
  print('Valores B:',dict_leds1['B'])
  
  # alternativa, usar função show_info()
  print('')
  leds_matrix_list[1].show_info()
  leds_matrix_list[2].show_info()
  
  input('\nTecle Enter para Continuar...')
  
  # III. Alterar valor dos LEDs
  print('_'*80)
  print('Demo III - Alterar valores dos LEDs')
  print('\nEscolhendo valores RGB randomicos para os LEDs')
  # alterando valor de leds de uma forma randomica
  nb_leds1 = leds_matrix_list[0].get_nb_leds()
  nb_bits = optogenetic.nb_bits
  
  randomlistR = random.sample(range(0, 2**nb_bits - 1), nb_leds1)
  randomlistG = random.sample(range(0, 2**nb_bits - 1), nb_leds1)
  randomlistB = random.sample(range(0, 2**nb_bits - 1), nb_leds1)
  leds_matrix_list[0].set_values_leds(randomlistR, randomlistG, randomlistB)
  leds_matrix_list[0].show_info()
  
  input('\nTecle Enter para Continuar...')
  
  # IV. Parar estimulação por LEDs
  print('_'*80)
  print('Demo IV - Desligar LEDs (parar estímulo)')
  
  leds_matrix_list[0].show_info()
  print('\nZerando os valores RGB dos LEDs...')
  leds_matrix_list[0].stop_leds()
  leds_matrix_list[0].show_info()
  
  input('\nTecle Enter para Continuar...')
  
  # V. Alterar apenas um LED
  print('_'*80)
  print('Demo V - Alterando o valor de apenas um LED')
  R = 123
  G = 0
  B = 123
  ind_led = 34 # índice não existente
  print('\nR: {}, G: {}, B: {}, ind_led: {}'.format(R,G,B,ind_led))
  print('Caso de erro: índice não existente')
  leds_matrix_list[0].set_values_single_led(ind_led, R, G, B)
  time.sleep(.5)
  
  print('')
  R = 264 # valor extrapolado
  G = 0
  B = 123
  ind_led = 20
  print('R: {}, G: {}, B: {}, ind_led: {}'.format(R,G,B,ind_led))
  print('Caso de erro: valor R ou G ou B extrapolado')
  leds_matrix_list[0].set_values_single_led(ind_led, R, G, B)
  time.sleep(.5)
  
  print('')
  R = 123
  G = 0
  B = 123
  ind_led = 20
  print('R: {}, G: {}, B: {}, ind_led: {}'.format(R,G,B,ind_led))
  print('Alteração válida')
  leds_matrix_list[0].set_values_single_led(ind_led, R, G, B)
  leds_matrix_list[0].show_info()
  time.sleep(.5)
  
  continuar_teste = 1
  while(continuar_teste):
    print('')
    print('Input do usuário - alteração de leds_matrix1')
    str_input = 'Digite o índice o led (0 a ' + str(leds_matrix_list[0].get_nb_leds() - 1) + ')' 
    ind_led = int(input(str_input))
    str_input = 'Digite o valor de R (0 a ' + str(2**nb_bits - 1) + ')' 
    R = int(input(str_input))
    str_input = 'Digite o valor de G (0 a ' + str(2**nb_bits - 1) + ')' 
    G = int(input(str_input))
    str_input = 'Digite o valor de B (0 a ' + str(2**nb_bits - 1) + ')' 
    B = int(input(str_input))
    leds_matrix_list[0].set_values_single_led(ind_led, R, G, B)
    leds_matrix_list[0].show_info()
    continuar_teste = int(input('Alterar mais LEDs (NÃO 0 | SIM 1)?: '))
  
  print('\nZerando os valores RGB dos LEDs...')
  time.sleep(.5)
  leds_matrix_list[0].stop_leds()
  leds_matrix_list[0].show_info()
  
  input('\nTecle Enter para Continuar...')

# VI. mostrar como a estrutura pode ser alterada ao longo do tempo
# =============================================================================
print('_'*80)
print('Demo VI - Ativando LEDs de forma temporizada')

print('\nUma sequência de LEDs será realizada')
print('A sequência temporal e os valores dos LEDs foi pré-determinada')

matrix_sequence = []

values_led = []

# A sequência seguinte poderia ser melhor representada em um arquivo externo 
#que é lido pelo programa
dict_led = {}
dict_led['R']       = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['B']       = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 1 # sec
dict_led['imatrix'] = 1 # índice dentre as matrizes existentes
matrix_sequence.append(dict_led)

dict_led = {}
dict_led['R']       = [101,0,0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [101,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,70,0,0,0,0,0,0,0,0,0,0,0]
dict_led['B']       = [101,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 2
dict_led['imatrix'] = 0
matrix_sequence.append(dict_led)

dict_led = {}
dict_led['R']       = [102,0,0,0,0,0,0,255,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [102,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['B']       = [102,0,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 4
dict_led['imatrix'] = 0
matrix_sequence.append(dict_led)

dict_led = {}
dict_led['R']       = [103,0,0,0,0,0,0,255,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [103,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['B']       = [103,0,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 6
dict_led['imatrix'] = 0
matrix_sequence.append(dict_led)

# simultaneo à matriz anterior
dict_led = {}
dict_led['R']       = [104,0,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,0,0,127,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [104,0,0,0,255,0,255,0,0,0,0,0,0,0,0,127,0,0,0,0,0,0,90,0,0,0,0,0,0,0,0,0]
dict_led['B']       = [104,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0,0,0,0,127,0,0,100,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 6
dict_led['imatrix'] = 2
matrix_sequence.append(dict_led)

dict_led = {}
dict_led['R']       = [105,0,0,0,0,0,0,255,0,0,0,60,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [105,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,100,0,0,0,0,0,0,0]
dict_led['B']       = [105,0,0,0,0,0,0,125,0,0,0,0,0,0,90,0,0,0,0,0,0,120,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 10
dict_led['imatrix'] = 0
matrix_sequence.append(dict_led)

dict_led = {}
dict_led['R']       = [106,0,0,0,0,0,0,255,0,0,0,60,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0]
dict_led['G']       = [106,0,0,0,0,0,255,0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,100,0,0,0,0,0,0,0]
dict_led['B']       = [106,0,0,0,0,0,0,125,0,0,0,0,0,0,90,0,0,0,0,0,0,120,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 12
dict_led['imatrix'] = 1
matrix_sequence.append(dict_led)

dict_led = {}
dict_led['R']       = [107,0,0,0,0,0,0,255,0,0,0,60,0,0,0,0,0,0,0,125,0,0,0,0,0,120,0,0,0,0,0,0]
dict_led['G']       = [107,0,0,0,0,0,125,0,0,0,100,20,0,0,0,0,0,80,0,0,0,0,0,0,100,0,0,0,0,0,0,0]
dict_led['B']       = [107,0,0,0,0,0,0,125,0,0,0,0,0,0,90,0,0,0,30,0,0,120,0,0,0,0,0,0,0,0,0,0]
dict_led['time']    = 15
dict_led['imatrix'] = 2
matrix_sequence.append(dict_led)
  
count_stim = 0
timing_values = []
matrix_id = []
for imatrix in matrix_sequence:
  leds_matrix_list[imatrix['imatrix']].add_timed_values(imatrix['R'], imatrix['G'], imatrix['B'])
  timing_values.append(imatrix['time'])
  matrix_id.append(imatrix['imatrix'])
  count_stim += 1

sim_emergeny_time = 14 # momento em que uma parada simulada é acionada
end_time          = 20 # duração total do experimento, em segundos
print('Sequência temporal (s):', timing_values)
print('Tempo final da sequência:',end_time, 's')
print('Parada de emergência acionada em:',sim_emergeny_time, 's')
print('Sequência de matrizes: ', matrix_id)
input('\nTecle Enter para Continuar...')

start_stimulation_sequence(leds_matrix_list, matrix_id, timing_values, end_time, sim_emergeny_time)

print('')
print('_'*80)
print('Estado final das matrizes de LEDs\n')
for matrix_leds in leds_matrix_list:
  matrix_leds.show_info()
  
input('\nTecle Enter para zerar valores...')
print('')
print('_'*80)
print('Zerando valores...\n')
for matrix_leds in leds_matrix_list:
  matrix_leds.stop_leds()
  matrix_leds.show_info()