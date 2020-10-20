import csv

dados_brutos = open('coleta_unity.csv', 'r')

periodo_1 = []
periodo_2 = []

valores_objeto1_periodo1 = []
valores_objeto1_periodo2 = []

dados_objeto1_periodo1 = []
dados_objeto1_periodo2 = []

objeto1_periodo1 = []
objeto1_periodo2 = []

#salvando os dados em cada período do jogo
for linhas in dados_brutos:
    if 'Período 1' in linhas:
     periodo_1.append(linhas)
    elif 'Período 2' in linhas:
     periodo_2.append(linhas)

#salvando os dados do objeto2 nas listas
for linhas in periodo_1:
    if 'objeto2' in linhas:
     objeto1_periodo1.append(linhas)

for linhas in periodo_2:
    if 'objeto2' in linhas:
     objeto1_periodo2.append(linhas)

for linhas in objeto1_periodo1:
    valores1 = linhas.split('(') #removendo os caracteres que indtroduzem os dados
    valores2 = linhas.split('"\n')
    valores_objeto1_periodo1 = valores1[1].split('(')[0] #guardando somente os valores após o parenteses
    valores_objeto1_periodo1 = valores2[0].split('(')[1] #pegando o que vem antes das aspas e contrabarra
    
    for ob1 in valores_objeto1_periodo1.split(";"): #removendo os pontos e vírgulas entre os valores dos objetos
        dados_objeto1_periodo1.append(float(ob1))

for linhas2 in objeto1_periodo2:
    valores1 = linhas2.split('(') #removendo os caracteres que indtroduzem os dados
    valores2 = linhas2.split('"\n')
    valores_objeto1_periodo2 = valores1[1].split('(')[0] #guardando somente os valores após o parenteses
    valores_objeto1_periodo2 = valores2[0].split('(')[1] #pegando o que vem antes das aspas e contrabarra

    for ob2 in valores_objeto1_periodo2.split(";"): #removendo os pontos e vírgulas entre os valores dos objetos
        dados_objeto1_periodo2.append(float(ob2))

#vetores que armazenarão os valores finais no formato float

objeto1_periodo1_x = []
objeto1_periodo1_y = []
objeto1_periodo1_z = []

objeto1_periodo2_x = []
objeto1_periodo2_y = []
objeto1_periodo2_z = []

def passa_valores():

    for i in range(0,len(dados_objeto1_periodo1),1):#percorre todos os dados ja "limpos" de 1 em 1
        if(i%3 == 0 or i==0):
            objeto1_periodo1_x.append(dados_objeto1_periodo1[i]) #indices pares = sensor1
        elif(i%3 == 1 or i == 1):
            objeto1_periodo1_y.append(dados_objeto1_periodo1[i])  
        elif(i%3 == 2 or i == 2):
            objeto1_periodo1_z.append(dados_objeto1_periodo1[i])  

    for i in range(0,len(dados_objeto1_periodo2),1):#percorre todos os dados ja "limpos" de 1 em 1
        if(i%3 == 0 or i==0):
            objeto1_periodo2_x.append(dados_objeto1_periodo2[i]) #indices pares = sensor1
        elif(i%3 == 1 or i == 1):
            objeto1_periodo2_y.append(dados_objeto1_periodo2[i])  
        elif(i%3 == 2 or i == 2):
            objeto1_periodo2_z.append(dados_objeto1_periodo2[i])  

with open('informacoes_objeto1_periodo1.csv',  'w', newline = '') as csvfile:
    wr = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting =  csv.QUOTE_MINIMAL) #criando uma planilha que separará os dados

    passa_valores()

    wr.writerows(['objeto1 no período 1 x: ']+[objeto1_periodo1_x])
    wr.writerows(['objeto1 no período 1 y: ']+[objeto1_periodo1_y])
    wr.writerows(['objeto1 no período 1 z: ']+[objeto1_periodo1_z])


from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

passa_valores() #chama a função

plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot3D(objeto1_periodo1_z,objeto1_periodo1_y, objeto1_periodo1_x ,'red')
ax.view_init(90, -90)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Trajetória do objeto 1 no período 1')

plt.figure(2)
ax1 = plt.axes(projection='3d')
ax1.plot3D(objeto1_periodo2_z,objeto1_periodo2_y, objeto1_periodo2_x ,'green')
ax1.view_init(90, -90)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_title('Trajetória do objeto 1 no período 2')

plt.show()




