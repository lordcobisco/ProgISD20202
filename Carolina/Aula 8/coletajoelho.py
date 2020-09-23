import csv
def abrindo():
    with open('C:\\Users\\carol\\Desktop\\programacao20202\\isdprog2020\\Aula8\\coletaFlexJoelho.csv', 'r') as fileobj:
        lista=[]
        for line in fileobj:
            dadosEsp=line.split('],""[')
            esp2=dadosEsp[1].split(']""')[0]
            esp1=dadosEsp[0].split("[")[1]
            for dadosEsp1 in esp1.split(","):
                lista.append(float(dadosEsp1))
            for dadosEsp2 in esp2.split(","):
                lista.append(float(dadosEsp2))
    return lista
def calculo():
    coleta=abrindo()
    ang=0 
    angulos=[]
    for i in range (4,len(coleta),4):
        ang=0.98*(ang+coleta[i]*0.05)+(1-0.98)*coleta[i-3]
        angulos.append(ang)
    return angulos
def salvar():
    with open('anguloprocessado.csv','w',newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        coleta=calculo()
        sensor1=[]
        sensor2=[]
        for i in range(0,len(coleta),1):
            if ((i%2)==0):
                sensor1.append(coleta[i])
            else:
                sensor2.append(coleta[i])
        spamwriter.writerow([sensor1])
        spamwriter.writerow([sensor2])
    with open('anguloprocessado.csv', 'r',newline='') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
        for row in spamreader:
            print(','.join(row))
    with open('anguloprocessado.txt','w') as fileobj:
        coleta=calculo()
        sensor1=[]
        sensor2=[]
        for i in range(0,len(coleta),1):
            if((i%2)==0):
                sensor1.append(coleta[i])
            else:
                sensor2.append(coleta[i])
        fileobj.writelines(str(sensor1))
        fileobj.writelines(str(sensor2))
    with open('anguloprocessado.txt','r') as fileobj:
        print(fileobj.read())

salvar()