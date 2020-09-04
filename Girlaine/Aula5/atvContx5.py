#Questão A
Lista = ['Estado', 'População', 'CasosAcumulados', 'CasosNovos', 'ObitosAcumulados', 'ObitosNovos']
Estados =  ['AC', 'TO', 'PI' , 'PB' , 'AL' , 'RJ','DF' ]
População = [881935,1572866,3273227,4018127,3337357,17264943,3015268]
CasosAcumulados = [22933,38845,67226,97497,73701,199480,140170]
CasosNovos = [28,989,911,1274,763,4829,1435]
ObitosAcumulados = [590,531,1637,2203,1774,14728,2097]
ObitosNovos = [8,15,8,20,11,162,55]



#Região de Saúde 

Estados = ['AC', 'TO', 'PI' , 'PB' , 'AL' , 'RJ', 'DF']
print(Estados[0])
RegiaoDeSaude = ('Alto Acre', 'Baixo Acre e Purus','Jarua','Tarauaca/envira'),
print(RegiaoDeSaude)

print(Estados[1])
RegiaoDeSaude = ('Amor Perfeito', 'Bico de papagaio', ' Cantão', 'Capim Dourado')
print(RegiaoDeSaude)

print(Estados[2])
RegiaoDeSaude = ('Parnaiba',' Barras', 'Piripiri')
print(RegiaoDeSaude)

print(Estados[3])
RegiaoDeSaude = ('Cabedolo', 'Conde','Joao Pessoa')
print(RegiaoDeSaude)

print(Estados[4])
RegiaoDeSaude = ('Maceio','Cajueiro','Craibas','Igaci')
print(RegiaoDeSaude)

print(Estados[5])
RegiaoDeSaude = ('Baia da Ilha Grande','Baixada Litorânea','Centro-Sul','Metropolitana I')
print(RegiaoDeSaude)

print(Estados[6])
RegiaoDeSaude = ('Asa Norte','Lago Norte','Varjão','Cruzeiro')
print(RegiaoDeSaude)

# Questão b

print(Estados[5])
print(CasosAcumulados[5])

# Questão c

print(Estados[0])
print(ObitosAcumulados[0])

print(Estados[1])
print(ObitosAcumulados[1])

print(Estados[2])
print(ObitosAcumulados[2])

print(Estados[3])
print(ObitosAcumulados[3])

print(Estados[4])
print(ObitosAcumulados[4])

print(Estados[5])
print(ObitosAcumulados[5])

print(Estados[6])
print(ObitosAcumulados[6])

#Questão d 

print(Estados[3])
ObitosNovos = [0,0,0,0,0,7,0,0,0,0,6,0,55]
print(ObitosNovos)
print(ObitosNovos[-10])

#Questão é 

'''
Os valores que encontram-se na tupla, não são modificados. Quanto os valores nas listas, são modificaveis. 
'''

#Questão F

Estado = ['AC']
Municipios = ['Acrelandia', 'Assis Basil', 'Abreulandia','Aguiarnopolis','Acaua','Teresina','Aguia Branca', 'Aguia'],
RegiaoDeSaude = ['Baixo Acre e Puros ', 'Alto Acre', 'Cantao','bico do papagaio', 'Vale do Rio guaribas', 'Entre Rios'],
População = [15256,7417,2579,6733,7084,86485,10234,5640,20196,17545,203785,11759,3015268],
CasosAcumulados = [398,440,28,356,24,22102,52,24,69,426,4379,167,140170]
CasosNovos = [20,1,6,3,0,299,0,0,0,1,92,0,1435]
ObitosAcumulados = [8,9,2,6,0,833,2,0,2,6,137,6,2097]
ObitosNovos = [0,0,0,0,0,7,0,0,0,0,6,0,55] 

Lista = ['AC']
print(Lista)
Nova_Lista = ['Municipios','RegiaoDeSaude','População','CasosAcumulados','CasosNovos','ObitosAcumulados','ObitosNovos',Lista]
print(Nova_Lista)

#Questão G

Nova_Lista.remove('RegiaoDeSaude')
print(Nova_Lista)

#Questão H

ObitosNovos = [0,0,0,0,0,7,0,0,0,0,6,0,55]
print(min(ObitosNovos))
print(max(ObitosNovos))

# Questão i

 AC = {"Municipios" : [Acrelandia, Assis Basil, Abreulandia, Aguiarnopolis, Acaua, Teresina , Aguia Branca, Aguia]}
 print(AC)
 print(AC["Municipios"])
 








