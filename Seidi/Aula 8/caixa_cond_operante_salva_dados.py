# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:06:03 2020

@author: seidi
"""
from numpy.random import seed
from numpy.random import randint

# usei time para pausa
import time

import csv
formatos = ['csv', 'txt']

# seed random number generator
seed(101)

cont_tocou = 0

def detecta_aproximacao(tempo_restante, count_tocou):
  # Animal se aproximou após um período de tempo (aleatório)
  tempo_passado = randint(0, 101)/100    # gera um número aleatório entre 0 e 1 com resolução de 0.01
  time.sleep(tempo_passado)
  tempo_restante = tempo_restante - tempo_passado # desconta do tempo do experimento
  
  print('-'*100)
  print('Animal de aproximou. Liberada recompensa')
  
  # emissão de som
  som_emitido = randint(0,2)
  if(som_emitido == 0):
    print('\nFoi emitido o som phee (barra esquerda)')
  elif(som_emitido == 1):
    print('\nFoi emitido o som trill (barra direita)')
  
  # toque da barra
  animal_tocou = randint(0,limite_acerto)    # limite depende de o animal estar habituado ou não
  if(animal_tocou >= 1):
    count_tocou = count_tocou + 1
    lado_barra = randint(0,2)
    
    # acerto de barra pelo som emitido
    if(som_emitido == lado_barra):
      print('\nAnimal tocou a barra correta. Liberada recompensa')
    else:
      print('\nAnimal tocou a barra errada')
  else:
    
    lado_barra = float('nan')
    print('\nAnimal não tocou na barra')
      
  print('   Restam ', tempo_restante, ' minutos para o fim do treino')
  print('   Animal tocou', count_tocou, 'vezes na barra')
  
  if(count_tocou >= 20):  # animal acumulou 20 toques corretos
    print('O TREINO PASSOU PARA A PRÓXIMA ETAPA')
  if(count_tocou >= 50 and tempo_restante >= 0): # animal acumulou 50 toques corretos
    print('O TREINO PASSOU PARA A PRÓXIMA FASE')
  print('')
  return som_emitido, lado_barra, tempo_restante, count_tocou
  

# Requisito 1: Habituação
# i. se o animal está habituado, registrar em uma variável
# o animal estar habituado aumenta as chances de acerto
# animal não habituado: é esperado que acerte entre 20 a 50 vezes antes do termpo terminar
# animal habituado: é esperado que acerte 50 vezes antes do termpo terminar
animal_habituado = int(input('O animal já está habituado? (NÃO 0| SIM 1): '))

if(animal_habituado): 
  limite_acerto = 20  # maior chance de acerto
  print('Animal já está habituado mas seguirá com treino para registro dos dados')
else:
  limite_acerto = 2   # menor chance de acerto
  
cont_formatos = 1
for formato in formatos:
  print(cont_formatos, '-', formato)
  cont_formatos += 1
save_to = int(input('Digite o formato para salvar os dados:')) - 1

# Requisito 2: Regime de aproximações sucessivas
# i. iniciar a variável com 30min
tempo_restante = 30

# ii. se a variável de aproximação diminuiu (animal aproximou), liberar 
#0.5ml de rec
# iii.    se o animal tocou na barra 20x, retornar que o experimento
#passou para a próxima etapa
# iv.     se o som1 foi emitido e o animal tocou na barra esquerda, liberar
#0.5ml de rec
# v.      caso contrário, não liberar nada
# vi.     se o som2 foi emitido e o animal tocou na barra direita, liberar 0.5ml de rec
# vii.    caso contrário, não liberar nada
# viii.   se o experimento foi realizado 50x em 30min apresentr que o experimento
#seguirpa para a próxima fase

if(save_to == 0):
  with open('dados_cond_operante.csv','w',newline = '') as csvfile:
    while tempo_restante > 0:      
      csv_writer = csv.writer(csvfile, delimiter = ',')
      
      som_emitido, lado_barra, tempo_restante, cont_tocou = \
      detecta_aproximacao(tempo_restante, cont_tocou)
          
      csv_writer.writerow([str(som_emitido), str(lado_barra), str(tempo_restante), str(cont_tocou)])
elif(save_to == 1):  
  with open('dados_cond_operante.txt','w',newline = '') as txtfile:
    while tempo_restante > 0:      
      
      som_emitido, lado_barra, tempo_restante, cont_tocou = \
      detecta_aproximacao(tempo_restante, cont_tocou)
          
      txtfile.write(str(som_emitido) + ',' + str(lado_barra) + ',' + \
                    str(tempo_restante) + ',' + str(cont_tocou) + '\n')

  
print('-'*100)
print('O TEMPO LIMITE JÁ FOI ULTRAPASSADO')