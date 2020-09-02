#A)crie uma lista e uma tupla com as informações disponíveis no documento csv
#lista organizada por: [estados, populacao, casos acumulados, casos novos, obitos acumulados, obitos novos]
lista = [['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE','AL', 'RJ'], [1777225, 881935,4144597, 605761, 8602865, 845731, 1572866,7075181, 3273227, 9132078,3506853,4018127,9557071,3337357,17264943], [48923, 22933,112881,40183, 180090, 39957, 38845,139185, 67226, 199258,58307,97497, 113788, 73701,199480], [691, 328, 618,518, 1715, 254, 989,1777, 911, 1056, 409, 1274, 605,763, 4829], [1026, 590, 3524, 574, 5975, 619, 531, 3289, 1637,8196, 2102,2203, 7252,1774,14728], [9, 8, 19, 6, 30, 2, 15,12, 18,33,21,20,42, 11, 162]]
tupla = (('RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE','AL', 'RJ'), (1777225, 881935,4144597, 605761, 8602865, 845731, 1572866,7075181, 3273227, 9132078,3506853,4018127,9557071,3337357,17264943), (48923, 22933,112881,40183, 180090, 39957, 38845,139185, 67226, 199258,58307,97497, 113788, 73701,199480), (691, 328, 618,518, 1715, 254, 989,1777, 911, 1056, 409, 1274, 605,763, 4829), (1026, 590, 3524, 574, 5975, 619, 531, 3289, 1637,8196, 2102,2203, 7252,1774,14728), (9, 8, 19, 6, 30, 2, 15,12, 18,33,21,20,42, 11, 162))

#B)Mande printar na tela o número de casos acumulados para o estado do rio de janeiro tanto para a tupla quanto para a lista.

#printlista
print("casos acumulados no Rio de Janeiro: ", lista[2][14])
#printtupla
print("casos acumulados no Rio de Janeiro: ", tupla[2][14])

#C) Apresente na tela todos os óbitos acumulados mostrando os casos apenas para o caso dos estados
print("Obitos acumulados por estado: ", lista[4])

#D)Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10
#unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla,
#corrigindo os dados.   

lista[5][11]= lista[5][11] + 10

#tupla
#tupla[5][11]= tupla[5][11] + 10

print("Correção no número de obitos novos da Paraiba (lista):", lista[5][11])
print("Correção no número de obitos novos da Paraiba (tupla):", tupla[5][11])

#E)As duas operações foram possíveis (lista e tupla)? Justifique.
print("****OBS: Foi feita a tentativa de sobrescrever a lista e a tupla, porém só é possível fazer a alteração dos elementos da lista. A sintaxe da tupla não permite")

#F)Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa
#lista nova a lista já existente (append ou insert).

#Lista de municipios do Acre

municipiosAcre=[
"Rio Branco","Cruzeiro do Sul", "Sena Madureira","Tarauacá","Feijó","Senador Guiomard","Brasileia",
"Plácido de Castro","Xapuri","Marechal Thaumaturgo","Mâncio Lima","Rodrigues Alves","Porto Acre",
"Epitaciolândia","Acrelândia", "Manoel Urbano","Porto Walter","Bujari","Capixaba","Jordão","Assis Brasil",
"Santa Rosa do Purus"]

codregiaodeSaude=[12002,12003,120050, 12003, 12001, 12002, 12001, 12001, 12001, 12003, 12003,12003,12002,12001,
 12002,12002,12003, 12002, 12002, 12002, 12001, 12002]

municipiosAcre.append(codregiaodeSaude)
print(municipiosAcre)

#G) Remova da lista os dados das regiões de saúde.
municipiosAcre.remove(codregiaodeSaude)
print(municipiosAcre)
				
#H) Verifique se a soma dos dados dos municípios na data de 18/08/2020 é igual ao dado da
#lista, mostrando na tela apenas se for verdadeiro.										
somapopulacaoAcre=15256+7417+26278+10266+11733+88376+18411+34780+8317+18977+9459+18867+19761+11982+407319+18930+6540+23024+45848+42567+19323+18504
somaCasosAcumuladosAcre=398+440+1035+353+240+2961+456+968+119+553+253+287+386+240+9692+137+201+401+1267+1401+685+460
somaCasosNovosAcre=20+1+93+1+1+19+15+6+4+0+2+3+30+2+2+17+85+27
somaObitosAcumuladosAcre=8+9+15+6+7+53+11+16+1+8+2+1+8+2+377+6+2+10+10+13+11+14
somaObtidosNovosAcre=1+6+1

print(somaCasosAcumuladosAcre== lista[2][1])
print(somaCasosNovosAcre== lista[3][1])
print(somaObitosAcumuladosAcre== lista[4][1])
print(somaObtidosNovosAcre== lista[5][1])

#I) Retorne o tamanho total da lista.
print(len(lista))

#J) Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de
#óbitos novos.
maior=max(lista[5])
menor= min(lista[5])

print("Maior valor de obitos novos: ", maior)
print("Menor valor de obitos novos: ", menor)


#K) Crie um dicionário de forma que seja possível encontrar os municípios associados a um
#estado específico e extrair os dados de casos novos em apenas um comando.

dictAcre={
    "Acrelândia":20,"Assis Brasil":1,"Brasileia":93,"Bujari":1,"Capixaba":1,"Cruzeiro do Sul":19,
    "Epitaciolândia":15,"Feijó":6,"Jordão":4,"Mâncio Lima":0,"Manoel Urbano":2,"Marechal Thaumaturgo":3,
    "Plácido de Castro":0,
    "Porto Acre":0,"Porto Walter":0,"Rio Branco":30,"Rodrigues Alves":2,"Santa Rosa do Purus":2,
    "Senador Guiomard":17,"Sena Madureira":85,"Tarauacá":27,"Xapuri":0
}

print(dictAcre)

#L) Extraia os dados de Teresina/PI apresentando os casos novos com um print.
dictTeresinaPI={

    "codigo Municipio":221100,"codigo Região Saúde":22004,"populacao":864845,"Casos Acumulados":22102,
    "casos novos":299, "obitos acumulados":833, "obitos novos":7

}

print("Casos novos de Teresina/PI:", dictTeresinaPI["casos novos"])