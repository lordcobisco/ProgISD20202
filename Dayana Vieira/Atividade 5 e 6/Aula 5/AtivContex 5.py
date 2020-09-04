######################################################################################################
#             ESTE PROGRAMA É REFERENTE AO NÚMERO DE CASOS DE CORONAVIRUS POR REGIÃO                 #
######################################################################################################

import math 
#Lista de estados do Brasil (a)
estados=["Acre ","Amapá","Amazonas","Rondônia","Roraima","Tocantins","Pará","Alagoas ","Bahia","Ceará ","Maranhão","Paraíba","Pernambuco",
"Piauí","Rio Grande do Norte","Sergipe","Rio de Janeiro","São Paulo ","Espírito Santo","Minas Gerais",
"Rio Grande do Sul","Santa Catarina","Paraná","Distrito Federal","Goiás","Mato Grosso","Mato Grosso do Sul"]
populacao=[881935,845731,4144597,1777225,605761,1572866,8602865,3337357,14873064,9132078,7075181,40181127,9557071,3273227,3506853,2298696,
17264943,45919049,4018650,21168791,11377239,7164788,11433957,3015268,7018354,3484466,2778986]
CasosAcumulado=[22605,39703,112263,48232,39665,37856,178375,72938,217115,137408,198202,96223,113183,66315,57720,68313,
194651,702665,100859,175715,98007,121666,1275,138735,102665,74509,37425]
casosnovos=[57,185,351,42,365,867,406,204,1085,555,583,190,225,237,178,316,372,3172,1279,1331,130,786,
1275,2268,1073,1240,589]
obitosAcumulados=[582,617,3505,568,1017,516,5945,1763,4475,3277,8163,2183,7210,1619,2081,1717,14566,26899,2908,4223,
2744,1839,2733,2042,2336,2368,640]
NovosObitos=[6,4,22,0,0,5,5,10,69,13,30,21,22,11,14,12,4,47,33,91,55,42,42,66,14,28,14]
Estado=[estados,populacao,CasosAcumulado,casosnovos,obitosAcumulados,NovosObitos]##LISTA

##TUPLA (A)-Estados
estadosT=("Acre ","Amapá","Amazonas","Rondônia","Roraima","Tocantins","Pará","Alagoas ","Bahia","Ceará ","Maranhão","Paraíba","Pernambuco",
"Piauí","Rio Grande do Norte","Sergipe","Rio de Janeiro","São Paulo ","Espírito Santo","Minas Gerais",
"Rio Grande do Sul","Santa Catarina","Paraná","Distrito Federal","Goiás","Mato Grosso","Mato Grosso do Sul")
populacaoT=(881935,845731,4144597,1777225,605761,1572866,8602865,3337357,14873064,9132078,7075181,40181127,9557071,3273227,3506853,2298696,
17264943,45919049,4018650,21168791,11377239,7164788,11433957,3015268,7018354,3484466,2778986)
CasosAcumuladoT=(22605,39703,112263,48232,39665,37856,178375,72938,217115,137408,198202,96223,113183,66315,57720,68313,
194651,702665,100859,175715,98007,121666,1275,138735,102665,74509,37425)
casosnovosT=(57,185,351,42,365,867,406,204,1085,555,583,190,225,237,178,316,372,3172,1279,1331,130,786,
1275,2268,1073,1240,589)
obitosAcumuladosT=(582,617,3505,568,1017,516,5945,1763,4475,3277,8163,2183,7210,1619,2081,1717,14566,26899,2908,4223,
2744,1839,2733,2042,2336,2368,640)
NovosObitosT=(6,4,22,0,0,5,5,10,69,13,30,21,22,11,14,12,4,47,33,91,55,42,42,66,14,28,14)
EstadoTupla=(estadosT,populacaoT,CasosAcumuladoT,casosnovosT,obitosAcumuladosT,NovosObitosT)##TUPLA

## inserindo o número certo de novos óbitos do estado da Paraíba (d)
x=Estado[5][11]-10
Estado[5].insert(11,x)


