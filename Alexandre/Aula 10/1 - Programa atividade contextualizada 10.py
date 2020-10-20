#Teste com o pandas

import csv 
import pandas as pd #Organizar os dataframes 
from datetime import datetime #Marcador de horário para planilha de saída
now = datetime.now()

def coleta_dados():
    Paciente = input("Digite o nome do paciente")
    Codigo_paciente = int(input("Digite o código do paciente")) 
    D0 = int(input("Digite o nível de dor do paciente pré tratamento"))
    D1 = int(input("Digite o nível de dor do paciente pós tratamento "))
    Grupo = int(input("Digite se pertence ao grupo 01 ou 02"))
   
    
    with open('dados de neuromodulação com pandas.csv', 'a', newline= '') as csvFile:   #Salvar em csv os dados coletados
        spamWriter= csv.writer(csvFile, delimiter= ' ', quoting= csv.QUOTE_MINIMAL)
        
        spamWriter.writerow ([Paciente] + [Codigo_paciente] + [Grupo] + [D0] + [D1])
    


def analise_dados():
    grupo = 4
    while grupo != 1 or 2 or 3:
        grupo = int(input("Você gostaria de ver os dados do intragrupo 01, intragrupo 02 ou todos os dados?"))
        
        df = pd.read_csv("dados de neuromodulação com pandas.csv", encoding = "UTF-8",sep = " ")

        if grupo == 1:
            df_grupo1 = df[df.Grupo == 1]  # Filtrando o grupo 01
            dados_tratamento_grupo_1 = df_grupo1["Dor_pré_tratamento"]   #Dados de pré tratamento do grupo 01 que foi filtrado
            dados_pos_tratamento_grupo_1 = df_grupo1["Dor_pós_tratamento"] #Dados do pós tratamento do grupo 01 que foi filtrado

            print("###DADOS PRÉ TRATAMENTO DO GRUPO 01: ")
            print("\n",dados_tratamento_grupo_1.describe()) #Análise estatística dos dados pré tratamento

            print("###DADOS PÓS TRATAMENTO DO GRUPO 01: ")
            print("\n",dados_pos_tratamento_grupo_1.describe()) #Análise estatística dos dados pós tratamento

            #Salvando os dados processados parcialmente em csv

            with open("dados análise neuromodulação com pandas.csv","a",newline= '') as csvFile:
                spamWriter= csv.writer(csvFile, delimiter= ' ',
                quotechar ='|', quoting= csv.QUOTE_MINIMAL)

                spamWriter.writerow (["\n####### Dados grupo 01: ######"])
                spamWriter.writerow (["dia"] + [now.day] + ["do"] + [now.month]+ ["Horario:"] + [now.hour] + [":"] + [now.minute])
                spamWriter.writerow (["\nPRE TRATAMENTO: "])

            dados_tratamento_grupo_1.describe().to_csv('dados análise neuromodulação com pandas.csv',mode='a', header=False)  #Salvando os dados processados parcialmente

            with open("dados análise neuromodulação com pandas.csv","a",newline= '') as csvFile:
                spamWriter= csv.writer(csvFile, delimiter= ' ',
                quotechar ='|', quoting= csv.QUOTE_MINIMAL)

                spamWriter.writerow (["\nPOS TRATAAMENTO: "])
            dados_pos_tratamento_grupo_1.describe().to_csv('dados análise neuromodulação com pandas.csv',mode='a', header=False)  #Salvando os dados processados parcialmente

        elif grupo == 2:
            df_grupo2 = df[df.Grupo == 2]  # Filtrando o grupo 02
            dados_tratamento_grupo_2 = df_grupo2["Dor_pré_tratamento"]   #Dados de pré tratamento do grupo 02 que foi filtrado
            dados_pos_tratamento_grupo_2 = df_grupo2["Dor_pós_tratamento"] #Dados do pós tratamento do grupo 02 que foi filtrado

            print("###DADOS PRÉ TRATAMENTO DO GRUPO 02: ")
            print(dados_tratamento_grupo_2.describe()) #Análise estatística dos dados pré tratamento

            print("###DADOS PÓS TRATAMENTO DO GRUPO 02: ")
            print("\n", dados_pos_tratamento_grupo_2.describe()) #Análise estatística dos dados pós tratamento

            #Salvando os dados processados parcialmente em csv

            with open("dados análise neuromodulação com pandas.csv","a",newline= '') as csvFile:
                spamWriter= csv.writer(csvFile, delimiter= ' ',
                quotechar ='|', quoting= csv.QUOTE_MINIMAL)

                spamWriter.writerow (["\n####### Dados grupo 02: ######"])
                spamWriter.writerow (["dia"] + [now.day] + ["do"] + [now.month]+ ["Horario:"] + [now.hour] + [":"] + [now.minute])
                spamWriter.writerow (["\nPRE TRATAMENTO: "])

            dados_tratamento_grupo_2.describe().to_csv('dados análise neuromodulação com pandas.csv',mode='a', header=False)  #Salvando os dados processados parcialmente

            with open("dados análise neuromodulação com pandas.csv","a",newline= '') as csvFile:
                spamWriter= csv.writer(csvFile, delimiter= ' ',
                quotechar ='|', quoting= csv.QUOTE_MINIMAL)

                spamWriter.writerow (["\nPOS TRATAAMENTO: "])
            
            dados_pos_tratamento_grupo_2.describe().to_csv('dados análise neuromodulação com pandas.csv',mode='a', header=False)

        elif grupo == 3:
            dados_tratamento_dois_grupos = df["Dor_pré_tratamento"]
            dados_pós_tratamento_dois_grupos = df["Dor_pós_tratamento"]

            print("###DADOS PRÉ TRATAMENTO DOs DOIS GRUPOS: ")
            print(dados_tratamento_dois_grupos.describe())

            print("###DADOS PÓS TRATAMENTO DOS DOIS GRUPOS: ")
            print("\n",dados_pós_tratamento_dois_grupos.describe())

            #Salvando os dados processados parcialmente em csv

            with open("dados análise neuromodulação com pandas.csv","a",newline= '') as csvFile:
                spamWriter= csv.writer(csvFile, delimiter= ' ',
                quotechar ='|', quoting= csv.QUOTE_MINIMAL)

                spamWriter.writerow (["\n####### Dados DOIS GRUPOS: ######"])
                spamWriter.writerow (["dia"] + [now.day] + ["do"] + [now.month]+ ["Horario:"] + [now.hour] + [":"] + [now.minute])
                spamWriter.writerow (["\nPRE TRATAMENTO: "])

            dados_pós_tratamento_dois_grupos.describe().to_csv('dados análise neuromodulação com pandas.csv',mode='a', header=False)  #Salvando os dados processados parcialmente

            with open("dados análise neuromodulação com pandas.csv","a",newline= '') as csvFile:
                spamWriter= csv.writer(csvFile, delimiter= ' ',
                quotechar ='|', quoting= csv.QUOTE_MINIMAL)

                spamWriter.writerow (["\nPOS TRATAAMENTO: "])
            dados_pós_tratamento_dois_grupos.describe().to_csv('dados análise neuromodulação com pandas.csv',mode='a', header=False)
        else:
            print("\n,Digite um número válido")

        
        

#EXECUÇÃO

coleta_ou_analise = int(input(" Digite 1 para coleta, 2 para visualizar a tabela de dados coletados e 3 para análise"))

if coleta_ou_analise == 1:

   coleta_dados()

elif coleta_ou_analise == 2:
    df = pd.read_csv("dados de neuromodulação com pandas.csv", encoding = "UTF-8",sep = " ")
    print (df)


else:
    analise_dados()