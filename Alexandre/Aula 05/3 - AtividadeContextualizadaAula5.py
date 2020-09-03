
######## ALTERNATIVA A ####### - Realize o download dos dados de forma manual e crie uma lista e uma tupla com as informações disponíveis no documento csv 

#LISTA estados_lista (Dados pegos da tabela no dia 31/08/20)

    #Organização dos dados dos estados em listas - Informações na mesma posição correspondem ao mesmo estado. Por exemplo: Acre está na posição zero, logo, casos_acumulado_lista_estados_lista na posiçáo zero corresponde ao Acre

estados_lista =["Acre (AC)","Alagoas(AL)","Amazonas (AM)","Amapá (AP)","Bahia(BA)","Ceará(CE)","Distrito federal(DF)","Espírito santos (ES)","Goiás (G0)","Maranhão (MA)","Minas gerais (MG)","Mato gosso do sul (MS)","Mato grosso (MT)",
"Pará (PA)","Paraiba (PB)","Pernambuco (PE)","Piauí (PI)","Paraná (PR)","Rio de Janeiro (RJ)","Rio grande do norte (RN)","Rondônia (RO)","Roraíma (RR)","Rio Grande do Sul (RS)","Santa Catarina (SC)","Sergipe (SE)",
"São paulo (SP)","Tocantins (TO)"]
populacao_TCU_2019_lista_estado=[881935,3337357,4144597,845731,14873064,9132078,3015268,4018650,7018354,7075181,21168791,2778986,3484466,8602865,4018127,9557071,3273227,11433957,17264943,3506853,1777225,605761,11377239,7164788,2298696,45919049,1572866]
casos_acumulado_lista_estado=[24647,78804,120296,43193,256727,214953,162042,111261,132506,151615,216557,48937,91346,199556,105778,125539,77405,131906,223631,61748,55153,43518,125813,177777,72528,804342,50694]
casos_novos_lista_estado =[9,167,236,301,665,496,1246,910,1643,403,1507,415,1009,385,117,445,140,1303,329,99,474,48,1331,30913,111,938,321]
obitos_acumulados_lista_estado=[612,1887,3649,661,5397,8409,2521,3158,3094,3446,5335,862,2751,6146,2450,7593,1825,3290,16065,2256,1148,587,3435,2260,1857,30014,673]
obitos_novos_lista_estado=[3,9,10,1,53,25,52,23,19,10,9,11,26,31,15,19,10,39,38,8,19,0,40,25,13,36,9]

    #LISTAS organizados por estado - Informação dada na sequência: (1)Estado, (2) população do estado,(3) Casos acumulados,(4) casos novos,(5) óbitos acumulados e (6) óbitos novos
