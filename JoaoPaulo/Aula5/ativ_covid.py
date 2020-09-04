# Adicionando as informações a lista de dez estados escolhidos aleatoriamente

estados = ['RO','AC','AP','PI','RN','PB','PE','AL','BA','RJ']
populacao =[1777225, 881935, 845731, 3273227,3506853,4018127,9557071,3337357,14873064,17264943]
CasosAcumulado =[50147,23322,40603,69839,59138,99445,116359,74622,228596,205916]
casosnovos=[426,176,392,1364,471,951,1142,482,3937,2923]
obitosAcumulados=[1045,595,626,1660,2133,2244,7303,1793,4685,15074]
NovosObitos=[8,4,4,7,7,21,23,9,74,161]

#Adicionando as informações as tuplas de dez estados

estados_tupla = ('RO','AC','AP','PI','RN','PB','PE','AL','BA','RJ')
populacao_tupla =(1777225, 881935, 845731, 3273227,3506853,4018127,9557071,3337357,14873064,17264943)
CasosAcumulado_tupla =(50147,23322,40603,69839,59138,99445,116359,74622,228596,205916)
casosnovos_tupla=(426,176,392,1364,471,951,1142,482,3937,2923)
obitosAcumulados_tupla=(1045,595,626,1660,2133,2244,7303,1793,4685,15074)
NovosObitos_tupla=(8,4,4,7,7,21,23,9,74,161)

#Passando os valores dos estados para a lista principal
lista_covid = [estados,populacao,CasosAcumulado,casosnovos,obitosAcumulados,NovosObitos]

#Passando os valores dos estados para a tupla principal
lista_covid_tupla = (estados,populacao,CasosAcumulado,casosnovos,obitosAcumulados,NovosObitos)


#Exibindo a quantidade de óbitos acumulados no RJ para a lista
if 'RJ' in lista_covid[0]:
    print("O número de óbitos acumulados no RJ é: ", lista_covid[4][9])

#Exibindo a quantidade de óbitos acumulados no RJ para a tupla
if 'RJ' in lista_covid_tupla[0]:
    print("O número de óbitos acumulados no RJ é: ", lista_covid_tupla[4][9])

#Printando os valores de números de óbitos por estado para a lista

print (lista_covid[0][0], lista_covid[4][0])
print (lista_covid[0][1], lista_covid[4][1])
print (lista_covid[0][2], lista_covid[4][2])
print (lista_covid[0][3], lista_covid[4][3])
print (lista_covid[0][4], lista_covid[4][4])
print (lista_covid[0][5], lista_covid[4][5])
print (lista_covid[0][6], lista_covid[4][6])
print (lista_covid[0][7], lista_covid[4][7])
print (lista_covid[0][8], lista_covid[4][8])
print (lista_covid[0][9], lista_covid[4][9])

#Printando os valores de números de óbitos por estado para a tupla

print (lista_covid_tupla[0][0], lista_covid_tupla[4][0])
print (lista_covid_tupla[0][1], lista_covid_tupla[4][1])
print (lista_covid_tupla[0][2], lista_covid_tupla[4][2])
print (lista_covid_tupla[0][3], lista_covid_tupla[4][3])
print (lista_covid_tupla[0][4], lista_covid_tupla[4][4])
print (lista_covid_tupla[0][5], lista_covid_tupla[4][5])
print (lista_covid_tupla[0][6], lista_covid_tupla[4][6])
print (lista_covid_tupla[0][7], lista_covid_tupla[4][7])
print (lista_covid_tupla[0][8], lista_covid_tupla[4][8])
print (lista_covid_tupla[0][9], lista_covid_tupla[4][9])

#Reparando os valores para a Paraíba

if 'PB' in lista_covid[0]:
    lista_covid[5][5] = lista_covid[5][5] + 10
    print("A lista foi modificada")
    print(lista_covid)

if 'PB' in lista_covid_tupla[0]:
    lista_covid_tupla[5][5] = lista_covid_tupla[5][5] + 10
    print("A tupla foi modificada")
    print(lista_covid_tupla)
    #Percebe-se aqui que a tupla nao foi modificada, pois a mensagem não foi printada.

#Criando lista para o Acre 

