import csv
def ler():
     with open('C:\\Users\\eduar\\OneDrive\\Documentos\\GitHub\\ProgISD20202-1\\Maria_Eduarda\\aula8\\coletaFlexJoelho.csv','r') as fileObject:
             lista=[]
             for line in fileObject:
               dadosEsp=line.split('],""[')
               esp2=dadosEsp[1].split(']""')[0]
               #print(esp2)
               esp1=dadosEsp[0].split("[")[1]
               #print(esp1)
               for dadosEsp1 in esp1.split(","):
                     #print(float(dadosEsp1))
                     lista.append(float(dadosEsp1)) 
               for dadosEsp2 in esp2.split(","):
                     #print(float(dadosEsp2))
                     lista.append(float(dadosEsp2)) 
     return lista
def calculoDoAngulo():
     coleta=ler()
     ang=0
     angulos=[]
     #conferencia=[]
     for i in range (4,len(coleta),4):
          #conferencia.append(coleta[i])
          ang=0.98*(ang+coleta[i]*0.05)+(1-0.98)*coleta[i-3]
          angulos.append(ang)
     return angulos
def salvando ():
     coleta=calculoDoAngulo()
     sensor1=[]
     sensor2=[]
     for i in  range(0,len(coleta),1):
          if ((i%2)==0):
               sensor1.append(coleta[i])
          else:
               sensor2.append(coleta[i])
     with open('aula8\\anguloprocessado.csv', 'w', newline='') as csvfile:
          spamwriter = csv.writer(csvfile, delimiter= ' ',
                        quotechar= '|', quoting=csv.QUOTE_MINIMAL)
         
          spamwriter.writerow(['Valores dos Angulos'] )
          spamwriter.writerow(['Sensor 1: \n'] + [sensor1])
          spamwriter.writerow(['Sensor 2: \n']+[sensor2])
     with open('aula8\\anguloprocessado.csv','r',newline='') as csvfile:
          spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
          for row in spamreader:
               print(','.join(row))
     with open('aula8\\anguloprocessado.txt','w') as FileObject:
          FileObject.write("***Valores dos Angulos***\n#Sensor 1:\n")
          FileObject.writelines(str(sensor1))
          FileObject.write("\n\n#Sensor 2:\n")
          FileObject.writelines(str(sensor2))
     with open('aula8\\anguloprocessado.txt','r') as FileObject:
          print(FileObject.read())

print("****Welcome CalcAngle****")
salvando()