##REGIÕES DO NORDESTE 
municipio=["Maceió","Salvador","Fortaleza","São Luis","João Pessoa","Recife","Teresina","Natal",
"Aracaju","Parnamirim"]
regiao=["1 região","SALVADOR","1 região Fortaleza","SÃO LUIS","1 região da Mata Atlantica","RECIFE","Entre rios",
"7 região de saúde-Metropolitana","Aracaju","7 região de saúde-Metropolitana"]
populacaoR=[1018948,2872347,2669342,1101884,809015,1645727,864845,884122,657013,261469]
CasosAcumuladoR=[24909,67994,44971,17658,24597,29718,21803,21458,31777,5408]
casosnovosR=[77,153,41,73,1,57,31,24,180,19]
obitosAcumuladosR=[803,2153,3755,1183,762,2220,826,893,640,136]
NovosObitosR=[3,31,-1,6,6,4,5,6,5,0]
Regioes=[municipio,regiao,populacaoR,CasosAcumuladoR,casosnovosR,obitosAcumuladosR,NovosObitosR]

##TUPLA DAS REGIÕES (a)
municipioT=("Maceió","Salvador","Fortaleza","São Luis","João Pessoa","Recife","Teresina","Natal",
"Aracaju","Parnamirim")
regiaoT=("1 região","SALVADOR","1 região Fortaleza","SÃO LUIS","1 região da Mata Atlantica","RECIFE","Entre rios",
"7 região de saúde-Metropolitana","Aracaju","7 região de saúde-Metropolitana")
populacaoRT=(1018948,2872347,2669342,1101884,809015,1645727,864845,884122,657013,261469)
CasosAcumuladoRT=(24909,67994,44971,17658,24597,29718,21803,21458,31777,5408)
casosnovosRT=(77,153,41,73,1,57,31,24,180,19)
obitosAcumuladosRT=(803,2153,3755,1183,762,2220,826,893,640,136)
NovosObitosRT=(3,31,-1,6,6,4,5,6,5,0)
RegioesT=(municipioT,regiaoT,populacaoRT,CasosAcumuladoRT,casosnovosRT,obitosAcumuladosRT,NovosObitosRT)

#Estado e municipios de AC (f)
EstadoAC=[605761,40183,518,574,6]#LISTA AC
municipioAC=["Acrelândia","Assis Brasil","Brasiléia","Bujari","Capixaba","Cruzeiro do Sul","Feijó","Jordão","Mancio Lima",
"Manoel Urbano","Porto Acre","Rio Branco","Tarauaca","Xapuri","Sena Madureira"]
populacaoAC=[15256,7417,26278,10266,11733,88876, 34780, 8317,18977,9459,18504, 407319,42567,19323,45848 ]
CasosAcumuladoAC=[432,506,1119,367, 247, 3163, 1139, 160, 743,274, 495,10071, 422,1581,979, 1435]
Casos=[283,527,31106,]
casosnovosAC=[31,24,93,23,11,377,57,14,76,30,67,85,59,43]
obitosAcumuladosAC=[9,9,19,6,7, 57,18,1,9,2,2, 15,387,14,13,11]
NovosObitosAC=[1,2,2,2,1,4,2,1,1,1,2,13,2,1,1]
regiaoAC=["Baixo Acre","Alto Acre","Alto Acre","Baixo Acre","Baixo Acre",
"Jurua"," Jurua","Baixo Acre","Baixo Acre","Baixo Acre","Baixo Acre","Baixo Acre","Jurua","Alto Acre", "Baixo Acre"]
municipio.append(municipioAC)
populacaoR.append(populacaoAC)
CasosAcumuladoR.append(CasosAcumuladoAC)
NovosObitosR.append(NovosObitosAC)
AC=[municipioAC,regiaoAC,populacaoAC,CasosAcumuladoAC,casosnovosAC,obitosAcumuladosAC,NovosObitosAC]
##ADD em lista existente (f)
Estado[1].insert(4,EstadoAC[0])
Estado[3].insert(4,EstadoAC[2])
Estado[2].insert(4,EstadoAC[1])
Estado[4].insert(4,EstadoAC[3])
Estado[5].insert(4,EstadoAC[4])
Regioes[0].append(AC[0])
Regioes[1].append(AC[1])
Regioes[2].append(AC[2])
Regioes[3].append(AC[3])
Regioes[4].append(AC[4])
Regioes[5].append(AC[5])
Regioes[6].append(AC[6])

## Remove os dados das regiões 
AC.remove(regiaoAC)

##Soma dos dados do municipio de AC (h)
somaAC=[sum(AC[1]),sum(AC[2]),sum(AC[3]),sum(AC[4]),sum(AC[5])]

