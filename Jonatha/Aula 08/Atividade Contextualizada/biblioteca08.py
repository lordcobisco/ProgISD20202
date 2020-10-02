# MANIPULAÇÃO DE ARQUIVOS
from os import system
system('clear')

import csv
print('Biblioteca importada.')


csvfile = open('planilha.csv', 'w', newline='')


spamwriter = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(['linha1', 'linha2', 'linha3'])
spamwriter.writerow(['linha4', 'linha5', 'linha6'])
csvfile.close()


campo = input('Informe o dado que deseja armazenar: ')
arquivo = 'planilha.csv'

csvfile = open(arquivo, 'r', newline='')
dados = list()
spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
for linha in spamreader:
  dados.append(linha)

dados.append(campo)
print('Dados: ')
print(dados)
csvfile.close()


csvfile = open(arquivo, 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerows(dados)
'''
for dado in dados:
  spamwriter.writerow(dado)
'''
csvfile.close()


'''
with open('planilha.csv','w',newline='') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter = ' ', quotechar = ' ', quoting=csv.QUOTE_MINIMAL)
  #spamwriter.writerow(['linha1', 'linha2', 'linha3'])
  spamwriter.writerow(['linha1', 'linha2', 'linha3'])
  spamwriter.writerow(['linha1', 'linha2', 'linha3'])
  #spamwriter.writerow(['linha1', 'linha2', 'linha3'])

with open('planilha.csv','r',newline='') as arquivo:
  spamreader = csv.reader(arquivo, delimiter=' ', quotechar=' ')
  print('Tipo de spamreader: ',type(spamreader))
  for linha in spamreader:
    print('Tipo de linha: ',type(linha))
    print(', '.join(linha))

'''
