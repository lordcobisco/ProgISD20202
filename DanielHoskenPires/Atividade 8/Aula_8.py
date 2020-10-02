
fileObject = open ('aula8d.txt', 'w')
#print (fileObject)
fileObject.write ('Essa é a primeira linha do meu arquivo que finaliza com "\\n" \n')
fileObject.write ('Essa é a segunda linha do meu arquivo que finaliza com "\\n" \n')
fileObject.write ('Essa é a terceira linha do meu arquivo que finaliza com "\\n" \n')

fileObject.close()

fileObject = open ('aula8d.txt', 'r')
print (fileObject.read())

fileObject = open ('aula8d.txt', 'r')
print (fileObject.read(10))

#Ler arquivos de outras pastas
fileObject = open ('C:\\Users\\danie\\Desktop\\PNL\\PNL - Ibra\\Anot.txt', 'r')
#print (fileObject.read())
print (fileObject.readline())
print (fileObject.readline())
print (fileObject.readline())

fileObject.close()

fileObject = open ('Aula8d.txt', 'r')
print (fileObject.readlines()[0])
fileObject.close()

fileObject = open ('Aula8d.txt', 'r')
#print (fileObject.readlines()[0])
for line in fileObject:
    print(line)
fileObject.close()

fileObject = open('aula8d.txt', 'w')
Linhas = ['Primeira linha \n', 'Segunda linha \n', 'Terceira linha \n']
fileObject.writelines(Linhas)
fileObject.write(Linhas[1])
fileObject.close()

fileObject = open ('aula8d.txt', 'r')
for line in fileObject:
    print(line)
fileObject.close()

with open ('aula8d.txt','r') as fileObject:
    for line in fileObject:
        print(line)

with open ('aula8d.txt','r') as fileObject:
    for line in fileObject:
        print(line.split('i'))

import csv

with open ('arquivo.cvs', 'w', newline = '') as csvFile:
    spamWriter = csv.writer(csvFile, delimiter = ' ',
                            quotechar = '|', quoting = csv.QUOTE_MINIMAL)

    spamWriter.writerow(['Spam']*5 + ['feijão'])
    spamWriter.writerow(['Spam']*5 + ['feijão']*2)

with open ('arquivo.cvs', 'r', newline = '') as csvFile:
    spamReader = csv.reader(csvFile, delimiter = ' ',
                            quotechar = '|', quoting = csv.QUOTE_MINIMAL)

    for line in spamReader:
        print(line)
