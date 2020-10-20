
import csv

def lerDadosEsp(filePath = 'H14.09.006.GRAN_F.csv'):
    with open(filePath,'r',newline='') as filecsv:
        excelReader = csv.reader(filecsv, delimiter = ' ',
                                quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        for line in excelReader:
            print(line)

lerDadosEsp('H14.09.006.GRAN_F.csv')

import numpy
import matplotlib.pyplot as plt

dataset = open('H14.09.006.GRAN_F.csv','r')

N = 2
MeansN = ('Marker3')
MeansG = ('Marker4')
nStd = ('Marker3')
gStd = ('Marker4')
ind = np.arange(N)
width = 0.35

p1 = plt.bar(ind, MeansN, width, yerr=nStd)
p2 = plt.bar(nd, MeansG, width,    
                         bottom=MeansN, yerr=gStd)
                         


plt.title('Razão Glia Neurônio')
plt.xlabel('x label')
plt.ylabel('jsnsjdn')

plt.show