Acre_lista = [estados_lista[0],populacao_TCU_2019_lista_estado[0],casos_acumulado_lista_estado[0],casos_novos_lista_estado[0],obitos_acumulados_lista_estado[0],obitos_novos_lista_estado[0]]
Alagoas_lista = [estados_lista[1],populacao_TCU_2019_lista_estado[1],casos_acumulado_lista_estado[1],casos_novos_lista_estado[1],obitos_acumulados_lista_estado[1],obitos_novos_lista_estado[1]]
Amazonas_lista = [estados_lista[2],populacao_TCU_2019_lista_estado[2],casos_acumulado_lista_estado[2],casos_novos_lista_estado[2],obitos_acumulados_lista_estado[2],obitos_novos_lista_estado[2]]
Amapá_lista = [estados_lista[3],populacao_TCU_2019_lista_estado[3],casos_acumulado_lista_estado[3],casos_novos_lista_estado[3],obitos_acumulados_lista_estado[3],obitos_novos_lista_estado[3]]
Bahia_lista = [estados_lista[4],populacao_TCU_2019_lista_estado[4],casos_acumulado_lista_estado[4],casos_novos_lista_estado[4],obitos_acumulados_lista_estado[4],obitos_novos_lista_estado[4]]
Ceará_lista = [estados_lista[5],populacao_TCU_2019_lista_estado[5],casos_acumulado_lista_estado[5],casos_novos_lista_estado[5],obitos_acumulados_lista_estado[5],obitos_novos_lista_estado[5]]
Distrito_federal_lista = [estados_lista[6],populacao_TCU_2019_lista_estado[6],casos_acumulado_lista_estado[6],casos_novos_lista_estado[6],obitos_acumulados_lista_estado[6],obitos_novos_lista_estado[6]]
Espirito_santo_lista = [estados_lista[7],populacao_TCU_2019_lista_estado[7],casos_acumulado_lista_estado[7],casos_novos_lista_estado[7],obitos_acumulados_lista_estado[7],obitos_novos_lista_estado[7]]
Goias_lista = [estados_lista[8],populacao_TCU_2019_lista_estado[8],casos_acumulado_lista_estado[8],casos_novos_lista_estado[8],obitos_acumulados_lista_estado[8],obitos_novos_lista_estado[8]]
Maranhao_lista = [estados_lista[9],populacao_TCU_2019_lista_estado[9],casos_acumulado_lista_estado[9],casos_novos_lista_estado[9],obitos_acumulados_lista_estado[9],obitos_novos_lista_estado[9]]
Minas_gerais_lista = [estados_lista[10],populacao_TCU_2019_lista_estado[10],casos_acumulado_lista_estado[10],casos_novos_lista_estado[10],obitos_acumulados_lista_estado[10],obitos_novos_lista_estado[10]]
Mato_grosso_sul_lista = [estados_lista[11],populacao_TCU_2019_lista_estado[11],casos_acumulado_lista_estado[11],casos_novos_lista_estado[11],obitos_acumulados_lista_estado[11],obitos_novos_lista_estado[11]]
Mato_grosso_lista = [estados_lista[12],populacao_TCU_2019_lista_estado[12],casos_acumulado_lista_estado[12],casos_novos_lista_estado[12],obitos_acumulados_lista_estado[12],obitos_novos_lista_estado[12]]
Para_lista = [estados_lista[13],populacao_TCU_2019_lista_estado[13],casos_acumulado_lista_estado[13],casos_novos_lista_estado[13],obitos_acumulados_lista_estado[13],obitos_novos_lista_estado[13]]
Paraiba_lista = [estados_lista[14],populacao_TCU_2019_lista_estado[14],casos_acumulado_lista_estado[14],casos_novos_lista_estado[14],obitos_acumulados_lista_estado[14],obitos_novos_lista_estado[14]]
Pernambuco_lista = [estados_lista[15],populacao_TCU_2019_lista_estado[15],casos_acumulado_lista_estado[15],casos_novos_lista_estado[15],obitos_acumulados_lista_estado[15],obitos_novos_lista_estado[15]]
Piaui_lista= [estados_lista[16],populacao_TCU_2019_lista_estado[16],casos_acumulado_lista_estado[16],casos_novos_lista_estado[16],obitos_acumulados_lista_estado[16],obitos_novos_lista_estado[16]]
Parana_lista = [estados_lista[17],populacao_TCU_2019_lista_estado[17],casos_acumulado_lista_estado[17],casos_novos_lista_estado[17],obitos_acumulados_lista_estado[17],obitos_novos_lista_estado[17]]
Rio_de_janeiro_lista= [estados_lista[18],populacao_TCU_2019_lista_estado[18],casos_acumulado_lista_estado[18],casos_novos_lista_estado[18],obitos_acumulados_lista_estado[18],obitos_novos_lista_estado[18]]
Rio_grande_norte_lista = [estados_lista[19],populacao_TCU_2019_lista_estado[19],casos_acumulado_lista_estado[19],casos_novos_lista_estado[19],obitos_acumulados_lista_estado[19],obitos_novos_lista_estado[19]]
Rondonia_lista = [estados_lista[20],populacao_TCU_2019_lista_estado[20],casos_acumulado_lista_estado[20],casos_novos_lista_estado[20],obitos_acumulados_lista_estado[20],obitos_novos_lista_estado[20]]
Roraima_lista = [estados_lista[21],populacao_TCU_2019_lista_estado[21],casos_acumulado_lista_estado[21],casos_novos_lista_estado[21],obitos_acumulados_lista_estado[21],obitos_novos_lista_estado[21]]
Rio_grande_sul_lista = [estados_lista[22],populacao_TCU_2019_lista_estado[22],casos_acumulado_lista_estado[22],casos_novos_lista_estado[22],obitos_acumulados_lista_estado[22],obitos_novos_lista_estado[22]]
Santa_catarina_lista = [estados_lista[23],populacao_TCU_2019_lista_estado[23],casos_acumulado_lista_estado[23],casos_novos_lista_estado[23],obitos_acumulados_lista_estado[23],obitos_novos_lista_estado[23]]
Sergipe_lista = [estados_lista[24],populacao_TCU_2019_lista_estado[24],casos_acumulado_lista_estado[24],casos_novos_lista_estado[24],obitos_acumulados_lista_estado[24],obitos_novos_lista_estado[24]]
Sao_paulo_lista = [estados_lista[25],populacao_TCU_2019_lista_estado[25],casos_acumulado_lista_estado[25],casos_novos_lista_estado[25],obitos_acumulados_lista_estado[25],obitos_novos_lista_estado[25]]
Tocantins_lista = [estados_lista[26],populacao_TCU_2019_lista_estado[26],casos_acumulado_lista_estado[26],casos_novos_lista_estado[26],obitos_acumulados_lista_estado[26],obitos_novos_lista_estado[26]]

