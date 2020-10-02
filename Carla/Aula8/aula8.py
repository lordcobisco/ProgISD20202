'''
arquivo = open("workfile","w") 
 
arquivo.write("Hello World\n") 
arquivo.write("This is our new text file\n") 
arquivo.write("and this is another line.\n") 
arquivo.write("Why? Because we can.\n") 
 
arquivo.close()

arquivo = open("workfile","r") 
print(arquivo.read())

arquivo = open("workfile","r") 
print(arquivo.read(5))

arquivo = open("workfile","r")
print(arquivo.readline())
print(arquivo.readline())

arquivo = open("workfile","r")
print(arquivo.readline(3))

arquivo = open("workfile","r")
print(arquivo.readlines())

arquivo = open("workfile","r")
for linha in arquivo: 
  print(linha) 
 
arquivo = open("workfile","w")
linahsDoTexto = ["Uma linha do texto aqui\n", "e outra linha do texto aqui\n", 
"mais uma linha do texto\n", "quarta linha\n"] 
arquivo.writelines(linahsDoTexto) 

arquivo.write("Linha adicionada no final")

arquivo.close()
arquivo = open("workfile","r")
for linha in arquivo: 
  print(linha) 
arquivo.close()

arquivo = open("workfile","w")
linahsDoTexto = ["Uma linha do texto aqui\n", "e outra linha do texto aqui\n", 
"mais uma linha do texto\n", "quarta linha\n"] 
arquivo.writelines(linahsDoTexto)
arquivo.close()

with open("workfile") as arquivo: 
  for line in arquivo: 
    print (line)


with open("hello", "w") as f:
  linahsDoTexto = ["Uma linha do texto aqui\n", "e outra linha do texto aqui\n", 
"mais uma linha do texto\n", "quarta linha\n"]
  f.writelines(linahsDoTexto)

with open("hello", "r") as f:
  data = f.readlines()
 
for line in data:
  words = line.split()
  print(words)
  '''

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
