print ('Esse programa  tem como objetivo receber dados para o setup do miscroscopio ')

# Definição das variáveis, principais informações no artigo de referência e em:
# https://www.olympus-lifescience.com/pt/laser-scanning/fv3000/#!cms[focus]=cmsContent2543
info1 =  64 #bits
info2 =  63 #ms
info3 = 25 #de 1 a 50
info4 = 4
info5 = 10
info6 = 6
info7 = 12
info8 = 10
info9 = 10
info10 = 100 
info23 = 100  #ms
info24 = 50  #nm


varBool = True

# Informações de dados de entrada retirados do artigo de referência proposto pela atividade
info11 = int (input("Qual a resolução de imagem desejada? \n"))
print ('Houve alteração na variável desejada?' , info11 == info1) # se for igual, aparece True
info12 = int (input("Velocidade de escaneamento?\n"))
print ('Houve alteração na variável desejada?' , info12 == info2)
info13 =  int (input("Qual o zoom óptico?\n"))
print ('Houve alteração na variável desejada?' , info13 == info3)
info14 = int (input("Qual a posição inicial do eixo x?\n"))
print ('Houve alteração na variável desejada?' , info14 == info4)
info15 = int (input("Qual a posição inicial do eixo y?\n"))
print ('Houve alteração na variável desejada?' , info15 == info5)
info16 = int(input("Qual a posição final do eixo x?\n"))
print ('Houve alteração na variável desejada?' , info16 == info6)
info17 = int (input("Qual a posição final do eixo y?\n"))
print ('Houve alteração na variável desejada?' , info17 == info7)
info18 = int (input("Qual o valor do passo no eixo x?\n"))
print ('Houve alteração na variável desejada?' , info18 == info8)
info19 = int (input("Qual o valor do passo no eixo y?\n"))
print ('Houve alteração na variável desejada?' , info19 == info9)
info20 = int (input("Qual o número de superfícies a serem construídas?\n"))
print ('Houve alteração na variável desejada?' , info20 == info10)
info21 = int (input("Qual o tempo de integração do espectrômetro?\n"))
print ('Houve alteração na variável desejada?' , info21 == info23)
info22 = int (input("Qual o comprimento de onda a ser detectado?\n"))
print ('Houve alteração na variável desejada?' , info22 == info24)
print ("\n")


# Configurações setadas
print (' As informações de configurações setadas foram: \n')
print ("Resolução de imagem: ", info11)
print ("Velocidade de escaneamento: ", info12)
print ("Zoom óptico: ", info13)
print ("Posição inicial do eixo x: ", info14)
print ("Posição inicial do eixo y ", info15)
print ("Posição final do eixo x ", info16)
print ("Posição final do eixo y ", info17)
print ("Valor do passo no eixo x: ", info18)
print ("Valor do passo no eixo y: ", info19)
print ("Número de superfícies a serem construídas: ", info20)
print ("Tempo de integração do espectrômetro: ", info21)
print ("Comprimento de onda a ser detectado: ", info22)


# Calibração
calibracao_hor = (input("Digite a calibração no sentido horizontal (Digite 10x a letra 'm' e, em seguinda, 10x a letra 'd'):  \n"))
print ('A informação foi corretamente digitada: ', calibracao_hor)

calibracao_ver = (input("Digite a calibração no sentido horizontal (Digite 10x a letra 'o' e, em seguinda, 10x a letra 'e'):  \n"))
print ('A informação foi corretamente digitada ', calibracao_ver)

print('A calibração foi concluída')