# TUPLA estados_lista (Dados pegos da tabela no dia 31/08/20)

        #Organização dos dados dos estados_lista em Tupla - Informações na mesma posição correspondem ao mesmo estado. Por exemplo: Acre está na posição zero, logo, casos_acumulado_lista_estados_lista na posiçáo zero corresponde ao Acre

estados_tupla=("Acre (AC)","Alagoas(AL)","Amazonas (AM)","Amapá (AP)","Bahia(BA)","Ceará(CE)","Distrito federal(DF)","Espírito santos (ES)","Goiás (G0)","Maranhão (MA)","Minas gerais (MG)","Mato gosso do sul (MS)","Mato grosso (MT)",
"Pará (PA)","Paraiba (PB)","Pernambuco (PE)","Piauí (PI)","Paraná (PR)","Rio de Janeiro (RJ)","Rio grande do norte (RN)","Rondônia (RO)","Roraíma (RR)","Rio Grande do Sul (RS)","Santa Catarina (SC)","Sergipe (SE)",
"São paulo (SP)","Tocantins (TO)")
populacao_TCU_2019_tupla_estado =(881935,3337357,4144597,845731,14873064,9132078,3015268,4018650,7018354,7075181,21168791,2778986,3484466,8602865,4018127,9557071,3273227,11433957,17264943,3506853,1777225,605761,11377239,7164788,2298696,45919049,1572866)
casos_acumulado_tupla_estado=(24647,78804,120296,43193,256727,214953,162042,111261,132506,151615,216557,48937,91346,199556,105778,125539,77405,131906,223631,61748,55153,43518,125813,177777,72528,804342,50694)
casos_novos_tupla_estado=(9,167,236,301,665,496,1246,910,1643,403,1507,415,1009,385,117,445,140,1303,329,99,474,48,1331,30913,111,938,321)
obitos_acumulados_tupla_estado=(612,1887,3649,661,5397,8409,2521,3158,3094,3446,5335,862,2751,6146,2450,7593,1825,3290,16065,2256,1148,587,3435,2260,1857,30014,673)
obitos_novos_tupla_estado=(3,9,10,1,53,25,52,23,19,10,9,11,26,31,15,19,10,39,38,8,19,0,40,25,13,36,9)

    #TUPLAS organizados por estado - Informação dada na sequência: (1)Estado, (2) população do estado,(3) Casos acumulados,(4) casos novos,(5) óbitos acumulados e (6) óbitos novos
