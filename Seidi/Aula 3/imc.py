# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:39:07 2020

@author: seidi
"""

peso    = 64 # em kg
altura  = 1.67 # em m
imc     = peso/altura**2

print('valor do imc: ', imc)
print('muito abaixo do peso: ', imc <= 17)
print('abaixo do normal', imc > 17 and imc <= 18.5)
print('dentro do normal', imc > 18.5 and imc <= 25)
print('acime do normal', imc >25 and imc <= 30)
print('muito acima do normal', imc > 30)