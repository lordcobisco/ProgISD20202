import csv
import numpy as np
def calculoDoX():
     X=np.random.rand(100)
     return X
def calculoDoY():
     X=calculoDoX()
     Y=[]
     for i in range(0,len(X)):
          Y.append(X[i])
     Yt=np.array(Y)
     return Yt
def salvando ():
     X=calculoDoX()
     Y=calculoDoY()
     with open('aula10\\Trabalho\\anguloprocessado10.csv', 'w', newline='') as csvfile:
          spamwriter = csv.writer(csvfile, delimiter= ' ',
                                 quoting=csv.QUOTE_MINIMAL)
          spamwriter.writerows([X])
          spamwriter.writerows([Y])

a=calculoDoX()
print(a)
salvando()