Acre_tupla = (estados_tupla[0],populacao_TCU_2019_tupla_estado[0],casos_acumulado_tupla_estado[0],casos_novos_tupla_estado[0],obitos_acumulados_tupla_estado[0],obitos_novos_tupla_estado[0])
Alagoas_tupla = (estados_tupla[1],populacao_TCU_2019_tupla_estado[1],casos_acumulado_tupla_estado[1],casos_novos_tupla_estado[1],obitos_acumulados_tupla_estado[1],obitos_novos_tupla_estado[1])
Amazonas_tupla = (estados_tupla[2],populacao_TCU_2019_tupla_estado[2],casos_acumulado_tupla_estado[2],casos_novos_tupla_estado[2],obitos_acumulados_tupla_estado[2],obitos_novos_tupla_estado[2])
Amapá_tupla = (estados_tupla[3],populacao_TCU_2019_tupla_estado[3],casos_acumulado_tupla_estado[3],casos_novos_tupla_estado[3],obitos_acumulados_tupla_estado[3],obitos_novos_tupla_estado[3])
Bahia_tupla = (estados_tupla[4],populacao_TCU_2019_tupla_estado[4],casos_acumulado_tupla_estado[4],casos_novos_tupla_estado[4],obitos_acumulados_tupla_estado[4],obitos_novos_tupla_estado[4])
Ceará_tupla = (estados_tupla[5],populacao_TCU_2019_tupla_estado[5],casos_acumulado_tupla_estado[5],casos_novos_tupla_estado[5],obitos_acumulados_tupla_estado[5],obitos_novos_tupla_estado[5])
Distrito_federal_tupla = (estados_tupla[6],populacao_TCU_2019_tupla_estado[6],casos_acumulado_tupla_estado[6],casos_novos_tupla_estado[6],obitos_acumulados_tupla_estado[6],obitos_novos_tupla_estado[6])
Espirito_santo_tupla = (estados_tupla[7],populacao_TCU_2019_tupla_estado[7],casos_acumulado_tupla_estado[7],casos_novos_tupla_estado[7],obitos_acumulados_tupla_estado[7],obitos_novos_tupla_estado[7])
Goias_tupla = (estados_tupla[8],populacao_TCU_2019_tupla_estado[8],casos_acumulado_tupla_estado[8],casos_novos_tupla_estado[8],obitos_acumulados_tupla_estado[8],obitos_novos_tupla_estado[8])
Maranhao_tupla = (estados_tupla[9],populacao_TCU_2019_tupla_estado[9],casos_acumulado_tupla_estado[9],casos_novos_tupla_estado[9],obitos_acumulados_tupla_estado[9],obitos_novos_tupla_estado[9])
Minas_gerais_tupla = (estados_tupla[10],populacao_TCU_2019_tupla_estado[10],casos_acumulado_tupla_estado[10],casos_novos_tupla_estado[10],obitos_acumulados_tupla_estado[10],obitos_novos_tupla_estado[10])
Mato_grosso_sul_tupla = (estados_tupla[11],populacao_TCU_2019_tupla_estado[11],casos_acumulado_tupla_estado[11],casos_novos_tupla_estado[11],obitos_acumulados_tupla_estado[11],obitos_novos_tupla_estado[11])
Mato_grosso_tupla = (estados_tupla[12],populacao_TCU_2019_tupla_estado[12],casos_acumulado_tupla_estado[12],casos_novos_tupla_estado[12],obitos_acumulados_tupla_estado[12],obitos_novos_tupla_estado[12])
Para_tupla = (estados_tupla[13],populacao_TCU_2019_tupla_estado[13],casos_acumulado_tupla_estado[13],casos_novos_tupla_estado[13],obitos_acumulados_tupla_estado[13],obitos_novos_tupla_estado[13])
Paraiba_tupla = (estados_tupla[14],populacao_TCU_2019_tupla_estado[14],casos_acumulado_tupla_estado[14],casos_novos_tupla_estado[14],obitos_acumulados_tupla_estado[14],obitos_novos_tupla_estado[14])
Pernambuco_tupla = (estados_tupla[15],populacao_TCU_2019_tupla_estado[15],casos_acumulado_tupla_estado[15],casos_novos_tupla_estado[15],obitos_acumulados_tupla_estado[15],obitos_novos_tupla_estado[15])
Piaui_tupla = (estados_tupla[16],populacao_TCU_2019_tupla_estado[16],casos_acumulado_tupla_estado[16],casos_novos_tupla_estado[16],obitos_acumulados_tupla_estado[16],obitos_novos_tupla_estado[16])
Parana_tupla = (estados_tupla[17],populacao_TCU_2019_tupla_estado[17],casos_acumulado_tupla_estado[17],casos_novos_tupla_estado[17],obitos_acumulados_tupla_estado[17],obitos_novos_tupla_estado[17])
Rio_de_janeiro_tupla = (estados_tupla[18],populacao_TCU_2019_tupla_estado[18],casos_acumulado_tupla_estado[18],casos_novos_tupla_estado[18],obitos_acumulados_tupla_estado[18],obitos_novos_tupla_estado[18])
Rio_grande_norte_tupla = (estados_tupla[19],populacao_TCU_2019_tupla_estado[19],casos_acumulado_tupla_estado[19],casos_novos_tupla_estado[19],obitos_acumulados_tupla_estado[19],obitos_novos_tupla_estado[19])
Rondonia_tupla = (estados_tupla[20],populacao_TCU_2019_tupla_estado[20],casos_acumulado_tupla_estado[20],casos_novos_tupla_estado[20],obitos_acumulados_tupla_estado[20],obitos_novos_tupla_estado[20])
Roraima_tupla = (estados_tupla[21],populacao_TCU_2019_tupla_estado[21],casos_acumulado_tupla_estado[21],casos_novos_tupla_estado[21],obitos_acumulados_tupla_estado[21],obitos_novos_tupla_estado[21])
Rio_grande_sul_tupla = (estados_tupla[22],populacao_TCU_2019_tupla_estado[22],casos_acumulado_tupla_estado[22],casos_novos_tupla_estado[22],obitos_acumulados_tupla_estado[22],obitos_novos_tupla_estado[22])
Santa_catarina_tupla = (estados_tupla[23],populacao_TCU_2019_tupla_estado[23],casos_acumulado_tupla_estado[23],casos_novos_tupla_estado[23],obitos_acumulados_tupla_estado[23],obitos_novos_tupla_estado[23])
Sergipe_tupla = (estados_tupla[24],populacao_TCU_2019_tupla_estado[24],casos_acumulado_tupla_estado[24],casos_novos_tupla_estado[24],obitos_acumulados_tupla_estado[24],obitos_novos_tupla_estado[24])
Sao_paulo_tupla = (estados_tupla[25],populacao_TCU_2019_tupla_estado[25],casos_acumulado_tupla_estado[25],casos_novos_tupla_estado[25],obitos_acumulados_tupla_estado[25],obitos_novos_tupla_estado[25])
Tocantins_tupla = (estados_tupla[26],populacao_TCU_2019_tupla_estado[26],casos_acumulado_tupla_estado[26],casos_novos_tupla_estado[26],obitos_acumulados_tupla_estado[26],obitos_novos_tupla_estado[26])


