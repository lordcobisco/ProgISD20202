'''
arquivo = open("workfile","w") 
 
arquivo.write("Dayalla") 
arquivo.write("\nlinha") 
arquivo.write("\nlinha de novo") 
arquivo.write("\nlinha de novo") 
 
arquivo.close()

arquivo = open("workfile","r") 
print(arquivo.read())

arquivo = open("workfile","r") 
print(arquivo.read(10))

arquivo = open("workfile","r")
print(arquivo.readline())
print(arquivo.readline())

arquivo = open("workfile","r")
print(arquivo.readline(15))

arquivo = open("workfile","r")
print(arquivo.readlines())

arquivo = open("workfile","r")
for linha in arquivo: 
  print(linha) 
 
arquivo = open("workfile","w")
linhas = ["Dayalla\n", "ISD\n", 
"LINHA DE TEXTO\n", "OUTRA LINHA DE TEXTO\n"] 
arquivo.writelines(linhas) 

arquivo.write("Linha adicionada no final")

arquivo.close()
arquivo = open("workfile","r")
for linha in arquivo: ["Dayalla\n", "ISD\n", 
"LINHA DE TEXTO\n", "OUTRA LINHA DE TEXTO\n"] 
  print(linha) 
arquivo.close()

arquivo = open("workfile","w")
linahsDoTexto = 
arquivo.writelines(linahsDoTexto)
arquivo.close()

with open("workfile") as arquivo: 
  for line in arquivo: 
    print (line)


with open("hello", "w") as f:
  linahsDoTexto = ["Dayalla\n", "ISD\n", "LINHA DE TEXTO\n", "OUTRA LINHA DE TEXTO\n"] 
  f.writelines(linahsDoTexto)

with open("hello", "r") as f:
  data = f.readlines()
 
for line in data:
  words = line.split()
  print(words)
  

# importando aquivos csv

import csv

with open('eggs.csv', 'w', newline='') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=' ',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
  spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
  spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', 'r', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
    print(', '.join(row))
