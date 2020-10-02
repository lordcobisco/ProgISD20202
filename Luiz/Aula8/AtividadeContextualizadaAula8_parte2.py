
fileObject = open('C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv', 'r')
for line in fileObject:
	print(line)
#fileObject.close()



def lerDadosEsp(filePath = 'C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv'):
    lista = []
    with open(filePath, 'r') as fileObject:
        for line in fileObject:
            dadosEsp = line.split('],"[')
            esp1 = dadosEsp[0].split('[')[1]
            for dadosEsp1 in esp1.split(','):
                    print(float(dadosEsp1))
                    lista.append(float(dadosEsp1))
    return lista


lista = lerDadosEsp('C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv')
print(lista)


'''
import pandas as pd
dados = pd.read_csv('C:/Users/Cliente_Ibyte/Documents/ISD Neuro Engenharia/2020/Fundamentos de Programação de Desenvolvimento de Projetos Aplicados a Neuroengenharia/Atividades/Aula 8/coletaFlexJoelho.csv')
dados.head()
df = pd.dados.DataFrames(sensores=dados, colums=['Sensor1', 'Sensor2'])
df.head()
print(df)

'''