#LISTA REGIÕES DE SAÚDE (Dados pegos da tabela no dia 31/08/20)
        #Organização dos dados das regiões de saúde em lista - Informações na mesma posição correspondem a mesma região de saúde. 
regioes_saude_lista = ["Vale do Jamari(RO - Código 11001)","Cafe (RO - Código 11002)", "Central(RO - Código 11003)","Madeira-mármore(RO - Código 11004)","Zona da mata(RO - Código 11005)",
"Cone sul(RO - Código 11006)","Vale do guapore (RO - Código 11007)","Alto acre (AC - Código 12001)","Baixo Acre e purus (AC - Código 12002)","Jurua e tarauaca/envira (AC - Código 12003)"]
populacao_TCU_2019_lista_regioes_saude =[107863,85359,128969,529544,55058,99854,18331,26278,407319,88376]
casos_acumulado_lista_regioes_saude =[4483,1682,2068,26868,1229,2799,207,1113,9987,3132]
casos_novos_lista_regioes_saude =[15,1,37,124,1,32,18,4,4,0]
obitos_acumulados_lista_regioes_saude =[76,27,45,646,16,40,4,17,384,55]
obitos_novos_lista_regioes_saude =[1,4,3,4,0,1,1,0,1,1]


        #LISTAS organizados por regiões de saúde - Informação dada na sequência: (1)Estado, (2) população do estado,(3) Casos acumulados,(4) casos novos,(5) óbitos acumulados e (6) óbitos novos
Vale_do_jamari_lista =[regioes_saude_lista[0],populacao_TCU_2019_lista_regioes_saude[0],casos_acumulado_lista_regioes_saude[0],casos_novos_lista_regioes_saude[0],obitos_acumulados_lista_regioes_saude[0],obitos_novos_lista_regioes_saude[0]]
Cafe_lista = [regioes_saude_lista[1],populacao_TCU_2019_lista_regioes_saude[1],casos_acumulado_lista_regioes_saude[1],casos_novos_lista_regioes_saude[1],obitos_acumulados_lista_regioes_saude[1],obitos_novos_lista_regioes_saude[1]]
Central_lista = [regioes_saude_lista[2],populacao_TCU_2019_lista_regioes_saude[2],casos_acumulado_lista_regioes_saude[2],casos_novos_lista_regioes_saude[2],obitos_acumulados_lista_regioes_saude[2],obitos_novos_lista_regioes_saude[2]]
Madeira_marmore_lista = [regioes_saude_lista[3],populacao_TCU_2019_lista_regioes_saude[3],casos_acumulado_lista_regioes_saude[3],casos_novos_lista_regioes_saude[3],obitos_acumulados_lista_regioes_saude[3],obitos_novos_lista_regioes_saude[3]]
Zona_da_mata_lista = [regioes_saude_lista[4],populacao_TCU_2019_lista_regioes_saude[4],casos_acumulado_lista_regioes_saude[4],casos_novos_lista_regioes_saude[4],obitos_acumulados_lista_regioes_saude[4],obitos_novos_lista_regioes_saude[4]]
Cone_sul_lista = [regioes_saude_lista[5],populacao_TCU_2019_lista_regioes_saude[5],casos_acumulado_lista_regioes_saude[5],casos_novos_lista_regioes_saude[5],obitos_acumulados_lista_regioes_saude[5],obitos_novos_lista_regioes_saude[5]]
Vale_do_guapode_lista = [regioes_saude_lista[6],populacao_TCU_2019_lista_regioes_saude[6],casos_acumulado_lista_regioes_saude[6],casos_novos_lista_regioes_saude[6],obitos_acumulados_lista_regioes_saude[6],obitos_novos_lista_regioes_saude[6]]
Alto_acre_lista = [regioes_saude_lista[7],populacao_TCU_2019_lista_regioes_saude[7],casos_acumulado_lista_regioes_saude[7],casos_novos_lista_regioes_saude[7],obitos_acumulados_lista_regioes_saude[7],obitos_novos_lista_regioes_saude[7]]
Baixo_acre_purus_lista = [regioes_saude_lista[8],populacao_TCU_2019_lista_regioes_saude[8],casos_acumulado_lista_regioes_saude[8],casos_novos_lista_regioes_saude[8],obitos_acumulados_lista_regioes_saude[8],obitos_novos_lista_regioes_saude[8]]
Jurua_tarauaca_lista = [regioes_saude_lista[9],populacao_TCU_2019_lista_regioes_saude[9],casos_acumulado_lista_regioes_saude[9],casos_novos_lista_regioes_saude[9],obitos_acumulados_lista_regioes_saude[9],obitos_novos_lista_regioes_saude[9]]

