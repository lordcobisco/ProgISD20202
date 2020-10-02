class dispositivos:
	def eletrodo (canais, RGB):
		"""Essa Função das listas dos canais do eletrodo e as variaveis do led RGB"""
		def dispositivo2():
			"""Esse dispositivo é acionado para gravar o experimento"""

camera = ['Ajuste do Foco','Iniciar video','Aumentar o zoom','Parar Video']
programaDeFilmagem = ['Cortar video','Melhorar qualidade do video','Tranformar o video em gif']
   

canais = ['Canal1', 'Canal2', 'Canal3', 'Canal4', 'Canal5', 'Canal6', 'Canal7','Canal8','Canal9', 'Canal10','Canal11,','Canal12','Canal13','Canal14','Canal15','Canal16','Canal17','Canal18','Canal19','Canal20','Canal21','Canal22','Canal23','Canal24','Canal25','Canal26','Canal27','Canal28','Canal29','Canal30','Canal31','Canal32']; RGB = ['Red', 'Green', 'Blue']
print(canais)
print(RGB)

print(input('Qual canal deseja utilizar?'))


print(camera)
print(programaDeFilmagem)
print(int(input('Deseja começar a filmagem? (Se não aperte 0 se se sim aperte1)')))





from datetime import datetime, timedelta
from sys import stdout
from time import sleep
 
print(''' Cronometro regressivo | programador => mmxm ''')
segundos = int(input('Digite a quantidade de segundos o led Red ficará acionado no canal selecionado: '))
tempo = timedelta(seconds=segundos)

print('\n')
 
while (str(tempo) != '0:00:00'):
	stdout.write("\r%s"%tempo)
	stdout.flush()
	tempo = tempo - timedelta(seconds=1)
	sleep(1)
 
stdout.write("\r0:00:00")
stdout.flush()
 
print ('\a')

if(tempo<=20):
	print('Continua o experimento')
	if(not tempo<=20):
		print('O experimento foi interrompido') 

from datetime import datetime, timedelta
from sys import stdout
from time import sleep
 
print(''' Cronometro regressivo | programador => mmxm ''')
segundos = int(input('Digite a quantidade de segundos o led Green ficará acionado no canal selecionado: '))
tempo = timedelta(seconds=segundos)

print('\n')
 
while (str(tempo) != '0:00:00'):
	stdout.write("\r%s"%tempo)
	stdout.flush()
	tempo = tempo - timedelta(seconds=1)
	sleep(1)
 
stdout.write("\r0:00:00")
stdout.flush()
 
print ('\a')

if(tempo<=20):
	print('Continua o experimento')
	if(not tempo<=20):
		print('O experimento foi interrompido') 

from datetime import datetime, timedelta
from sys import stdout
from time import sleep
 
print(''' Cronometro regressivo | programador => mmxm ''')
segundos = int(input('Digite a quantidade de segundos o led Blue ficará acionado no canal selecionado: '))
tempo = timedelta(seconds=segundos)

print('\n')
 
while (str(tempo) != '0:00:00'):
	stdout.write("\r%s"%tempo)
	stdout.flush()
	tempo = tempo - timedelta(seconds=1)
	sleep(1)
 
stdout.write("\r0:00:00")
stdout.flush()
 
print ('\a')

if(tempo<=20):
	print('Continua o experimento')
	if(not tempo<=20):
		print('O experimento foi interrompido') 
