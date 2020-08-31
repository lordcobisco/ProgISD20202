# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:10:37 2020

@author: seidi
"""

peso    = float(input("Digite seu peso (em kg): "))
altura  = float(input("Digite sua altura (em m): "))
imc     = peso/altura**2

print('valor do imc: ', imc)

if(imc <= 17):
  print('muito abaixo do peso (imc abaixo de 17)')
elif(imc > 17 and imc <= 18.5):
  print('abaixo do normal (imc entre 17 e 18.5)', )
elif(imc > 18.5 and imc <= 25):
  print('dentro do normal (imc entre 18.5 e 25)')
elif(imc >25 and imc <= 30):
  print('acima do normal (imc entre 25 e 30)')
elif(imc > 30):
  print('muito acima do normal (imc maior que 30)')