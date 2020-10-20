'''
fileObject = open('aula8.txt','w')
fileObject.close()
#print(fileObject)
fileObject.write('Essa é a primeira linha do meu arquivo e finaliza com "\\n" \n')
fileObject.write('Essa é a segunda linha do meu arquivo e finaliza com "\\n" \n')
fileObject.write('Essa é a terceira linha do meu arquivo e finaliza com "\\n" \n')

fileObject.close()

fileObject = open('aula8.txt','r')
print(fileObject.read())
fileObject.close()

fileObject = open('aula8.txt','r')
print(fileObject.read(10))
fileObject.close()


fileObject = open('D:/Projetos/ModeloAndre/read.py','r')
#string = fileObject.read()
#print(fileObject.read())
#print(fileObject.readline())
#print(fileObject.readline())
#print(fileObject.readline())
#print(fileObject.readline())

print(fileObject.readline(10))
print(fileObject.readline(10))
print(fileObject.readline(10))
print(fileObject.readline(10))
fileObject.close()


fileObject = open('aula8.txt','r')
#print(fileObject.readlines()[2])
for line in fileObject:
    print(line)
fileObject.close()


fileObject = open('aula8.txt','w')

Linhas = ['primeira linha \n','segunda linha \n','terceira linha \n']
fileObject.writelines(Linhas)
fileObject.write(Linhas[0])
fileObject.close()

fileObject = open('aula8.txt','r')
for line in fileObject:
    print(line)
fileObject.close()

with open('aula8.txt','r') as fileObject:
    for line in fileObject:
        print(line)

def lerDadosEsp(filePath = 'coletaFlexJoelho.csv'):
    lista = []
    with open(filePath,'r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in  esp1.split(','):
                print(float(dadosEsp1))
                lista.append(float(dadosEsp1))
    return lista

lista = lerDadosEsp('coletaFlexJoelho.csv')
print(lista)
'''
import csv

with open('arquivo.csv','w',newline = '') as csvFile:
    spamWriter = csv.writer(csvFile, delimiter = ' ',
                           quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    
    spamWriter.writerow(['Spam']*5 + ['feijão'])
    spamWriter.writerow(['Spam']*5 + ['feijão']*2)

with open('arquivo.csv','r',newline = '') as csvFile:
    spamReader = csv.reader(csvFile, delimiter = ' ',
                           quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for line in spamReader:
        print(line)