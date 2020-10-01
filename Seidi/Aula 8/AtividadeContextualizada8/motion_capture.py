# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:15:59 2020

@author: seidi
"""
import csv
M = 0.98
dt = 0.05

def init_dict_dados():
  """Cria a estrutura vazia que receberá os dados"""
  dict_dados = []
  dict_dados.append([])
  dict_dados.append([])
  dict_dados[0] = {}
  dict_dados[0]['ax'] = []
  dict_dados[0]['ay'] = []
  dict_dados[0]['az'] = []
  dict_dados[0]['wx'] = []
  dict_dados[0]['wy'] = []
  dict_dados[0]['wz'] = []
  dict_dados[1] = {}
  dict_dados[1]['ax'] = []
  dict_dados[1]['ay'] = []
  dict_dados[1]['az'] = []
  dict_dados[1]['wx'] = []
  dict_dados[1]['wy'] = []
  dict_dados[1]['wz'] = []
  return dict_dados

def list_to_dict(dados_lista, dict_dados):
  """Passa a lista de dados por linha pra estrutura"""
  dict_dados[0]['ax'].append(dados_lista[0])
  dict_dados[0]['ay'].append(dados_lista[1])
  dict_dados[0]['az'].append(dados_lista[2])
  dict_dados[0]['wx'].append(dados_lista[3])
  dict_dados[0]['wy'].append(dados_lista[4])
  dict_dados[0]['wz'].append(dados_lista[5])
  
  dict_dados[1]['ax'].append(dados_lista[6])
  dict_dados[1]['ay'].append(dados_lista[7])
  dict_dados[1]['az'].append(dados_lista[8])
  dict_dados[1]['wx'].append(dados_lista[9])
  dict_dados[1]['wy'].append(dados_lista[10]) 
  dict_dados[1]['wz'].append(dados_lista[11]) 
  
  return dict_dados

def calcula_angulo(ang, dado_w, dado_a):
  """ aplica a formula ang = M*(ang + dado_w*dt) + (1-M)*(dado_a)"""
  return M*(ang + dado_w*dt) + (1-M)*(dado_a)

def append_ang(dict_dados, ind_sensor):
  """Para cada linha de dados do sensor, calcula o angulo e concatena na estrutura"""
  angulo_sensor = dict_dados[ind_sensor]['ay'][0]
  for idado in range(len(dict_dados[ind_sensor]['ay'])):
    angulo_sensor = calcula_angulo(angulo_sensor, dict_dados[ind_sensor]['wy'][idado], \
                                   dict_dados[ind_sensor]['ay'][idado])
    dict_dados[ind_sensor]['angy'].append(angulo_sensor)
  return dict_dados

# inicia a estrutura de dados
dict_dados = init_dict_dados()

# Lendo um arquivo csv
with open('coletaFlexJoelho.csv', 'r', newline='') as csvfile:
  dados_flex_joelho = csv.reader(csvfile, delimiter='"')
  start_line = True
  
  for row in dados_flex_joelho:
    
    # primeira linha é diferente das outras
    if start_line:
      print(row)
      ind1 = 1
      ind2 = 2
      sensor1 = row[ind1].split(',') # separa em elementos
      sensor2 = row[ind2].split(',')

      sensor1.remove(sensor1[-1])
      dados_sensor1 = [float(x.replace('"', '').replace('[', '').replace(']','')) for x in sensor1]
      dados_sensor2 = [float(x.replace('"', '').replace('[', '').replace(']','')) for x in sensor1]
      dados_sensor1.extend(dados_sensor2)
      dados_sensores = dados_sensor1
      start_line = False
      
    # restante das linhas. Se quiser testar o erro, é só apagar do if start_line até esse else
    else:
      dados_sensores = row[0]
      dados_sensores = dados_sensores.split(',') # separa em elementos
      
      # substitui aspas e colchetes por nada e transforma lista de strings em lista de floats
      dados_sensores = [float(x.replace('"', '').replace('[', '').replace(']','')) for x in dados_sensores]
    
    # Insere dados na estrutura
    dict_dados = list_to_dict(dados_sensores, dict_dados)


# Os dados são acessíveis através de dict_dados
# dict_dados[0] é o sensor 1
# dict_dados[1] é o sensor 2
# cada sensor possui dados 'ax', 'ay', 'az', 'wx', 'wy', 'wz'
# ou seja, acessa todos os dados de um eixo por exemplo fazendo dict_dados[0]['ay']

dict_dados[0]['angy'] = []
dict_dados[1]['angy'] = []

dict_dados = append_ang(dict_dados, 0)
dict_dados = append_ang(dict_dados, 1)
    
# salva os valores calculados em arquivo csv
with open('angulos_calculados.csv','w',newline = '') as csvfile:
  ang_writer = csv.writer(csvfile, delimiter = ',')
  for ang_sensor1, ang_sensor2 in zip(dict_dados[0]['angy'],dict_dados[1]['angy']):
    ang_writer.writerow([str(ang_sensor1), str(ang_sensor2)])
    
# salva os valores calculados em arquivo txt
with open('angulos_calculados.txt','w',newline = '') as txtfile:
  for ang_sensor1, ang_sensor2 in zip(dict_dados[0]['angy'],dict_dados[1]['angy']):
    txtfile.write(str(ang_sensor1) + ',' + str(ang_sensor2) + '\n')