##DICIONÁRIO 
Nordeste=["Alagoas ","Bahia","Ceará ","Maranhão","Paraíba","Pernambuco",
"Piauí","Rio Grande do Norte","Sergipe"]
print("***Regiões de saúde***\n")
print("\n0-Maceió/AL\n1-Salvador/BA\n2-Fortaleza/CE\n3-São Luis/MA\n4-João Pessoa/PB\n5-Recife/PE\n6-Teresina/PI\n7-Natal/RN\n8-Aracaju/SE")
dadosCovid={"0":[Nordeste[0],Regioes[0][0],Regioes[4][0]],"1":[Nordeste[1],Regioes[0][1],Regioes[4][1]],"2":[Nordeste[2],Regioes[0][2],Regioes[4][2]],
"3":[Nordeste[3],Regioes[0][3],Regioes[4][3]],"4":[Nordeste[4],Regioes[0][4],Regioes[4][4]],"5":[Nordeste[5],Regioes[0][5],Regioes[4][5]],
"6":[Nordeste[6],Regioes[0][6],Regioes[4][6]],"7":[Nordeste[7],Regioes[0][7],Regioes[4][7]],"8":[Nordeste[8],Regioes[0][8],Regioes[4][8]]}
comando=input('Escolha e aperte o número equivalente à cidade buscada')
print("Município: ",dadosCovid[comando][1],"\nEstado:",dadosCovid[comando][0],"\nCasos Novos: ",dadosCovid[comando][2])

#######################################################################
print("\n############################################################")
print("*******Seja bem vindo ao COVID Saúde Brasil**************")
choice=int(input("Caso você deseje saber sobre como está a Covid 19 por estados aperte 3,\npelas principais regiões de sáude do nordeste aperte 2,e 3 para os municipios do RR: "))
## Aqui pode printar o número de casos acumulados para o estado do rio de janeiro (b)
if(choice==1):
     e1=int(input("\nPara saber os dados por estado aperte 1 e para os obitos acumulado aperte em 2:"))
     if(e1==1): 
           print("***Wiki:estados do Brasil**\n")
           print("\nNORTE:\n0-Acre\n1-Amapá\n2-Amazonas\n3-Rondônia\n4-Roraima\n5-Tocantins\n6-Pará")
           print("\nNORDESTE:\n7-Alagoas\n8-Bahia\n9-Ceará\n10-Maranhão\n11-Paraíba\nPernanbuco\n13-Piauí\n14-Rio Grande do Norte\n15-Sergipe")
           print("\nSUDESTE:\n16-Rio de Janeira\n17-São Paulo\n18-Espírito Santo\n19-Minas Gerais")
           print("\nSUL:\n20-Rio Grande do Sul\n21-Santa Catarina\n22-Paraná")
           print("\nCENTRO-OESTE:\n23-Distrito Federal\n24-Goiás\n25-Mato Grosso\n26-Mato Grosso do Sul")
           opc=int(input("Selecione o número do estado escolhido: "))
           print("\nRESPOSTAS DA LISTA")
           print("\n****",Estado[0][opc],"****\nPopulação:",Estado[1][opc],"\nCasos acumulados:",Estado[2][opc],"\nCasos novos:",Estado[3][opc],"\nObitos acumulados",Estado[4][opc],"\nObitosnovos:",Estado[5][opc])
           print("\nRESPOSTAS RETIRADAS DA TUPLA")
           print("\n****",EstadoTupla[0][opc],"****\nPopulação:",EstadoTupla[1][opc],"\nCasos acumulados:",EstadoTupla[2][opc],"\nCasos novos:",EstadoTupla[3][opc],"\nObitos acumulados",EstadoTupla[4][opc],"\nObitosnovos:",EstadoTupla[5][opc])
    ## Obito acumulado de todos os estados (c)
     else:
           print("***Obito Acumulado por estatos***")
           print(estados[0],":",obitosAcumulados[0],"\n"+estados[1],":",obitosAcumulados[1],"\n"+estados[2],":",obitosAcumulados[2])
           print(estados[3],":",obitosAcumulados[3],"\n"+estados[4],":",obitosAcumulados[4],"\n"+estados[5],":",obitosAcumulados[5])
           print(estados[6],":",obitosAcumulados[6],"\n"+estados[7],":",obitosAcumulados[7],"\n"+estados[8],":",obitosAcumulados[8])
           print(estados[9],":",obitosAcumulados[9],"\n"+estados[10],":",obitosAcumulados[10],"\n"+estados[11],":",obitosAcumulados[11])
           print(estados[14],":",obitosAcumulados[14],"\n"+estados[13],":",obitosAcumulados[13],"\n"+estados[12],":",obitosAcumulados[12])
           print(estados[15],":",obitosAcumulados[15],"\n"+estados[16],":",obitosAcumulados[16],"\n"+estados[17],":",obitosAcumulados[17])
           print(estados[20],":",obitosAcumulados[20],"\n"+estados[19],":",obitosAcumulados[19],"\n"+estados[18],":",obitosAcumulados[18])
           print(estados[21],":",obitosAcumulados[21],"\n"+estados[22],":",obitosAcumulados[22],"\n"+estados[23],":",obitosAcumulados[23])
           print(estados[26],":",obitosAcumulados[26],"\n"+estados[25],":",obitosAcumulados[7],"\n"+estados[24],":",obitosAcumulados[24])
      ## Max e Min dos valores númericos de óbitos novos (j)
           print("Menor valor numérico de óbitos novos:",min(Estado[5]))
           print("Maior valor numérico de óbitos novos:",max(Estado[5]))
           print("***Total:108536***")        
