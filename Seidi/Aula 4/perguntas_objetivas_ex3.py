# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:49:31 2020

@author: seidi
"""

performance_treino_1 = float(input('Qual a porcentagem de acertos do primeiro treino?'))
performance_treino_2 = float(input('Qual a porcentagem de acertos do segundo treino?'))
performance_treino_3 = float(input('Qual a porcentagem de acertos do terceiro treino?'))
performance_treino_4 = float(input('Qual a porcentagem de acertos do quarto treino?'))

media_performance = (performance_treino_1 + performance_treino_2 +\
  performance_treino_3 + performance_treino_4)/4

if(media_performance <= 60):
  print("Refaça a sessão de treino")
elif(media_performance > 60 and media_performance <= 75):
  print("Prossiga para o experimento, mas não espere uma performance boa")
else:
  print("A performance de treino é boa, continue com o experimento")
  
  
  
