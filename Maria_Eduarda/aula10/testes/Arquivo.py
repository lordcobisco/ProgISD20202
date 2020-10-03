import csv
import numpy as np
def calculoDoX():
    X=np.random.rand(100)
    return X

def calculoDoY():
    X=calculoDoX()
    Y=[]
    y=0
    for i in range(0,len(X)):
        y=y+3.4*(10*X[i]-y)
        Y.append(y)
    Y=np.array(Y)
    return Y

def salvando ():
     X=calculoDoX()
     Y=calculoDoY()
     with open('aula10\\Trabalho\\dados10.csv', 'w', newline='') as csvfile:
          spamwriter = csv.writer(csvfile, delimiter= ',',quoting=csv.QUOTE_MINIMAL)
          spamwriter.writerow(X)
          spamwriter.writerow(Y)
          #spamwriter.writerow(['Sensor 2: \n']+[sensor2])
     with open('aula10\\dados10.csv','r',newline='') as csvfile:
          spamreader = csv.reader(csvfile,delimiter=' ',quotechar=',')
          for row in spamreader:
               print(','.join(row))


salvando()