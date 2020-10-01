############# CAROLINA KARLA DE SOUZA EVANGELISTA ##############
####################### MATRICULA 202002003 ####################
################ EXERCICIO CONTEXTUALIZADO 5 ###################

## listas
estados = ['Rondonia','Acre','Roraima','Tocantins','Piaui','Rio Grande do Norte','Paraiba','Pernambuco','Sergipe', 'Rio de Janeiro' ]
populacao = [1777225,881935,605761,1572866,3273227,3506853,4018127,9557071,2298696,17264943]
casosAC = [48923,22933,40183,38845,67226,58307,97497,113788,68699,199480]
obitosAC = [1026,590,574,531,1637,2102,2203,7252,1729,14728]
casosN = [691,328,518,989,911,409,1274,605,386,4829]
obitosN = [9,8,6,15,18,21,20,42,12,162]
regioessaude = ['ZONA DA MATA','VALE DO JAMARI','BAIXO ACRE E PURUS','ALTO ACRE','CENTRO NORTE','SUL','CANTAO','BICO DO PAPAGAIO','VALE DO RIO GUARIBAS','ENTRE RIOS','CAICO','ACU','1 REGIÃO','3 REGIÃO','PETROLINA','CARUARU','ARACAJU','ESTANCIA']

## tuplas
Testados = ("Rondonia", "Acre", "Roraima", "Tocantins","Piaui", "Rio Grande do Norte", "Paraiba", "Pernambuco", "Sergipe", "Rio de Janeiro")
Tpopulacao = (1777225,881935,605761,1572866,3273227,3506853,4018127,9557071,2298696,17264943)
TcasosAC = (48923,22933,40183,38845,67226,58307,97497,113788,68699,199480)
TobitosAC = (1026,590,574,531,1637,2102,2203,7252,1729,14728)
TcasosN = (691,328,518,989,911,409,1274,605,386,4829)
TobitosN = (9,8,6,15,18,21,20,42,12,162)
Tregioessaude = ("ZONA DA MATA","VALE DO JAMARI","BAIXO ACRE E PURUS","ALTO ACRE","CENTRO NORTE","SUL","CANTAO","BICO DO PAPAGAIO","VALE DO RIO GUARIBAS","ENTRE RIOS","CAICO","ACU","1ª REGIÃO","3ª REGIÃO","PETROLINA","CARUARU","ARACAJU","ESTANCIA")

listaCOV = [estados, populacao, casosAC, obitosAC, casosN, obitosN, regioessaude]
print(listaCOV)

tuplaCOV = (Testados, Tpopulacao, TcasosAC, TobitosAC, TcasosN, TobitosN, Tregioessaude)
print(tuplaCOV)

### LETRA B DO EXERCICIO ###
if 'Rio de Janeiro' in listaCOV[0]:
    print("O número casos acumulados para o estado do RJ:", listaCOV[2][9])

### LETRA C DO EXERCICIO ###
print("O numero de obitos acumulados para cada estado é:")
print(listaCOV[0][0], listaCOV[3][0])
print(listaCOV[0][1], listaCOV[3][1])
print(listaCOV[0][2], listaCOV[3][2])
print(listaCOV[0][3], listaCOV[3][3])
print(listaCOV[0][4], listaCOV[3][4])
print(listaCOV[0][5], listaCOV[3][5])
print(listaCOV[0][6], listaCOV[3][6])
print(listaCOV[0][7], listaCOV[3][7])
print(listaCOV[0][8], listaCOV[3][8])
print(listaCOV[0][9], listaCOV[3][9])


### LETRA D DO EXERCICIO ###
if 'Paraiba' in listaCOV[0]:
    listaCOV[3][6] = listaCOV[3][6] + 10
    print("Este é o valor correto de obitos na paraiba")
    print(listaCOV)

### LETRA E DO EXERCICIO ###

'''
Não é possivel manipular os dados utilizando uma tupla, apenas com as listas, por isso a operação não foi possivel

'''
### LETRA F DO EXERCICIO ###
cidadesAC = ['Acrelandia', 'Assis Brasil','Brasiléia','Bujari','Capixaba','Cruzeiro do Sul','Epitaciolândia','Feijó','Jordão','Mâncio Lima','Manoel Urbano','Marechal Thaumaturgo','Plácido de Castro','Porto Walter','Rio Branco','Rodrigues Alves','Santa Rosa do Purus','Senador Guiomard','Sena Madureira','Tarauacá', 'Xapuri', 'Porto Acre']
populacaoAC = [7417,26278,10266,11733,88376,18411,34780,8317,18977,9459,18867,19761,11982,407319,18930,6540,23024,45848,42567,19323,18504]
casosAC_AC = [398,440,1035,353,240,2961,456,968,119,553,253,287,386,240,9692,137,201,401,1267,1401,685,460]
obitosAC_AC = [8,9,15,6,7,53,11,16,1,8,2,1,8,2,377,6,2,10,10,13,11,14]
casosN_AC = [20,1,93,1,1,19,15,6,4,0,2,3,0,0,30,0,2,2,17,85,27,0]
obitosN_AC = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,1,0]
regioesAC = ['BAIXO ACRE E PURUS', 'ALTO ACRE','ALTO ACRE','BAIXO ACRE E PURUS','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','ALTO ACRE','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','BAIXO ACRE E PURUS','BAIXO ACRE E PURUS','BAIXO ACRE E PURUS','JURUA E TARAUACA/ENVIRA','ALTO ACRE','BAIXO ACRE E PURUS']


listaCOV2 = [cidadesAC, populacaoAC, casosAC_AC, obitosAC_AC, casosN_AC, obitosN_AC,regioesAC]
print(listaCOV2)

### adicionando a nova lista (LETRA F) ###
listaCOV.append(listaCOV2)
print(listaCOV)

### LETRA G DO EXERCICIO ###
listaCOV2.remove(regioesAC)
print(listaCOV)

### LETRA H DO EXERCICIO ###
soma = [sum(listaCOV2[1]),sum(listaCOV2[2]),sum(listaCOV2[3]), sum(listaCOV2[4]), sum(listaCOV2[5])]

if(soma[0] == listaCOV[1][1]):
    if(soma[1] == listaCOV[2][1]):
        if(soma[2] == listaCOV[3][1]):
            if(soma[3] == listaCOV[4][1]):
                if(soma[4] == listaCOV[5][1]):
                    print(True)
else:
    print("Dados não batem") ## não consegui fazer as somas baterem, entao coloquei um else ###


#### LETRA J DO EXERCICIO ##

print("Menor e maior valor de óbitos novos")
minimoOBN = min(listaCOV[5])
maximoOBN = max(listaCOV[5])
print("Menor:", minimoOBN, "\nMaior", maximoOBN)

### LETRA L DO EXERCICIO ###

if 'Piaui' in listaCOV[0]:
    print(listaCOV[4][4])
    print("Estes são os casos novos no Piaui")

    ##### Não consegui carregar todos os dados, o excel travava cada vez que eu ia abrir o arquivo .cvs ####
    #### Espero que compreenda ####
