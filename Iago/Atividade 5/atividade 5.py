import math

# LISTA USA []
estadoLista = [
    "AC",
    "AL",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MG",
    "MS",
    "MT",
    "PA",
    "PB",
    "PE",
    "PI",
    "PR",
    "RJ",
    "RN",
    "RO",
    "RR",
    "RS",
    "SC",
    "SE",
    "SP",
    "TO",
]
totalPopulacaoLista = [
    881935,
    3337357,
    4144597,
    845731,
    14873064,
    9132078,
    3015268,
    4018650,
    7018354,
    7075181,
    21168791,
    2778986,
    3484466,
    8602865,
    4018127,
    9557071,
    3273227,
    11433957,
    17264943,
    3506853,
    1777225,
    605761,
    11377239,
    7164788,
    2298696,
    45919049,
    1572866,
]
casosAcumuladoLista = [
    460,
    73701,
    112881,
    39957,
    221041,
    199258,
    140170,
    101874,
    105962,
    139185,
    177787,
    38393,
    75877,
    180090,
    97497,
    113788,
    67226,
    108237,
    199480,
    58307,
    48923,
    40183,
    101217,
    124313,
    68699,
    711530,
    38845,
]
casosNovosLista = [
    0,
    763,
    618,
    254,
    3926,
    1056,
    1435,
    1015,
    3297,
    1777,
    2072,
    968,
    1368,
    1715,
    1274,
    605,
    911,
    1858,
    4829,
    409,
    691,
    518,
    3210,
    2647,
    386,
    8865,
    989,
]
obitosAcumuladoLista = [
    14,
    1774,
    3524,
    619,
    4542,
    8196,
    2097,
    2938,
    2414,
    3289,
    4306,
    657,
    2384,
    5975,
    2203,
    7252,
    1637,
    2781,
    14728,
    2102,
    1026,
    574,
    2822,
    1883,
    1729,
    27315,
    531,
]
obitosNovosLista = [
    0,
    11,
    19,
    2,
    67,
    33,
    55,
    30,
    78,
    12,
    83,
    17,
    16,
    30,
    20,
    42,
    18,
    48,
    162,
    21,
    9,
    6,
    78,
    44,
    12,
    416,
    15,
]

lista1 = [
    estadoLista,
    totalPopulacaoLista,
    casosAcumuladoLista,
    casosNovosLista,
    obitosAcumuladoLista,
    obitosNovosLista,
]
"""--------------------------------------------------------------------------
#TUPLA USA ()
------------------------------------------------------------------------------
"""

estadoTupla = (
    "AC",
    "AL",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MG",
    "MS",
    "MT",
    "PA",
    "PB",
    "PE",
    "PI",
    "PR",
    "RJ",
    "RN",
    "RO",
    "RR",
    "RS",
    "SC",
    "SE",
    "SP",
    "TO",
)
totalPopulacaoTupla = (
    881935,
    3337357,
    4144597,
    845731,
    14873064,
    9132078,
    3015268,
    4018650,
    7018354,
    7075181,
    21168791,
    2778986,
    3484466,
    8602865,
    4018127,
    9557071,
    3273227,
    11433957,
    17264943,
    3506853,
    1777225,
    605761,
    11377239,
    7164788,
    2298696,
    45919049,
    1572866,
)
casosAcumuladoTupla = (
    460,
    73701,
    112881,
    39957,
    221041,
    199258,
    140170,
    101874,
    105962,
    139185,
    177787,
    38393,
    75877,
    180090,
    97497,
    113788,
    67226,
    108237,
    199480,
    58307,
    48923,
    40183,
    101217,
    124313,
    68699,
    711530,
    38845,
)
casosNovosTupla = (
    0,
    763,
    618,
    254,
    3926,
    1056,
    1435,
    1015,
    3297,
    1777,
    2072,
    968,
    1368,
    1715,
    1274,
    605,
    911,
    1858,
    4829,
    409,
    691,
    518,
    3210,
    2647,
    386,
    8865,
    989,
)
obitosAcumuladoTupla = (
    14,
    1774,
    3524,
    619,
    4542,
    8196,
    2097,
    2938,
    2414,
    3289,
    4306,
    657,
    2384,
    5975,
    2203,
    7252,
    1637,
    2781,
    14728,
    2102,
    1026,
    574,
    2822,
    1883,
    1729,
    27315,
    531,
)
obitosNovosTupla = (
    0,
    11,
    19,
    2,
    67,
    33,
    55,
    30,
    78,
    12,
    83,
    17,
    16,
    30,
    20,
    42,
    18,
    48,
    162,
    21,
    9,
    6,
    78,
    44,
    12,
    416,
    15,
)

