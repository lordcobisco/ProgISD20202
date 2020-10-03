import csv
def orgDados():
    with open('C:\\Users\\lupc9\\Desktop\\Programação\\coletaFlexJoelho.csv', 'r') as fileObject:
        lista=[]
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp2 = dadosEsp[1].split(']""')[0]
            esp1 = dadosEsp[0].split("[")[1]
            for dadosEsp1 in esp1.split(","):
                lista.append(float(dadosEsp1))
            for dadosEsp2 in esp2.split(","):
                lista.append(float(dadosEsp2))
    return lista
    
def processamento():
    dados = orgDados()
    ang = 0 
    angulos = []
    for i in range (4, len(dados), 4):
        ang = 0.98*(ang + dados[i] * 0.05) + (1 - 0.98) * dados[i-3]
        angulos.append(ang)
    return angulos

def salvar():
    with open('anguloProcessado.csv','w',newline ='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ' ',
                    quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        dados = processamento()
        s1 = []
        s2 = []
        for i in range(0, len(dados), 1):
            if ((i%2) == 0):
                s1.append(dados[i])
            else:
                s2.append(dados[i])
        spamwriter.writerow([s1])
        spamwriter.writerow([s2])
    with open('anguloProcessado.csv', 'r',newline='') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
        for row in spamreader:
            print(','.join(row))
    with open('anguloProcessado.txt','w') as fileObject:
        dados = processamento()
        s1 = []
        s2 = []
        for i in range(0, len(dados), 1):
            if((i%2) == 0):
                s1.append(dados[i])
            else:
                s2.append(dados[i])
        fileObject.writelines(str(s1))
        fileObject.writelines(str(s2))
    with open('anguloProcessado.txt','r') as fileObject:
        print(fileObject.read())

salvar() 