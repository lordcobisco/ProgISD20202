import time, sys
#from datetime import date, datetime,timezone,timedelta
from datetime import datetime
from pytz import timezone
import pytz
#Cronometro 
"""for i in range(0, 10):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print ("\ncronometrou bb")

#Setando data atual
hoje=date.today()
print(hoje,"É DIA DE FESTA")
for i in range(0, 10):
    sys.stdout.write("\rFica na sua casa{}".format(i))
    sys.stdout.flush()
    time.sleep(1)
    
#Formatando a data
datatxt='0{}/0{}/{}'.format(hoje.day,hoje.month,hoje.year)
print("\nBufo querida:",datatxt)

datatxt=hoje.strftime('%d / %m / %Y')
print("Hoje é dia da maga do StarckOver flow:",datatxt)

#Pegando o tempo (Zoas o "tempo é um construto humano", História, Tyego professor (2016))
datime=datetime.now()
datatxt=datime.strftime('%d/%m/%Y %H:%M')
print ("Hora da aventura:",datatxt)

#Tranformando um string em datetime
datatxt='01/03/2018 12:30'
datime=datetime.strptime(datatxt,'%d/%m/%Y %H:%M')
print("Trava na beleza e segura essa transformação:",datime)

#Fuso horário
datime=datetime.now()
diferenca=timedelta(hours=-3)#(dias,segundos,microsegundos,minutis,horas,weeks)
print(diferenca)
fuso=timezone(diferenca)
print(fuso)

#Padronizar padrão SP
dataSp=datime.astimezone(fuso)
dataSpTXT=dataSp.strftime('%d/%m/%Y %H:%M')
print(dataSpTXT)"""


for tz in pytz.all_timezones:
    print(tz)

"""data_e_hora_atuais = datetime.now()
fuso_horario = timezone(‘America/Sao_Paulo’)
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(‘%d/%m/%Y %H:%M’)

print(data_e_hora_sao_paulo_em_texto)"""