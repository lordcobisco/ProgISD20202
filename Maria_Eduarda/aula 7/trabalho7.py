"""class LED:
    def __init__ (self,initRed,initGreen,initBlue):
        self.red=initRed
        self.green=initGreen
        self.blue=initBlue
    def __repr__ (self):
         return str(self.__dict__)
def listaIntensidadeLed (num):
     LEDs=[]
     for i in range (0,num,1):
         red=float(input("Intensidade da luz vermelho"))  
         green=float(input("Intensidade da luz verde"))    
         blue=float(input("Intensidade de luz azul"))       
         LEDs.insert(0,LED(red,green,blue))
    
     return str(LEDs)
        
 #LEDs.__repr__

lista=listaIntensidadeLed(2)

print(lista)"""

import time,sys
from datetime import datetime

num_Experimentos=int(input("Informe o número de experimentos que estará sendo feito: "))
dispositivos=int(input("Informe o número de dispositivos: "))
tempo_da_sessão=int(input("Digite o tempo de da sessão em minutos: "))
tempo_Led=int(input("Informe o tempo que as leds devem ficar ligadas"))
delay=int(input("Informe o tempo do intervalo que a led será desligada"))
now = datetime.now()
x=now.minute+tempo_da_sessão
y=now.minute
print(y,x)
while (y!=x):
     for i in range(0, tempo_Led):
         sys.stdout.write("\r Ligada{}".format(i))
         sys.stdout.flush()
         time.sleep(1)
     for j in range(0,delay):
         sys.stdout.write("\rDesligada{}".format(j))
         sys.stdout.flush()
         time.sleep(1)
     y=now.minute