tupla1 = (
    estadoTupla,
    totalPopulacaoTupla,
    casosAcumuladoTupla,
    casosNovosTupla,
    obitosAcumuladoTupla,
    obitosNovosTupla,
)

"""
------------------------------------------------------------------------------------------------
#PRINT DE CASOS DO RJ - tupla e lista
------------------------------------------------------------------------------------------------
"""
print("LISTA ITEM b - DADOS DO DIA 18/08/2020")
print("Print uma tupla dos casos acumulados do RJ")
print("Estado | Casos Acumulados")
print(estadoTupla[18], "    | ", casosAcumuladoTupla[18], "\n")

print("TUPLA ITEM b - DADOS DO DIA 18/08/2020")
print("Print uma Lista dos casos acumulados do RJ")
print("Estado | Casos Acumulados")
print(estadoLista[18], "    | ", casosAcumuladoLista[18], "\n")

# Apresente na tela todos os óbitos acumulados mostrando os casos apenas para
#  o caso dos estados (sem mostrar regiões de saúde, etc..)

print("Apresentar na tela todos os óbitos acumulados")
print("Estado | Casos Acumulados")
print(estadoLista[0], "    | ", casosAcumuladoLista[0])
print(estadoLista[1], "    | ", casosAcumuladoLista[1])
print(estadoLista[2], "    | ", casosAcumuladoLista[2])
print(estadoLista[3], "    | ", casosAcumuladoLista[3])
print(estadoLista[4], "    | ", casosAcumuladoLista[4])
print(estadoLista[5], "    | ", casosAcumuladoLista[5])
print(estadoLista[6], "    | ", casosAcumuladoLista[6])
print(estadoLista[7], "    | ", casosAcumuladoLista[7])
print(estadoLista[8], "    | ", casosAcumuladoLista[8])
print(estadoLista[9], "    | ", casosAcumuladoLista[9])
print(estadoLista[10], "    | ", casosAcumuladoLista[10])
print(estadoLista[11], "    | ", casosAcumuladoLista[11])
print(estadoLista[12], "    | ", casosAcumuladoLista[12])
print(estadoLista[13], "    | ", casosAcumuladoLista[13])
print(estadoLista[14], "    | ", casosAcumuladoLista[14])
print(estadoLista[15], "    | ", casosAcumuladoLista[15])
print(estadoLista[16], "    | ", casosAcumuladoLista[16])
print(estadoLista[17], "    | ", casosAcumuladoLista[17])
print(estadoLista[18], "    | ", casosAcumuladoLista[18])
print(estadoLista[19], "    | ", casosAcumuladoLista[19])
print(estadoLista[20], "    | ", casosAcumuladoLista[20])
print(estadoLista[21], "    | ", casosAcumuladoLista[21])
print(estadoLista[22], "    | ", casosAcumuladoLista[22])
print(estadoLista[23], "    | ", casosAcumuladoLista[23])
print(estadoLista[24], "    | ", casosAcumuladoLista[24])
print(estadoLista[25], "    | ", casosAcumuladoLista[25])
print(estadoLista[26], "    | ", casosAcumuladoLista[26])

"""
Assuma que os dados de óbitos novos para o estado da paraíba estejam errados
em 10 unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla, corrigindo os dados. 
"""
obitosNovosLista[14] = obitosNovosLista[14] - 10

print("\n")
print("Questão d")
print("Óbitos novos para o Estado da Paraíba corrigido em -10 ")
print(estadoLista[14], "    | ", obitosNovosLista[14], "\n\n")

print("Justificando a questão e")
print("não é possivel alterar dados de uma tupla\n")