##Imprimindo dados sobre as 10 regiões de Saúde
if(choice==2):
      print("***Wiki: principais regiões de saúde***\n")
      print("\n0-Maceió\n1-Salvador\n2-Fortaleza\n3-São Luis\n4-João Pessoa\n5-Recife\n6-Teresina\n7-Natal\n8-Aracaju\n9-Parnamirim")
      ## Max e Min dos valores númericos de óbitos novos (j)
      print("Menor valor numérico de óbitos novos:",min(Regioes[6]))
      print("Maior valor numérico de óbitos novos:",max(Regioes[6]))
      opc=int(input("Selecione o número do município escolhido: "))
      if(opc!=9):
           print("\n***"+Regioes[0][opc]+"***")
           print(estados[opc+7],"\n*Região de Saúde:",Regioes[1][opc])
           print("População:",Regioes[2][opc],"\nCasos acumulados:",Regioes[3][opc],"\nCasos novos:",Regioes[4][opc],"\nObitos acumulados",Regioes[5][opc],"\nObitosnovos:",Regioes[6][opc])
      else:
           print("\n***"+Regioes[0][opc]+"***")
           print("Rio Grande do Norte","\n*Região de Saúde:",Regioes[1][opc])
           print("População:",Regioes[2][opc],"\nCasos acumulados:",Regioes[3][opc],"\nCasos novos:",Regioes[4][opc],"\nObitos acumulados",Regioes[5][opc],"\nObitosnovos:",Regioes[6][opc])
#Imprimindo os dados do municípios de AC
if(choice==3):
       print("***Bem vindo Covid Saúde AC***\n")
       print("\nRegião de saúde:CENTRO NORTE:\n0-Acrelândia\n1-Assis Brasil\n2-Brasiléia\n3-Bujari\n4-Capixaba\n5-Cruzeiro do Sul\n6-Feijó\n7-Mancio Lima\n8-Manoel Urbano")
       print("\nRegião de saúde:SUL:\n9-Porto Acre\n10-Rio Branco\n11-Tarauaca\n12-Xapuri\n13-Sena Madureira")
      ## Max e Min dos valores númericos de óbitos novos (j)
       print("Menor valor numérico de óbitos novos:",min(AC[6]))
       print("Maior valor numérico de óbitos novos:",max(AC[6]))
       opc=int(input("Selecione o número do município escolhido: "))
       if(opc<9):
           print("\n***"+municipioAC[opc]+"***")
           print("Acre","\n*Região de Saúde: Alto Acre")
           print("População:",populacaoAC[opc],"\nCasos acumulados:",CasosAcumuladoAC[opc],"\nCasos novos:",casosnovosAC[opc],"\nObitos acumulados",obitosAcumuladosAC[opc],"\nObitosnovos:",NovosObitosAC[opc])
       else:
           print("\n***"+municipioAC[opc]+"***")
           print("Acre","\n*Região de Saúde: Baixo Acre")
           print("População:",populacaoAC[opc],"\nCasos acumulados:",CasosAcumuladoAC[opc],"\nCasos novos:",casosnovosAC[opc],"\nObitos acumulados",obitosAcumuladosAC[opc],"\nObitosnovos:",NovosObitosAC[opc]) 

## Se conferir, imprima os resultados (h)
if (somaAC==EstadoAC):
       print("População:",EstadoAC[0],"\nCasos acumulados:",EstadoAC[1],"\nCasos novos:",EstadoAC[2])
       print("\nObitos acumulados",EstadoAC[3],"\nObitosnovos:",EstadoAC[4]) 

