#Aula 08 - Exemplos do slide 08


arquivo = open('aula08.txt','w')
#arquivo.close()
#print(arquivo)

arquivo.write('Essa é a primeira linha do meu arquivo e finaliza com "\\n" \n')
arquivo.write('Essa é a segunda linha do meu arquivo e finaliza com "\\n" \n')
arquivo.write('Essa é a terceira linha do meu arquivo e finaliza com "\\n" \n')
arquivo.write('Essa é a quarta linha do meu arquivo e finaliza com "\\n" \n')

arquivo.close()

arquivo = open('aula08.txt','r')
print(arquivo.read())
arquivo.close()

arquivo = open('aula08.txt','r')
print(arquivo.read(10))
arquivo.close()

arquivo = open('aula08.txt','r')
print(arquivo.readline())
arquivo.close()

arquivo = open('aula08.txt','r')
print(arquivo.readline())
print(arquivo.readline())
arquivo.close()

arquivo = open('aula08.txt', 'r')
print(arquivo.read(10))
arquivo.close()

arquivo = open('aula08.txt','w')
linhasDoTexto = ["Mais uma linha do texto aqui\n", "e outra linha do texto aqui\n","E assim vai\n"]
arquivo.writelines(linhasDoTexto)

arquivo.write("Mais linhas no final")
arquivo.close()

arquivo = open('aula08.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()

arquivo = open('aula08.txt','r')
for line in arquivo:
    print(line)
arquivo.close()
'''
#Contar palavras 
'''
with open('aula08.txt','w') as f:
    linhasDoTexto = ["Mais uma linha do texto aqui\n", "e outra linha do texto aqui\n","E assim vai\n"]
    f.writelines(linhasDoTexto)

with open('aula08.txt','r') as f:
    data = f.readlines()

for line in data:
    words = line.split()
    print(words)

import csv

with open('arquivo08.csv','w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderfull Spam', 'More Spam'])

with open('arquivo08.csv','r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))