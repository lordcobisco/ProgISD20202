import csv
angulos = list()
listaVariaveis = ('aceleracaox', 'aceleracaoy', 'aceleracaoz', 'velocidadeAngularx', 'velocidadeAngulary', 'velocidadeAngularz')
listaSensor1 = list()
listaSensor2 = list()



# with open('C:\\Users\Dayalla\Desktopjoelho.csv', 'r', newline='') as arquivo:
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    for linha in spamreader:
        print(linha)


# Para o sensor 1 
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    j=0
    for linha in spamreader:
        saida = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        listaSensor1.append(dict())
        for i in range(len(saida)):
            listaSensor1[j][listaVariaveis[i]] = (saida[i]) 
        j+=1
    print(listaSensor1)

# Para o sensor 2 - A VARIAVEL RESULTADO CORRESPONDE À SAÍDA
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    j=0
    for linha2 in spamreader:
        saida2 = linha2[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        listaSensor2.append(dict())
        for i in range(len(saida2)):
            listaSensor2[j][listaVariaveis[i]] = (saida2[i]) 
        j+=1
    print(listaSensor2)


#ang = M**((ang) + dadow**dt)+(1-M)**dadoa
#M = 0.98
#dt = 0.05
#dadow = velocidadeAngulary
#ang = 0.98((ang+velocidadeAngulary*0.05)+(1-0.98)**dadoa, simplificando a fórmula
#fica: ang = 2.45**(velocidadeAngulary) + dadoa


def  calculoAngulo(dadoa, angulos)
    return  dadoa, angulos
    dadoa = float(input("Informe o valor do dadoa: ")
    angulo = 2.45**[velocidadeAngulary] + dadoa
print(dadoa, angulos)
  

arquivotxt = opne('resultadoAngulo.txt','w')
arquivocsv = opne('resultadoAngulo.csv', 'w', newline = '')
spamwriter = csv.writer(arquivocsv, delimiter = '', quotecar = '|', quoting = csv.QUOTE_MINIMAL)
arquivotxt.write('listaSensor1')

for m in listaSensor1:
    angulos.append(ang(m,angulos))

for n in angulos:
    print(n)
    arquivotxt.write(str(n))
    spamwriter.writerow(str(n))

print('Resultados')
arquivotxt.close()
arquivocsv.close()
    

# Para o sensor 2 
with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
    spamreader = csv.reader(arquivo, delimiter=" ", quotechar='|')
    j=0
    for linha2 in spamreader:
        saida2 = linha2[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
        listaSensor2.append(dict())
        for i in range(len(saida2)):
            listaSensor2[j][listaVariaveis[i]] = (saida2[i]) 
        j+=1
    print(listaSensor2)


#ang = M**((ang) + dadow**dt)+(1-M)**dadoa
#M = 0.98
#dt = 0.05
#dadow = velocidadeAngulary
#ang = 0.98((ang+velocidadeAngulary*0.05)+(1-0.98)**dadoa, simplificando a fórmula
#fica: ang = 2.45**(velocidadeAngulary) + dadoa


def  calculoAngulo(dadoa, angulos)
    return dadoa, angulos
    dadoa=float(input("Informa o valor de dadoa: ")
    angulo = 2.45**[velocidadeAngulary] + dadoa
print(dadoa, angulos)  

arquivotxt = open('resultadoAngulo.txt','w')
arquivocsv = open('resultadoAngulo.csv', 'w', newline = '')
spamwriter = csv.writer(arquivocsv, delimiter = '', quotecar = '|', quoting = csv.QUOTE_MINIMAL)
arquivotxt.write('listaSensor2')

for m in listaSensor2:
    angulos.append(ang(m,angulos))

for n in angulos:
    print(n)
    arquivotxt.write(str(n))
    spamwriter.writerow(str(n))

print('Resultados')
arquivotxt.close()
arquivocsv.close()
    