#TUPLA REGIÕES DE SAÚDE (Dados pegos da tabela no dia 31/08/20)

        #Organização dos dados das regiões de saúde em tuplas - Informações na mesma posição correspondem a mesma região de saúde. 
regioes_saude_tupla = ("Vale do Jamari(RO - Código 11001)","Cafe (RO - Código 11002)", "Central(RO - Código 11003)","Madeira-mármore(RO - Código 11004)","Zona da mata(RO - Código 11005)",
"Cone sul(RO - Código 11006)","Vale do guapore (RO - Código 11007)","Alto acre (AC - Código 12001)","Baixo Acre e purus (AC - Código 12002)","Jurua e tarauaca/envira (AC - Código 12003)")
populacao_TCU_2019_tupla_regioes_saude =(107863,85359,128969,529544,55058,99854,18331,26278,407319,88376)
casos_acumulado_tupla_regioes_saude =(4483,1682,2068,26868,1229,2799,207,1113,9987,3132)
casos_novos_tupla_regioes_saude =(15,1,37,124,1,32,18,4,4,0)
obitos_acumulados_tupla_regioes_saude = (76,27,45,646,16,40,4,17,384,55)
obitos_novos_tupla_regioes_saude =(1,4,3,4,0,1,1,0,1,1)

         #TUPLA organizados por regiões de saúde - Informação dada na sequência: (1)Estado, (2) população do estado,(3) Casos acumulados,(4) casos novos,(5) óbitos acumulados e (6) óbitos novos

Vale_do_jamari_tupla =(regioes_saude_tupla[0],populacao_TCU_2019_tupla_regioes_saude[0],casos_acumulado_tupla_regioes_saude[0],casos_novos_tupla_regioes_saude[0],obitos_acumulados_tupla_regioes_saude[0],obitos_novos_tupla_regioes_saude[0])
Cafe_tupla = (regioes_saude_tupla[1],populacao_TCU_2019_tupla_regioes_saude[1],casos_acumulado_tupla_regioes_saude[1],casos_novos_tupla_regioes_saude[1],obitos_acumulados_tupla_regioes_saude[1],obitos_novos_tupla_regioes_saude[1])
Central_tupla = (regioes_saude_tupla[2],populacao_TCU_2019_tupla_regioes_saude[2],casos_acumulado_tupla_regioes_saude[2],casos_novos_tupla_regioes_saude[2],obitos_acumulados_tupla_regioes_saude[2],obitos_novos_tupla_regioes_saude[2])
Madeira_marmore_tupla = (regioes_saude_tupla[3],populacao_TCU_2019_tupla_regioes_saude[3],casos_acumulado_tupla_regioes_saude[3],casos_novos_tupla_regioes_saude[3],obitos_acumulados_tupla_regioes_saude[3],obitos_novos_tupla_regioes_saude[3])
Zona_da_mata_tupla = (regioes_saude_tupla[4],populacao_TCU_2019_tupla_regioes_saude[4],casos_acumulado_tupla_regioes_saude[4],casos_novos_tupla_regioes_saude[4],obitos_acumulados_tupla_regioes_saude[4],obitos_novos_tupla_regioes_saude[4])
Cone_sul_tupla = (regioes_saude_tupla[5],populacao_TCU_2019_tupla_regioes_saude[5],casos_acumulado_tupla_regioes_saude[5],casos_novos_tupla_regioes_saude[5],obitos_acumulados_tupla_regioes_saude[5],obitos_novos_tupla_regioes_saude[5])
Vale_do_guapode_tupla = (regioes_saude_tupla[6],populacao_TCU_2019_tupla_regioes_saude[6],casos_acumulado_tupla_regioes_saude[6],casos_novos_tupla_regioes_saude[6],obitos_acumulados_tupla_regioes_saude[6],obitos_novos_tupla_regioes_saude[6])
Alto_acre_tupla = (regioes_saude_tupla[7],populacao_TCU_2019_tupla_regioes_saude[7],casos_acumulado_tupla_regioes_saude[7],casos_novos_tupla_regioes_saude[7],obitos_acumulados_tupla_regioes_saude[7],obitos_novos_tupla_regioes_saude[7])
Baixo_acre_purus_tupla = (regioes_saude_tupla[8],populacao_TCU_2019_tupla_regioes_saude[8],casos_acumulado_tupla_regioes_saude[8],casos_novos_tupla_regioes_saude[8],obitos_acumulados_tupla_regioes_saude[8],obitos_novos_tupla_regioes_saude[8])
Jurua_tarauaca_tupla = (regioes_saude_tupla[9],populacao_TCU_2019_tupla_regioes_saude[9],casos_acumulado_tupla_regioes_saude[9],casos_novos_tupla_regioes_saude[9],obitos_acumulados_tupla_regioes_saude[9],obitos_novos_tupla_regioes_saude[9])




