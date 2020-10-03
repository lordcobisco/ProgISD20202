#Atividade Contextializada 08 - Motion Capture

import csv

#Letra a: ler os arquivos em csv e separar os dados dos dois sensores

def lerDadosEsp(filePath = 'coletaFlexJoelho.csv'):
    listaSensores = []
    with open('coletaFlexJoelho.csv','r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                listaSensores.append(float(dadosEsp1))
    return (listaSensores)

listaSensores = lerDadosEsp('coletaFlexJoelho.csv')
print(listaSensores)

#Letra b: calcular os valores de ângulo para cada sensor

listaAngulo = [] 
def calculoAngulo(listaAngulo):
    ang = 0
    M = 0.98
    dt = 0.05

    for n in range(4,len(listaSensores),4): #o dadow está na quarta posição do vetor, logo, percorrer a cada quatro
        ang = M*(ang+listaSensores[n]*dt)+(1-M)*listaSensores[n-3] 
        listaAngulo.append(ang)
    return listaAngulo

calculoAngulo(listaAngulo)

#Letra c: salvar resultados em dois arquivos

with open('anguloProcessado.csv', 'w', newline = '') as csvFile: #abrindo o arquivo para escrita
    spamWriter = csv.writer(csvFile, delimiter = ' ',
                           quotechar = '|', quoting = csv.QUOTE_MINIMAL)

    spamWriter.writerow(['Os ângulos processados são: \n'] + [listaAngulo])
    
with open('anguloProcessado.txt', 'w') as fileObject: 
    fileObject.writelines(["Os ângulos processados são: \n"] + [str(listaAngulo)]) 