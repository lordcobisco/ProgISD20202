from os import system
system('clear')

'''
# Funcionalidades - Manipulação de Arquivos:
1. Open;
2. Read;
3. Readline e readlines;
4. Write;
5. Close;
6. Repetições contadas (for);
7. With statement;
8. Separação de linhas.
'''

file = open('arquivo','w')
file.write('Escrevendo uma linha no arquivo.\n')
file.write('Escrevendo outra linha.\n')
file.close

'''
file = open('arquivo', 'r')
print(file.read())
file.close


file = open('arquivo', 'r')
#print(file.readline(10))
print(file.readlines()) # Retorna as linhas do arquivo em lista
file.close


#Lendo linhas de um arquivo com for
file = open('arquivo','r')
for linha in file:
  print(linha)
file.close()
'''

# Escrevendo multiplas linhas (Armazena em um arquivo como linhas os campos de uma lista)
arquivo = open('arquivo','w')
linhas = ['Digitando alguma coisa para aparecer num arquivo.\n', 'E isso aqui é outra coisa.\n','mais outra coisa...\n', 'outra coisa...\n']
arquivo.writelines(linhas)
arquivo.write('Adicionando mais um texto.\n')
arquivo.close()

'''
arquivo = open('arquivo','r')
for linha in arquivo:
  print(linha)


# Outra forma de abrir o arquivo para leitura - O arquivo fecha automaticamente após o comando...
with open('arquivo') as arquivo:
  for linha in arquivo:
    print(linha)


# Dando um split() nas linhas
with open('arquivo') as arquivo:
  for linha in arquivo:
    palavras = linha.split()
    print(palavras)
'''

''''
### MANIPULAÇÃO DE ARQUIVOS CSV ###
A biblioteca Lib/csv.py tem as funções:

1. csv.reader;
2. csv.writer.

Parâmetros necessários para a leitura e escrita de arquivos CSV usando a Lib/csv.py:

a. Delimiter - Caractere utilizado para separar campos;
b. Quotechar - Caractere usado para campos que contém caracteres especiais;
c. Quoting - Controla quando as cotações devem ser geradas pelo escritor e reconhecidas pelo leitor;
d. newline = ''
'''

#Escrevendo em um arquivo CSV
import csv
print('Biblioteca importada.')
with open('planilha.csv','w',newline='') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
  spamwriter.writerow(['Spam']*5 + ['Texto Adicional'])
  spamwriter.writerow(['linha1', 'linha2', 'linha3'])

with open('planilha.csv','r',newline='') as arquivo:
  spamreader = csv.reader(arquivo, delimiter=' ', quotechar='|')
  print('Tipo de spamreader: ',type(spamreader))
  for linha in spamreader:
    print('Tipo de linha: ',type(linha))
    print(', '.join(linha))