######## ALTERNATIVA B ####### - Mande printar na tela o número de casos acumulados para o estado do rio de janeiro tanto para a tupla quanto para a lista
        #NOTA: É possível gerar com base com base no código acima a informação de qualquer estado. 
print("No estado do Rio de Janeiro, O número de casos acumulados é: ", Rio_de_janeiro_lista[2])
print ("No estado do Rio de Janeiro, O número de casos acumulados é: ", Rio_de_janeiro_tupla[2])


######## ALTERNATIVA C ####### -Apresente na tela todos os óbitos acumulados mostrando os casos apenas para o caso dos estados (sem mostrar regiões de saúde, etc..).
print("\nNo estado do ",Acre_lista[0], "O número de óbitos acumulados é: ", Acre_lista[4])
print("No estado do ",Alagoas_lista [0], "O número de óbitos acumulados é: ", Alagoas_lista [4])
print("No estado do ",Amazonas_lista [0], "O número de óbitos acumulados é: ",Amazonas_lista [4])
print("No estado do ",Amapá_lista [0], "O número de óbitos acumulados é: ", Amapá_lista [4])
print("No estado do ",Bahia_lista [0], "O número de óbitos acumulados é: ", Bahia_lista [4])
print("No estado do ",Ceará_lista [0], "O número de óbitos acumulados é: ", Ceará_lista [4])
print("No estado do ",Distrito_federal_lista [0], "O número de óbitos acumulados é: ", Distrito_federal_lista [4])
print("No estado do ",Espirito_santo_lista [0], "O número de óbitos acumulados é: ", Espirito_santo_lista [4])
print("No estado do ",Goias_lista [0], "O número de óbitos acumulados é: ", Goias_lista [4])
print("No estado do ",Maranhao_lista [0], "O número de óbitos acumulados é: ", Maranhao_lista [4])
print("No estado do ",Minas_gerais_lista [0], "O número de óbitos acumulados é: ", Minas_gerais_lista [4])
print("No estado do ",Mato_grosso_sul_lista [0], "O número de óbitos acumulados é: ", Mato_grosso_sul_lista [4])
print("No estado do ",Para_lista [0], "O número de óbitos acumulados é: ", Para_lista [4])
print("No estado do ",Paraiba_lista [0], "O número de óbitos acumulados é: ", Paraiba_lista [4])
print("No estado do ",Pernambuco_lista [0], "O número de óbitos acumulados é: ", Pernambuco_lista [4])
print("No estado do ",Piaui_lista[0], "O número de óbitos acumulados é: ", Piaui_lista [4])
print("No estado do ",Parana_lista [0], "O número de óbitos acumulados é: ", Parana_lista [4])
print("No estado do ",Rio_de_janeiro_lista [0], "O número de óbitos acumulados é: ", Rio_de_janeiro_lista [4])
print("No estado do ",Rio_grande_norte_lista [0], "O número de óbitos acumulados é: ", Rio_grande_norte_lista [4])
print("No estado do ",Rondonia_lista [0], "O número de óbitos acumulados é: ", Rondonia_lista [4])
print("No estado do ",Roraima_lista [0], "O número de óbitos acumulados é: ", Roraima_lista [4])
print("No estado do ",Rio_grande_sul_lista [0], "O número de óbitos acumulados é: ", Rio_grande_sul_lista [4])
print("No estado do ",Santa_catarina_lista [0], "O número de óbitos acumulados é: ",Santa_catarina_lista [4])
print("No estado do ",Sergipe_lista [0], "O número de óbitos acumulados é: ", Sergipe_lista [4])
print("No estado do ",Sao_paulo_lista [0], "O número de óbitos acumulados é: ", Sao_paulo_lista [4])
print("No estado do ",Tocantins_lista [0], "O número de óbitos acumulados é: ", Tocantins_lista [4])


 ######## ALTERNATIVA D ####### - 	Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10 unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla, corrigindo os dados. 
Paraiba_lista[5]= Paraiba_lista[5] + 10
print ("\nO valor corrigido de óbitos novos na Paraiba é: ",Paraiba_lista[5]) #Valor inicial é 15


######## ALTERNATIVA E ######### -	As duas operações foram possíveis (lista e tupla)? Justifique.
# Não. Só foi possível somente na lista. A tupla não é possível, uma vez que a tupla é imutável, não permitindo essa troca de valores

