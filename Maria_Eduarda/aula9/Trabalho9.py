import csv
import numpy as np

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
     coleta=np.array(list(ler()))
     ang=0
     angulos=[]
     #conferencia=[]
     for i in range (5,len(coleta),5):
          #conferencia.append(coleta[i])
          ang=0.98*(ang+coleta[i]*0.05)+(1-0.98)*coleta[i-4]
          angulos.append(ang)
     resultado=np.array(list(angulos))
     return resultado
def VariacaoAngular():
    Angulos=calculoDoAngulo()
    variacao=[]
    for i in range(0,len(Angulos),1):
        VarAng=Angulos[i+1]-Angulos[i]
        variacao.append(VarAng)
    Variacao_Angulo=np.array(list(variacao))
    return Variacao_Angulo

def Somatorio():
    Angulos=calculoDoAngulo()
    soma=np.sum(Angulos)
    return soma

def Media():
    Angulos=calculoDoAngulo()
    media=np.mean(Angulos)
    return media

def Minimo():
    Angulos=calculoDoAngulo()
    mim=np.amin(Angulos)
    return mim

def Maximo():
    Angulos=calculoDoAngulo()
    maxi=np.amax(Angulos)
    return maxi

def Integral ():
    Angulos=calculoDoAngulo()
    somaAcumulada=np.cumsum(Angulos)
    return somaAcumulada

def Aredondar():
    Angulos=calculoDoAngulo()
    aredondamento=np.around(Angulos,2)
    return aredondamento

def DiferencaMedia():
    Angulos=calculoDoAngulo()
    diferenca_media=(np.square(Angulos))/Angulos.size
    return diferenca_media

def salvando ():
     soma=Somatorio()
     media=Media()
     minimo=Minimo()
     maximo=Maximo()
     integral=Integral()
     aredondar=Aredondar()
     diferenca_media=DiferencaMedia()
     with open('aula9\\anguloprocessado9.csv', 'w', newline='') as csvfile:
          spamwriter = csv.writer(csvfile, delimiter= ' ',
                        quotechar= '|', quoting=csv.QUOTE_MINIMAL)
          coleta=np.array(list(calculoDoAngulo()))
          sensor1=[]
          sensor2=[]
          for i in  range(0,len(coleta),1):
               if ((i%2)==0):
                    sensor1.append(coleta[i])
               else:
                    sensor2.append(coleta[i])
          spamwriter.writerow(['Valores dos Angulos'] )
          spamwriter.writerow(['Sensor 1: \n'] + [sensor1])
          spamwriter.writerow(['Sensor 2: \n']+[sensor2])
          spamwriter.writerow(['Operações:'] )
          spamwriter.writerow(['Somatório: \n']+[soma])
          spamwriter.writerow(['Media: \n']+[media])
          spamwriter.writerow(['Minimo: \n']+[minimo])
          spamwriter.writerow(['Maximo: \n']+[maximo])
          spamwriter.writerow(['Integral: \n']+[integral])
          spamwriter.writerow(['Aredondamento: \n']+[aredondar])
          spamwriter.writerow(['Diferença média: \n']+[diferenca_media])
     with open('aula9\\anguloprocessado9.csv','r',newline='') as csvfile:
          spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
          for row in spamreader:
               print(','.join(row))
     with open('aula9\\anguloprocessado9.txt','w') as FileObject:
          coleta=calculoDoAngulo()
          sensor1=[]
          sensor2=[]
          for i in  range(0,len(coleta),1):
               if ((i%2)==0):
                    sensor1.append(coleta[i])
               else:
                    sensor2.append(coleta[i])
          FileObject.write("***Valores dos Angulos***\n#Sensor 1:\n")
          FileObject.writelines(str(sensor1))
          FileObject.write("\n\n#Sensor 2:\n")
          FileObject.writelines(str(sensor2))
          FileObject.write("***Operacoes***\n#Somatorio:\n")
          FileObject.write(str(soma))
          FileObject.write("Media:\n")
          FileObject.write(str(media))
          FileObject.write("Minimo:\n")
          FileObject.write(str(minimo))
          FileObject.write("Maximo:\n")
          FileObject.write(str(maximo))
          FileObject.write("Integral:\n")
          FileObject.write(str(integral))
          FileObject.write("Aredondamento:\n")
          FileObject.write(str(aredondar))
          FileObject.write("Diferença Média:\n")
          FileObject.writelines(str(diferenca_media))

     with open('aula9\\anguloprocessado9.txt','r') as FileObject:
          print(FileObject.read())

print("****Welcome CalcAngle****")
salvando()   