#Aula 08 - 03/09/2020 - Manipulação de arquivos


fileObject = open('aula8.txt', 'w') #w (write) leitura ou escrita
#print(fileObject)

fileObject.write('Essa é a primeira linha do meu arquivo e finaliza com "\\n" \n')
fileObject.write('Essa é a segunda linha do meu arquivo e finaliza com "\\n" \n')
fileObject.write('Essa é a terceira linha do meu arquivo e finaliza com "\\n" \n')

fileObject.close() #sempre que abrir o arquivo, open, tem que fechar, close

fileObject = open('aula8.txt', 'r') #abrindo o arquivo para leitura - r
print(fileObject.read())
fileObject.close()


#Ler os arquivos por linha
fileObject = open('aula08.txt', 'r')
print(fileObject.read(10)) #lê os 10 primeiros caracteres
fileObject.close()


fileObject = open('D:\Repositorios\Program.20202\Programas\dados.txt', 'r') #lendo através do caminho do diretório, caso o arquivo não esteja na pasta do programa
#print(fileObject.read()) #lendo o arquivo todo
print(fileObject.readline()) #lendo a linha 1
print(fileObject.readline()) #lendo a linha 2
print(fileObject.readline()) #lendo a linha 3
fileObject.close()

fileObject = open('aula8.txt', 'r')
#print(fileObject.readlines()[0]) #lendo a primeira linha
#fileObject.close()

for line in fileObject:
    print(line)
fileObject.close()


fileObject = open('aula8.txt', 'w') #abrindo para escrita
Linhas = ['primeira linha \n', 'segunda linha \n', 'terceira linha \n'] #não existe mais o que tinha, foi sobrescrito por essa lista
fileObject.writelines(Linhas) 
fileObject.close()


fileObject = open('aula8.txt', 'r') #abrinda para leitura depois da escrita acima
for line in fileObject: #ler todas as linhas do arquivo
    print(line)
fileObject.close()


#Definição de escopo - with
with open('aula8.txt', 'r') as fileObject: #não precisa fazer o close pq o with já gerencia, só vai existir no escopo
    for line in fileObject:
        print(line)


#Manipulação de arquivos - CSV

import csv

with open('arquivo.csv', 'w', newline = '') as csvFile: #abrindo o arquivo para escrita
    spamWriter = csv.writer(csvFile, delimiter = ' ',
                           quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    spamWriter.writerow(['Spam']*5 + ['feijão'])
    spamWriter.writerow(['Spam']*5 + ['feijão']*2)

with open('arquivo.csv', 'r', newline = '') as csvFile: #abrindo o arquivo para leitura
    spamReader = csv.reader(csvFile, delimiter = ' ',
                           quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for line in spamReader: #ler linha a linha tudo que escreveu
        print(line)


#Exercício slide 30 - IMC
def armazenar(arquivo, tipo, texto):
    if(tipo == 'txt'):
        arquivo.write(texto)
    elif(tipo == 'csv'):
        spamwriter = csv.writer(arquivo, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(texto)

arquivo = open('arquivo.txt','w')
saida = ''
while(True):
    tipo = input('\nVocê deseja salvar a saída em um arquivo txt ou csv? ')
    if(tipo=='txt'):
        arquivo = open('arquivo.txt', 'w')
        break
    elif(tipo=='csv'):
        import csv
        arquivo = open('arquivo.csv', 'w', newline='')
        break
    
while(True):
    peso = float(input ("Qual o seu peso em quilogramas? "))
    altura = float(input ("Qual a sua altura em metros? "))
    imc = peso / (altura**2)
    print("Como o seu peso é: %skg e a sua altura é: %sm, logo, o seu IMC será: %s\n" %(peso, altura, imc))
    if(imc<17):
        print("Você está muito abaixo do peso.")
        armazenar(arquivo,tipo,saida)
    elif(17 <= imc < 18.5):
        print("Você está abaixo do peso normal.")
        armazenar(arquivo,tipo,saida)
    elif(18.5 <= imc < 25):
        print("O seu peso está dentro do normal.")
        armazenar(arquivo,tipo,saida)
    elif(25 <= imc < 30):
        print("Você está acima do peso normal.")
        armazenar(arquivo,tipo,saida)
    else:
        print("Você está muito acima do peso.")
        armazenar(arquivo,tipo,saida)

arquivo.close()