####### ALTERNATIVA F ######### - Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa lista nova a lista já existente

#Lista nova estado
Lista_nova_amapa = [845731,39957,254,619,2] #Informação de 18/08/20

#Municípios
municipios_listaAP = ["Serra do Navio","Amapá","Pedra Branca do Amapari","Calçoene","Cutias","Ferreira Gomes","Itaubal","Laranjal do Jari","Macapá","Mazagão","Oiapoque","Porto Grande",
"Pracuúba","Santana","Tartarugalzinho","Vitória do Jari"]
populacao_TCU_2019_lista_municipioAP = [5397,9109,16502,11117,5983,7780,5503,50410,503327,21632,27270,21971,5120,121364,17315,15931]
casos_acumulado_lista_municipioAP = [574,449,2436,1118,522,532,286,4020,16297,1318,2333,1030,350,5988,921,1783]
casos_novos_lista_municipioAP = [2,4,3,1,0,1,0,60,68,9,0,2,0,59,24,21]
obitos_acumulados_lista_municipioAP = [4,4,5,5,2,3,0,43,417,7,19,10,2,81,4,13]
obitos_novos_lista_municipioAP = [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]
regioes_saude_lista_AP = ["CENTRAL","NORTE","CENTRAL","NORTE","CENTRAL","CENTRAL","CENTRAL","SUDOESTE","CENTRAL","SUDOESTE","NORTE","CENTRAL"
"NORTE","SUDOESTE","NORTE","SUDOESTE"]

lista_municipios_amapa = [municipios_listaAP,populacao_TCU_2019_lista_municipioAP,casos_acumulado_lista_municipioAP,casos_novos_lista_municipioAP,
obitos_acumulados_lista_municipioAP,obitos_novos_lista_municipioAP,regioes_saude_lista_AP]

#Adicionando a lista com os dados do município a lista criada só com os dados do Amapá
Lista_nova_amapa.append(lista_municipios_amapa)
print("\n",Lista_nova_amapa)

########## ALTERNATIVA G ######## - Remova da lista os dados das regiões de saúde.
lista_municipios_amapa.remove(regioes_saude_lista_AP)
print (Lista_nova_amapa)


######### ALTERNATIVA H ###########  - Verifique se a soma dos dados dos municípios na data de 18/08/2020 é igual ao dado da lista, mostrando na tela apenas se for verdadeiro.
Lista_nova_amapa = [845731,39957,254,619,2] #Informação de 18/08/20
print("\nA soma dos dados do estado no dia 18/08/20 é igual a soma dos dados dos municípios? ", 
sum (lista_municipios_amapa[1]) + sum (lista_municipios_amapa[2]) + sum (lista_municipios_amapa[3]) + sum (lista_municipios_amapa[4]) + sum (lista_municipios_amapa[5]) == sum (Lista_nova_amapa)) #Está dando True



####### ALTERNATIVA I  ##### - i.	Retorne o tamanho total da lista.

tamanho_lista = (len(Lista_nova_amapa)) + (len(lista_municipios_amapa)*16) # (O tamanho real de dados na lista é a soma dos dados do estado (5)) + (o número de municipios(16) multiplicado por pela quantidade de informações (6 - Já que foi removida as regiões de saúde)retirada por municipio (totalizando 101)
print("\nO tamanho da lista é: ", tamanho_lista)

############ ALTERNATIVA J ############ - j.	Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de óbitos novos.
maior_valor_obitos_novos_lista = max(lista_municipios_amapa[5])
menor_valor_obitos_novos_lista = min(lista_municipios_amapa[5])
print ("\nO menor e maior valor, respectivamente, de óbitos novos são: ", menor_valor_obitos_novos_lista ,"e", maior_valor_obitos_novos_lista)

########## ALTERNATIVA K E L ##################### - 
# Crie um dicionário de forma que seja possível encontrar os municípios associados a um estado específico e extrair os dados de casos novos em apenas um comando. 

dicionario_municipios_casos_novos_amapa = {"Serra do navio":2,"Amapá":4,"Pedra Branca do Amapari":31,"Calçoene":1,"Cutias":0,"Ferreira Gomes":1,"Itaubal":0,"Laranjal do Jari":60,
"Macapá":68,"Mazagão":9,"Oiapoque":0,"Porto Grande":2,"Pracuúba":0,"Santana":59,"Tartarugalzinho":24,"Vitória do Jari":21}

print("\n",dicionario_municipios_casos_novos_amapa)


# Extraia os dados de Teresina/PI apresentando os casos novos com um print.
dicionario_casos_novos_teresina = {"População":864845, "Casos acumulados":22102,"Casos novos":299,"Óbitos acumulados":833,"Óbitos novos":7} 
print ("\n",dicionario_casos_novos_teresina ["Casos novos"] )










