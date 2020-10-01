###### PROGRAMA PARA EXPERIMENTO EM OPTOGENÉTICA #####

print('Este é o programa de optogenética\nPara iniciar, você deverá configurar a cor do LED de acordo com o código RGB de cada cor')

def luz(): #utilizando funções
    comprimentodeonda=int(input("Insira o comprimemto de onda em nanometros: ")) #comprimento de onda em nanometros
    potencia=int(input("Insira a potência em mW mm²: ")) #potencia em mW mm²
    print("Os parâmetros de estimulação setados foram:", comprimentodeonda,"nm", potencia,"mW mm²")

led_r = int(input("Insira o código RGB do LED vermelho: "))
led_g = int(input("Insira o código RGB do LED verde: "))
led_b = int(input("Insira o código RGB do LED azul: "))
cor = (led_r,led_g, led_b)

if cor==(0,255,0): #estrutura de decisão
    print("A cor do led setada foi verde")
    luz() #chamando a função
if cor==(255,0,0):
    print("A cor do led setada foi vermelha")
    luz() 
if cor==(0,0,255):
    print("A cor do led setada foi azul")
    luz()

import time,sys #temporização
pulso=int(input("Insira a quantidade de pulsos continuos: ")) #pulso continuo em segundos
for i in range(0, pulso): #estrutura de repetição
    sys.stdout.write("\rA estimulação está ativada {}s".format(i))
    sys.stdout.flush()
    time.sleep(1)

print ("\nA estimulação foi finalizada")
