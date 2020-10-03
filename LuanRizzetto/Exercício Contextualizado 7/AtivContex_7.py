#Atividade Contextualizada 7

import time,sys

print('Por favor, selecione o canal a ser configurado.')
canais = ['Canal1', 'Canal2', 'Canal3', 'Canal4', 'Canal5', 'Canal6', 'Canal7','Canal8','Canal9', 'Canal10','Canal11,','Canal12','Canal13','Canal14','Canal15','Canal16','Canal17','Canal18','Canal19','Canal20','Canal21','Canal22','Canal23','Canal24','Canal25','Canal26','Canal27','Canal28','Canal29','Canal30','Canal31','Canal32']
print(canais)
ch = int(input('Qual canal deseja configurar? '))
print('Canal',ch,'selecionado.')


def luzR():
    compOndaR = int(input("Insira o comprimento de onda (entre 625~740nm): ")) 
    potR = int(input("Insira a potência em mW: "))
    print("Parâmetros escolhidos:", compOndaR,"nm", potR,"mW")

def luzG():
    compOndaG = int(input("Insira o comprimento de onda (entre 500~565nm): ")) 
    potG = int(input("Insira a potência em mW: "))
    print("Parâmetros escolhidos:", compOndaG,"nm", potG,"mW")

def luzB():
    compOndaB = int(input("Insira o comprimento de onda (entre 440~485nm): ")) 
    potB = int(input("Insira a potência em mW: "))
    print("Parâmetros escolhidos:", compOndaB,"nm", potB,"mW")        

ledR = int(input("Insira a componente do LED vermelho (0~255): "))
ledG = int(input("Insira a componente do LED verde (0~255): "))
ledB = int(input("Insira a componente do LED azul (0~255): "))
cor = (ledR, ledG, ledB)

if cor == (255,0,0): 
    print("Cor vermelha selecionada")
    luzR() 
if cor == (0,255,0):
    print("Cor verde selecionada")
    luzG() 
if cor == (0,0,255):
    print("Cor azul selecionada")
    luzB()

 
tempo = int(input("Insira o tempo necessário: ")) 
for i in range(0, tempo):
    sys.stdout.write("\r Contagem regressiva: {}s".format(i))
    sys.stdout.flush()
    time.sleep(1)

print ("\nA estimulação foi finalizada")

dispositivo1.start()
dispositivo2.start()



