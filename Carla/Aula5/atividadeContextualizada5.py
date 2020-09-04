#Lista
estados = ['Acre','Tocantins','Piauí','Paraíba','Alagoas','Rio de Janeiro','Distrito Federal']
populacao = [881935,1572866,3273227,4018127,3337357,17264943,3015268]
casosAcumulados = [22933,38845,67226,97497,73701,199480,140170]
casosNovos = [328,989,911,1274,763,4829,1435]
obitosAcumulados = [590,531,1637,2203,1774,14728,2097]
obitosNovos = [8, 15,8,20,11,162,55]

print(max(obitosNovos))
print(min(obitosNovos))

print(casosNovos[2])

Lista = [estados,populacao,casosAcumulados,casosNovos,obitosAcumulados,obitosNovos]
#Regiões de saúde
municipios = ['Acrelândia','Assis Brasil','Abreulândia','Aguiarnópolis','Acauã','Teresina','Água Branca', 'Aguiar','Água Branca','Anadia','Angra dos Reis','Aperibé','Brasília',]
regiaoDeSaude = ['BAIXO ACRE E PURUS','ALTO ACRE','CANTAO','BICO DO PAPAGAIO','VALE DO RIO GUARIBAS','ENTRE RIOS','11ª REGIAO','7ª REGIAO','10ª REGIAO DE SAUDE','5ª REGIAO DE SAUDE','BAIA DA ILHA GRANDE','NOROESTE','DISTRITO FEDERAL']
populacaoRs = [15256,7417,2579,6733,7084,864845,10234,5640,20196,17545,203785,11759,3015268]
CasosAcumuladosRs = [398,440,28,356,24,	22102,52,24,69,426,4379,167,140170]
casosNovosRs = [20,1,6,3,0,299,0,0,0,1,92,0,1435]
obitosAcumuladosRs = [8,9,2,6,0,833,2,0,2,6,137,6,2097]
obitosNovos = [0,0,0,0,0,7,0,0,0,0,6,0,55]
ListaRegioesdeSaude = [municipios,regiaoDeSaude,populacaoRs,CasosAcumuladosRs,casosNovosRs,obitosAcumuladosRs,obitosNovos]

print(max(obitosNovos))
print(min(obitosNovos))

Lista.append(ListaRegioesdeSaude)


if'Rio de Janeiro' in Lista [0]:
    print(' O número de óbitos acumulados no Rio de Janeiro é?',Lista[5][6])

print (Lista[0][0], Lista[5][0])
print (Lista[0][1], Lista[5][1])
print (Lista[0][2], Lista[5][2])
print (Lista[0][3], Lista[5][3])
print (Lista[0][4], Lista[5][4])
print (Lista[0][5], Lista[5][5])
print (Lista[0][6], Lista[5][6])

if 'Paraíba' in Lista[0]:
    Lista[5][5] = Lista[5][4] + 10
    print(Lista)

#tupla
estados = ('Acre','Tocantins','Piauí','Paraíba','Alagoas','Rio de Janeiro','Distrito Federal')
populacao = (881935,1572866,3273227,4018127,3337357,17264943,3015268)
casosAcumulados = (22933,38845,67226,97497,73701,199480,140170)
casosNovos = (328,989,911,1274,763,4829,1435)
obitosAcumulados = (590,531,1637,2203,1774,14728,2097)
obitosNovos = (8, 15,8,20,11,162,55)

Tupla = (estados,populacao,casosAcumulados,casosNovos,obitosAcumulados,obitosNovos)
#Regiões de saúde
municipios = ('Acrelândia','Assis Brasil','Abreulândia','Aguiarnópolis','Acauã','Teresina','Água Branca', 'Aguiar','Água Branca','Anadia','Angra dos Reis','Aperibé','Brasília')
regiaoDeSaude = ('BAIXO ACRE E PURUS','ALTO ACRE','CANTAO','BICO DO PAPAGAIO','VALE DO RIO GUARIBAS','ENTRE RIOS','11ª REGIAO','7ª REGIAO','10ª REGIAO DE SAUDE','5ª REGIAO DE SAUDE','BAIA DA ILHA GRANDE','NOROESTE','DISTRITO FEDERAL')
populacaoRs = (15256,7417,2579,6733,7084,864845,10234,5640,20196,17545,203785,11759,3015268)
CasosAcumuladosRs = (398,440,28,356,24,	22102,52,24,69,426,4379,167,140170)
casosNovosRs = (20,1,6,3,0,299,0,0,0,1,92,0,1435)
obitosAcumuladosRs = (8,9,2,6,0,833,2,0,2,6,137,6,2097)
obitosNovos = (0,0,0,0,0,7,0,0,0,0,6,0,55)
TuplaRegioesdeSaude = (municipios,regiaoDeSaude,populacaoRs,CasosAcumuladosRs,casosNovosRs,obitosAcumuladosRs,obitosNovos)


#Não é possível fazer alterações na tupla, pois ela não sai de sua conformação original.

#Lista com dados do estado do Acre

acMunicipios = ['Acrelândia','Assis Brasil','Brasiléia''Bujari','Capixaba','Cruzeiro do Sul','Epitaciolândia','Feijó','Jordão','Mâncio Lima','Manoel Urbano','Marechal Thaumaturgo','Plácido de Castro','Porto Walter','Rio Branco','Rodrigues Alves','Santa Rosa do Purus','Senador Guiomard','Sena Madureira','Tarauacá','Xapuri','Porto Acre']
populacaoAc = [15256,7417,26278,10266,11733,88376,18411,34780,8317,18977,9459,18867,19761,11982,407319,18930,6540,23024,45848,42567,19323,18504]
casosAcumuladosAc = [398,440,1035,353,240,2961,456,968,119,553,253,287,386,240,9692,137,201,401,1267,1401,685,460]
casosNovosAc = [20,1,93,1,1,19,15,6,4,0,2,3,0,0,30,0,2,2,17,85,27,0]
obitosAcumuladosAc = [8,9,15,6,7,53,11,16,1,8,2,1,8,2,377,6,2,10,10,13,11,14]
obitosNovsAc = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,1,0] 
listaAc = [acMunicipios,populacaoAc,casosAcumuladosAc,casosNovosAc,obitosAcumuladosAc,obitosNovsAc]
Lista.append(listaAc)
print(Lista)

print(max(obitosNovsAc))
print(min(obitosNovsAc))
Lista.remove(ListaRegioesdeSaude)

##Soma dos dados do municipio de AC no dia 18/08/2020 
print(sum(populacaoAc))
print(sum(casosAcumuladosAc))
print(sum(casosNovosAc))
print(sum(obitosAcumuladosAc))
print(sum(obitosNovsAc))

print('Somatorio igual')

print("Tamanho da lista de estados:",len(Lista))
print("Tamanho da lista de regiões de saude:",len(ListaRegioesdeSaude))
print("Tamanho da lista dos dados de Acre em 18/08:",len(listaAc))


##DICIONÁRIO 
Ac = {"Municipios Acre":['Acrelândia','Assis Brasil','Brasiléia''Bujari','Capixaba','Cruzeiro do Sul','Epitaciolândia','Feijó','Jordão','Mâncio Lima','Manoel Urbano','Marechal Thaumaturgo','Plácido de Castro','Porto Walter','Rio Branco','Rodrigues Alves','Santa Rosa do Purus','Senador Guiomard','Sena Madureira','Tarauacá','Xapuri','Porto Acre']}
