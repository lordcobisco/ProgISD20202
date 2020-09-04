import csv
"""F=open('novo.txt','w') #CriarArquivo
print(F)
#Escrever
F.write("Lá vem esse tal Hello world novamente\\n \n")
F.write("Queria que o platfor.io me ajudasse\n")
F.write("Eu só queria que ele deixasse eu dá start no django\n")
F.close()#tudo que abre fecha
F=open('novo.txt','r')
#print(F.read())#Ler
print(F.readline()) #ler a primeira linha
print(F.readlines(1))#ler linhas
for line in F:
    print(line)

N=open('C:\\Users\\eduar\\OneDrive\Documentos\\GitHub\\ProgISD20202-1\\Maria_Eduarda\\Readme.txt','r')
print(N.read())

FlieObject=open('novo.txt','w')
Lista=["Sei que você\n","Vai querer ser\n","Uma de nós\n"]
FlieObject.writelines(Lista)#qualquer lugar
FlieObject.write(Lista[0])#na sequencia
FlieObject.close()

FlieObject=open('novo.txt','r')
print(FlieObject.read())

#Só existe no scopo
def ler():
     with open('coletaFlexJoelho.csv','r') as fileObject:
    #print(fileObject.read())
    #data=fileObject.readlines()
         lista=[]
         for line in fileObject:
             dadosEsp=line.split('],""[')
             esp1=dadosEsp[0].split("[")[1]
             for dadosEsp1 in esp1.split(","):
                 print(float(dadosEsp1))
                 lista.append(float(dadosEsp1))
     return lista    
print(ler())""" 
with open('eggs.csv', 'w', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter= ' ',
                        quotechar= '|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
     spamwriter.writerow(['Spam', 'Lovely Spam', "Wonderful Spam"])
with open('eggs.csv','r',newline='') as csvfile:
     spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
     for row in spamreader:
         print(','.join(row))
