from threading import Thread
import time
import random

class Dispositivo:
    def __init__(self,duracao,tempo, intensR, intensG, intensB, tensao):
        self.duracao = duracao
        self.tempo = tempo
        self.intensR = intensR
        self.intensG = intensG
        self.intensB = intensB
        self.tensao = tensao

    def Luzes(self, disp):
        end_time = time.time() + self.duracao
        luz= ["vermelha", "verde", "azul"]
        while time.time() < end_time:
            print(disp, "-------Luz ", luz[random.randint(0,2)], " acesa\n")
            time.sleep(self.tempo)
print('*******AVISO!**********')      
print("Em caso de emergencia, clique ctrl+c para parar o experimento!")

duracao= float(input("Qual a duração do experimento? "))
tempo= float(input("Qual o tempo que a luz permanece ligada? "))
intensity_r= float(input(" Qual a itensidade da luz vermelha? "))
intensity_g= float(input(" Qual a itensidade da luz verde? "))
intensity_b= float(input(" Qual a itensidade da luz azul? "))
tensaoeletrodo = []
for i in range(1):
    tensaoeletrodo.append(float(input("Qual a amplitude de tensão da matriz de 34 eletrodos? ")))

parametros= Dispositivo(duracao, tempo, intensity_r, intensity_g, intensity_b, tensaoeletrodo)

dispositivo1 = Thread(target=parametros.Luzes,args=["dispositivo 1"])
dispositivo2 = Thread(target=parametros.Luzes,args=["dispositivo 2"])

dispositivo1.start()
dispositivo2.start()