cidades_ac = ['Acrelândia','Assis Brasil','Brasiléia','Bujari','Capixaba','Cruzeiro do Sul','Epitaciolândia','Feijó','Jordão','Mâncio Lima','Manoel Urbano','Marechal Thaumaturgo','Plácido de Castro','Porto Walter','Rio Branco','Rodrigues Alves','Santa Rosa do Purus','Senador Guiomard','Sena Madureira','Tarauacá','Xapuri','Porto Acre']
populacao_ac = [15256,7417,26278,10266,11733,88376,18411,34780,8317,18977,9459,18867,19761,11982,407319,18930,6540,23024,45848,42567,19323,18504]
regiao_ac = ['BAIXO ACRE E PURUS','ALTO ACRE','ALTO ACRE','BAIXO ACRE E PURUS','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','ALTO ACRE','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','BAIXO ACRE E PURUS','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','ALTO ACRE','BAIXO ACRE E PURUS']
CasosAcumulado_ac = [403,454,1064,355,243,3031,463,1008,128,554,256,296,389,241,9723,140,204,414,1300,1451,733,472]
casosnovos_ac = [5,9,7,0,3,8,7,32,9,1,1,6,2,1,22,1,2,10,20,2,26,2]
obitosAcumulados_ac = [8,9,15,6,7,53,13,18,1,8,2,1,8,2,377,6,2,10,10,13,11,15]
NovosObitos_ac = [0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Criando lista principal para as variáveis do Acre
nova_lista_AC = [cidades_ac,populacao_ac, regiao_ac, CasosAcumulado_ac,casosnovos_ac,obitosAcumulados_ac,NovosObitos_ac]

#Adicionando  a nova lista à principal
lista_covid.append(nova_lista_AC)
print(lista_covid)
#Removendo as regiões do Acre da lista principal
nova_lista_AC.remove(regiao_ac)
print(lista_covid)

#Comparando a soma de dados dos MUNICÍPIOS do Acre com os dados do ESTADO do Acre para o dia de download: 20/08

lista_somas_ac = [sum(nova_lista_AC[1]),sum(nova_lista_AC[2]), sum(nova_lista_AC[3]),sum(nova_lista_AC[4]),sum(nova_lista_AC[5])]

if(lista_somas_ac[0] == lista_covid[1][1]):
    if(lista_somas_ac[1] == lista_covid[2][1]):
        if(lista_somas_ac[2] == lista_covid[3][1]):
            if(lista_somas_ac[3] == lista_covid[4][1]):
                if(lista_somas_ac[4] == lista_covid[5][1]):
                    print("As somas batem.")
                    print(True)

print("O tamanho total da lista é: ", len(lista_covid))

print(lista_covid[5])
print("O número  máximo de óbitos na lista é " , max(lista_covid[5]))
print("O número  mínimo de óbitos na lista é " , min(lista_covid[5]))


#Criação de dicionário para o estado do Acre

dic_regioes_ac = {'Acrelândia':nova_lista_AC[3][0],'Assis Brasil':nova_lista_AC[3][1],'Brasiléia':nova_lista_AC[3][2],'Bujari':nova_lista_AC[3][3],'Capixaba':nova_lista_AC[3][4],'Cruzeiro do Sul':nova_lista_AC[3][5],'Epitaciolândia':nova_lista_AC[3][6],'Feijó':nova_lista_AC[3][7],'Jordão':nova_lista_AC[3][8],'Mâncio Lima':nova_lista_AC[3][9],'Manoel Urbano':nova_lista_AC[3][10],'Marechal Thaumaturgo':nova_lista_AC[3][11],'Plácido de Castro':nova_lista_AC[3][12],'Porto Walter':nova_lista_AC[3][13],'Rio Branco':nova_lista_AC[3][14],'Rodrigues Alves':nova_lista_AC[3][15],'Santa Rosa do Purus':nova_lista_AC[3][16],'Senador Guiomard':nova_lista_AC[3][17],'Sena Madureira':nova_lista_AC[3][18],'Tarauacá':nova_lista_AC[3][19],'Xapuri':nova_lista_AC[3][20],'Porto Acre':nova_lista_AC[3][21]}

cidade = input("Digite a cidade do Acre que deseja saber a quantidade de casos novos no dia 20/08 \n")

print("A cidade de ", cidade, "possui ", dic_regioes_ac[cidade], "casos novos")


#Extraindo os dados do Teresina/PI
#O município apresenta somente uma região de saúde

regiao_PI = 'Nordeste'
estado_PI=	'PI'
municipio_PI = 	'Teresina'
regiaosaude_PI = 'ENTRE RIOS'
populacao_PI = 864845
casosacumulados_PI = 	22923
casosnovos_PI=	412
obitosacumulados_PI=	845
obitosnovos_PI=	6

lista_teresina = [regiao_PI,estado_PI,municipio_PI,regiaosaude_PI,populacao_PI,casosacumulados_PI, casosnovos_PI, obitosacumulados_PI, obitosnovos_PI]

print("O número de casos novos em Teresina no dia 20/08 na região ", lista_teresina[3], "foi de ", lista_teresina[6])


