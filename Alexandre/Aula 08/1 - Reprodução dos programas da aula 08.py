#REPRODUÇÃO DOS PROGRAMAS DA AULA 08

#Criando um arquivo 
arquivo = open("aula8.txt","w")

arquivo.write("Olá mundo\n")
arquivo.write("É muito interessante aprender a programa")

arquivo.close()

#Lendo o arquivo
arquivo = open ("aula8.txt","r")
print ("\n",arquivo.read())
arquivo.close()

arquivo = open ("aula8.txt","r")
print ("\n",arquivo.read(1))
arquivo.close()

arquivo = open ("aula8.txt","r")
print("\n",arquivo.readlines(3))
arquivo.close()

arquivo = open ("aula8.txt","r")
print("\n",arquivo.readlines())
arquivo.close()

arquivo = open ("aula8.txt","r")
for line in arquivo:
    print ("\n",line)
arquivo.close()

with open ("aula8.txt","r") as arquivo:
    for line in arquivo:
        print (line)

with open ("aula8.txt","r") as arquivo:
    for line in arquivo:
        print (line.split())   

with open ("aula8.txt","r") as arquivo:
    for line in arquivo:
        print (line.split("e"))   

## CSV

import csv

with open("arquivo.csv","w", newline = "") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = " ",
                            quotechar = "|",quoting = csv.QUOTE_MINIMAL)
    spamwriter.writerow (["Spam"]*5 + ["Feijão"])
    spamwriter.writerow (["Spam"]*5 + ["Feijão"]*2)

with open('arquivo.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',
                             quotechar='|',quoting = csv.QUOTE_MINIMAL)   
    for line in spamreader: 
        print (line)


