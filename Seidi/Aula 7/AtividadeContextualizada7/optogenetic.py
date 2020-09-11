# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:14:50 2020

@author: seidi
"""

nb_bits = 8

class optogenetic_matrix():
  
  def __init__(self, nb_leds = 32, name  = ''):
    """Inicializa matriz de eletrodos"""
    self.name = name
    
    # começa desligado
    self.dict_leds = {}
    self.leds_sequence = {}
    self.dict_leds['R'] = [0]*nb_leds
    self.dict_leds['G'] = [0]*nb_leds
    self.dict_leds['B'] = [0]*nb_leds
    
    # variáveis de sequência de ativação
    self.leds_sequence['time'] = []
    self.leds_sequence['R'] = []
    self.leds_sequence['G'] = []
    self.leds_sequence['B'] = []
    
    self.nb_leds = nb_leds
    print('Matriz instanciada com', self.nb_leds, 'LEDs RGB')
    
  def show_info(self):
    """Mostra informação completa do estado da matriz de eletrodos"""
    print('Mostrando os valores da matriz', self.name)    
    print('Valores R:', self.dict_leds['R'])
    print('Valores G:', self.dict_leds['G'])
    print('Valores B:', self.dict_leds['B'])
    print('Número de LEDs:', self.nb_leds)
    print('')
    
  def show_state(self): 
    """Mostra apenas valor atual dos LEDs da mtriz"""
    print('Valores R:', self.dict_leds['R'])
    print('Valores G:', self.dict_leds['G'])
    print('Valores B:', self.dict_leds['B'])    

  # Getters
  def get_name(self):
    """Retorna o nome dado à matriz"""
    return self.name
  
  def get_values_leds(self):
    """Retorna o dicionário de estado dos LEDs"""
    return self.dict_leds
  
  def get_nb_leds(self):
    """Retorna o número de LEDs da matriz"""
    return self.nb_leds
  
  def get_timing_sequence_value(self):
    """Retorna o momento seguinte de ativação dos LEDs"""
    if self.leds_sequence['time']:
      return self.leds_sequence['time'].pop(0)
    else:
      return float('NaN')
    
  def get_leds_sequence_value(self):
    """Retorna o estado seguinte de ativação dos LEDs"""
    if self.leds_sequence['R']:
      return self.leds_sequence['R'].pop(0),self.leds_sequence['G'].pop(0),self.leds_sequence['B'].pop(0)
    else:
      return float('NaN')
  
  # Setters
  def set_name(self, name):
    """Altera o nome dado à matriz"""
    self.name = name
  
  def stop_leds(self):
    """Zera os valores RGB dos LEDs da matriz"""    
    # desliga todos os leds
    self.dict_leds['R'] = [0]*self.nb_leds
    self.dict_leds['G'] = [0]*self.nb_leds
    self.dict_leds['B'] = [0]*self.nb_leds
    
  def set_values_leds(self, R, G, B):
    """Substitui os valores RGB dos LEDs da matriz por R, G  e B"""
    self.dict_leds['R'] = R
    self.dict_leds['G'] = G
    self.dict_leds['B'] = B
    
  def add_timed_values(self, led_values_R,led_values_G,led_values_B):
    """Inclui novo estado RGB na sequência de ativação"""
    self.leds_sequence['R'].append(led_values_R)
    self.leds_sequence['G'].append(led_values_G)
    self.leds_sequence['B'].append(led_values_B)  
    
  def set_values_single_led(self, led_index, value_R, value_G, value_B):
    """Altera o valor RGB de apenas um LED"""
    if(led_index >= self.nb_leds):
      print('Índice de LED não utilizável')
      print('Use um índice de 0 a', self.nb_leds)
    elif(value_R > 2**nb_bits - 1 or value_G > 2**nb_bits - 1 or value_B > 2**nb_bits - 1 ):
      print('Algum dos valores de RGB está acima do possível')
      print('Use valores individuais de 0 a', 2**nb_bits)
      print('Nenhum valor será alterado')
    else:
      self.dict_leds['R'][led_index] = value_R
      self.dict_leds['G'][led_index] = value_G
      self.dict_leds['B'][led_index] = value_B


