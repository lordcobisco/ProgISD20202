import time
import sys

inicio = time.time()

class dispositivos:

    def __init__():
        eletrodos = [1,2,3,4,5,6,7,8,9,10]

def coleta_luzes():
    canal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #Criando 32 canais
    quantidade_canal = int(input("Informe quantos canais serão utilizados ")) 
    for i in range (0, quantidade_canal,  1):
            
        R = int(input("Digite a intensidade de vermelho entre 0 e 255 para o canal "))
        G = int(input("Digite a intensidade de verde entre 0 e 255 para o canal "))
        B = int(input("Digite a intensidade de azul entre 0 e 255 para o canal "))

    canal[i] = [R,G,B]


def coleta_eletrodos():

    n = int(input("Digite a quantidade de eletrodos que será utilizada. Número máximo: 10  "))

    for i in range(0,n,10):
        print("Digite os dados do eletrodo ", i+1) #normalizando o índice para nao confundir o usuário
        coleta_luzes()
        agora = time.time() - inicio
        print("Tempo de digitacao: ", agora)    

coleta_eletrodos()


