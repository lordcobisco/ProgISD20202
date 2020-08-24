# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:58:23 2020

@author: seidi
"""

peso    = float(input("Digite seu peso (em kg): "))
altura  = float(input("Digite sua altura (em m): "))
imc     = peso/altura**2

print('valor do imc: ', imc)
print('muito abaixo do peso: ', imc <= 17)
print('abaixo do normal', imc > 17 and imc <= 18.5)
print('dentro do normal', imc > 18.5 and imc <= 25)
print('acime do normal', imc >25 and imc <= 30)
print('muito acima do normal', imc > 30)