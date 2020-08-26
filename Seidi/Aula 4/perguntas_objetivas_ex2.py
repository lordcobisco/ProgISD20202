# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:53:27 2020

@author: seidi
"""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))

if(num1 <= 30 and num2 <= 30):
  print('a porta A está aberta e a porta B está fechada')
if(num1 > 30 and num2 <= 30):
  print('a porta A está fechada e a porta B está fechada')
if(num1 <= 30 and num2 > 30):
  print('a porta A está aberta e a porta B está aberta')
if(num1 > 30 and num2 > 30):
  print('a porta A está fechada e a porta B está aberta')
  

