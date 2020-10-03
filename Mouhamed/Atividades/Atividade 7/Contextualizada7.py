#led rgb tem 4 canais. Tem 3 cores (vermelho, verde e azul). Cada "perna" corresponde a uma cor (tensão) e o terminal maior é o negativo
#perna esquerda para direita, cor vemelha, verde e azul. Controlar a intensidade com potenciometro por exemplp, pode alterar cores. 
#Eletrodo de 32 canais - cada um tem um RGB

#luz azul - ativação. Luz amarela inibição 

class Pesquisadores:

    def boas_vindas():
        return ('Bem vindo ao experimento de optogênese.')

    def Nome(x):
        n = int(x)
        if n ==1:
            return ('Pesquisador: Maria')
        elif n==2:
            return('Pesquisador: Jose')
        else:
            return('Pesquisador não cadastrado')

from Contextualizada7 import Pesquisadores
import time
import sys
id = int(input(" Digite o seu numero de identificação "))
print(Pesquisadores.boas_vindas())
print(Pesquisadores.Nome(id))

comando = input(" Deseja iniciar? s ou n ")
t1 = time.time()

if comando == "s":
    cores_led = (('vermelha', 5),('verde', 3.5), ( 'azul', 3.3 ))
    canais = []
    canal_desejado = int(input('Qual o canal a ser usado? (Digite de 1 a 32) '))

    for i in range (1,33):
        var = ('Canal:' , i)
        canais.insert(i, var)

    def led_aceso(tensao):

        tensao = float(tensao)

        if (tensao == 5):
            cor = cores_led[0][0]
        elif (tensao == 3.5):
            cor = cores_led[1][0]
        else:
            cor = cores_led[2][0]
        return cor

    trabalho = input('Ligar canal? s ou n ' )

    while(trabalho =='s'):
        for i in range (0,33):
            if(i==canal_desejado-1):
                tensao = input('Qual a tensão que está passando no canal?  (3.3 , 3.5 ou 5) ' )

                cor_led = led_aceso(tensao)
                print(" O led aceso do", canais[i], "é: ", cor_led)

        stop = input('Deseja parar o experimento? s ou n ' )
        if stop== 's':
            break
        trabalho = input("Deseja ligar outro canal? s ou n "  )
    
tempo_execucao = time.time() - t1
print("Tempo de execução: ", tempo_execucao)




