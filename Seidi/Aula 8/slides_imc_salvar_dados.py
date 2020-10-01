# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:10:37 2020

@author: seidi
"""

import csv
formatos = ['csv', 'txt']

def calcula_imc(peso, altura):
  return peso/altura**2

def mostar_situacao_imc(imc):
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
  
cont_formatos = 1
for formato in formatos:
  print(cont_formatos, '-', formato)
  cont_formatos += 1
save_to = int(input('Digite o formato para salvar os dados:')) - 1

peso    = float(input("Digite seu peso (em kg): "))
altura  = float(input("Digite sua altura (em m): "))
imc     = calcula_imc(peso, altura)

print('valor do imc: ', imc)
mostar_situacao_imc(imc)

if(save_to == 0):
  # salva os valores calculados em arquivo csv
  with open('imc_dados.csv','a',newline = '') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter = ',')
    csv_writer.writerow([str(peso), str(altura), str(imc)])
    
elif(save_to == 1):
  # salva os valores calculados em arquivo txt
  with open('imc_dados.txt','a',newline = '') as txtfile:
    txtfile.write(str(peso) + ',' + str(altura) + ',' + str(imc) + '\n')