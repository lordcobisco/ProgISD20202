#separando por splits

with open ('coletaFlexJoelho.csv','r') as fileObject:
    for line in fileObject:
        print(line.split('],""['))

#separando por mais splits (Dados numéricos)
with open ('coletaFlexJoelho.csv','r') as fileObject:
    for line in fileObject:
        dadosEsp = line.split('],""[')
        esp1 = dadosEsp[0].split('[')[1]
        for dadosEsp1 in esp1.split(','):
            print (float(dadosEsp1))

#otimizando com função def
def lerDadosesp(filePath = 'coletaFlexJoelho.csv'):
    with open (filePath,'r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                print (float(dadosEsp1))   

lerDadosesp('coletaFlexJoelho.csv')


#otimizando com função def e lista
def lerDadosesp(filePath = 'coletaFlexJoelho.csv'):
    lista = []
    with open (filePath,'r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],""[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                print (float(dadosEsp1))   
                lista.append(float(dadosEsp1))
    return lista

lista = lerDadosesp('coletaFlexJoelho.csv')
print(lista)

