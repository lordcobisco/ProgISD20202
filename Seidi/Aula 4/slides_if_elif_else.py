# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:23:19 2020

@author: seidi
"""
botao1Apertado = int(input('O rato apertou o botão 1?\n'))
botao2Apertado = int(input('O rato apertou o botão 2?\n'))

if(botao1Apertado and not botao2Apertado):
  print('Foram adicionados 10mg de comida')
elif(not botao1Apertado and botao2Apertado):
  print('Foram adicionados 20mg de comida')
elif(not botao1Apertado and not botao2Apertado):
  print('Nenhuma comida foi adicionada')
else:
  print('Foram adicionados 40mg de comida')
  
print('Fim de programa!')