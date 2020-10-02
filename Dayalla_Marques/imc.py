import math


def funcIMC(x,y,z):
    
  return x, y, z
peso = float(input('Digite seu peso: \n'))
altura = float(input('Agora digite sua altura: \n'))
imc = peso/(altura**2)
if imc < 17: print('Você está muito abaixo do peso ideal')
if 17 <= imc < 18.5: print('Você está abaixo do peso deal')
if 18.5 <= imc < 25: print('Você está dentro do peso ideal')
if 25 <= imc < 30: print('Você está acima do peso ideal')
if imc > 30: print('Você está muito acima do peso ideal')
arquivo =  open('arq.txt','w') 
arquivo.write('Esse programa calcula o imc')
arquivo.close()
arquivo = open('arq.txt','r')
print(arquivo.read())







#print(funcIMC(peso, altura, imc), file=arquivotexto)


