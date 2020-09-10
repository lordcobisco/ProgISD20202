'''
fileObject = open('aula8.txt', 'w')
fileObject.write('Hello World! Primeira linha do codigo e finaliza com "\\n" \n')
fileObject.write('Hello World! Segunda linha do codigo e finaliza com "\\n" \n')
fileObject.write('Hello World! TerceiraS linha do codigo e finaliza com "\\n" \n')

#print(fileObject)
fileObject=open('aula8.txt', 'r')
#Ler caractere
#print(fileObject.read(10))
#Ler linha
#print(fileObject.readline(0))
#print(fileObject.readlines()[0])
for linha in fileObject:
    print(linha)

fileObject= open('aula8.txt', 'w')
Linhas = ['primeira\n', 'segunda\n', 'terceira\n']
fileObject.writelines(Linhas)
fileObject.close()
#Uma maneira diferente de abrir o arquivo para não ter que abrir e fechar.
with open('aula8.txt', 'r') as fileObject:
    for line in fileObject:
        print(line.split())
def lerDadosEsp(filePath= 'coletaFlexJoelho.csv'):
    lista=[]
    with open(filePath, 'r') as fileObject:
        for line in fileObject:
            dadosEsp= line.split('],""[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                print(float(dadosEsp1))
                lista.append(float(dadosEsp1))
    return lista
lista=lerDadosEsp('coletaFlexJoelho.csv')
print(lista)

import csv

with open('arquivo.csv', 'w', newline= '') as csvFile:
    spamWriter= csv.writer(csvFile, delimiter= ' ',
     quotechar ='|', quoting= csv.QUOTE_MINIMAL)

    spamWriter.writerow(['Spam']*5 + ['feijao']) 
    spamWriter.writerow(['Spam']*5 + ['feijao']*2)

with open('arquivo.csv', 'r', newline= '') as csvFile:
    spamReader= csv.reader(csvFile, delimiter= ' ',
                    quotechar ='|', quoting= csv.QUOTE_MINIMAL)

    for line in spamReader:
        print(line)

'''
'''
filetxt= open('AuditoryStimulus.txt', 'w')

#Exercício Método de discriminação de estímulos auditivos para primatas através do condicionamento operante usando função
def habituacao(habituado):
    if (habituado):
        filetxt.write("O animal está habituado. Pode iniciar o experimento\n")
    else:
        filetxt.write("O animal não está habituado.\n")
def aproximacoesucessivas(contador, toque):
    if(toque):
        contador= contador +1

    return contador
def Reward(som, barra):
    if (som==1 and barra==1):
        filetxt.write("Liberar 0.5ml de recompensa\n")
    elif(som==2 and barra==2):
        filetxt.write("Liberar 0.5ml de recompensa\n")
    else:
        filetxt.write("Não liberar recompensa!\n")

arquivo= int(input("Como deseja salvar os seus dados?( 1 para txt, 2 para csv)"))
if(arquivo ==1):
    habituado = int(input("O rato está habituado? (Digite 1 para sim, 0 para não)"))
    habituacao(habituado)
    toque=0
    contador=0
    cont=0
    while(contador<2):
        toque=int(input("Animal tocou na barra?"))
        contador= aproximacoesucessivas(contador, toque)
    while(cont<5):
        som= int(input("Qual som foi emitido(1 ou 2)?"))
        barra= int(input("Qual barra foi acionada(1, para esquerda ou 2, para direita)?"))
        Reward(som, barra)
        cont= cont +1
filetxt.close()
'''
filecsv= open('imc.csv', 'w')

def calculoIMC(peso, altura):
    imc= peso/ (altura**2)
    return imc
def apresentarIMC(imc):

    if (imc<17):
        filecsv.write("Você está muito abaixo do peso, IMC\n")
    elif(imc>= 17 and imc <18.5):
        filecsv.write("Você está abaixo do peso normal, IMC\n ")
    elif(imc>= 18.5 and imc < 25):
        filecsv.write("Você está dentro do peso normal, IMC\n")
    elif(imc>= 25 and imc < 30):
        filecsv.write("Você está acima do peso normal, IMC\n")
    elif(imc>30):
        filecsv.write("Você está muito acima do peso, IMC\n")

deseja= 1
while(deseja==1):
    peso=float(input("Digite seu peso:"))
    altura=float(input("Digite sua altura:"))

    imc= calculoIMC(peso,altura)
    apresentarIMC(imc)
    deseja = int(input("Deseja calcular o seu imc novamente?")) 
    arquivo= int(input("Como deseja salvar os seus dados?( 1 para txt, 2 para csv)"))
filecsv.close()