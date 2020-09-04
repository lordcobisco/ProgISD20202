'''
lista = []
print(lista)


lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
print(lista)
novaLista = ['Nova lista', lista]
print(novaLista)

#Acesssando uma lista
string = lista[0]
print(string)
print(lista[1])

print(novaLista[0])
print(novaLista[1])
print(novaLista[1][1])
print(novaLista[1][2])


#função len
lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
novaLista = ['Gilberto', lista]
print(len(lista))
print(len(novaLista))
print(len(novaLista[1]))



#Operadores + e -
lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
novaLista = ['Gilberto', lista]
print(lista+lista)
print(len(lista+lista))
print(len(lista+[1]))

print(lista*3)


#Operador in
lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
print('Peixe' in lista)
if('Peixe' in lista):
    print('Existe a palavra Peixe como um dos elementos da lista')

#operador max, min, sum
listaDeNumeros = [56,5,75,8,2,96,6]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros)/len(listaDeNumeros))

#função

lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
print(lista[-1])
print(lista[-2])
print(lista[-3])



#Operador append

livros = ['Java', 'Python', 'SqlServer', 'Delphy']
print(livros)
livros.append('Android')
print(livros)

#Operador insert e pop

livros.insert(0,'Oracle')
print(livros)

print(livros.pop())
print(livros)
livros[1]="2020"
print(livros)


livros.remove('SqlServer')
print(livros)
""'
livros.sort()
print(livros)

#reverse inverte a ordem


numeros = [1,5,3,4,8,10,22,9]
numeros.sort()
numeros.reverse()
print(numeros)


lista = ['o carro é vermelho', 'Peixe','Peixe', 'Gilberto', 'Hera']
print(lista.count('Peixe'))
lista.remove('Peixe')
print(lista)


a = [81,82,83]
b = a
print(b is a)
b[1]=999
print(a)

a = [81,82,83]
b = [81,82,83]
print(b is a)
print(b == a)

lista = [10,20,30,40,50,60,70,80,90]
print(lista.index(60))
print(lista[1:6])

tupla = (1,2,3,4)
print(tupla)
tupla = (1,)
print(tupla)
tupla = ()
print(tupla)

tupla = ('Maria', 'João', 'Carlos', 'Gilberto', 'Hera')
print(tupla[0:3])
#tupla[0] = 'Ana'


dadosCovid = {}
print(dadosCovid)
dadosCovid = dict()
print(dadosCovid)

dadosCovidCasosNovos = {'Brasil':[0,1,0,0,1,0,0,0,2,3,4], 'Nordeste':[0,0,0,4,3,2,4,5,0,2]}
print(dadosCovidCasosNovos)
print(dadosCovidCasosNovos['Brasil'])

agenda = {}
print(agenda)

agenda = {"Maria": [9988877450, 98885555]}
print(agenda)

agenda = {"Maria": [9988877450, 98885555], "Pedro": [998888524], "Thomas": [98854471147]}
print(agenda)

print(agenda["Maria"])

agenda["Thomas"] = [98885225]
print(agenda)

agenda = {}
print(agenda)
agenda["Gilberto"] = [8555414452]

'''
#lista = [['Norte', 'AC', 'Sena Madureira', 12, 120050, 12002, 'BAIXO ACRE E PURUS', '2020-04-11 00:00:00', 15, 45848.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Rodrigues Alves', 12, 120042, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-07-04 00:00:00', 27, 18930.0, 97, 0, 4, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '2020-04-25 00:00:00', 17, 17722.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Piranhas', 27, 270710, 27010, '10ª REGIAO DE SAUDE', '2020-07-10 00:00:00', 28, 25039.0, 45, 0, 2, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Itamarati', 13, 130195, 13007, 'REGIONAL JURUA', '2020-06-11 00:00:00', 24, 7851.0, 78, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Amaturá', 13, 130006, 13009, 'ALTO SOLIMOES', '2020-07-11 00:00:00', 28, 11536.0, 464, 8, 8, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '2020-07-02 00:00:00', 27, 121364.0, 4090, 36, 66, 1, ' ', ' ', 1.0], ['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '2020-08-25 00:00:00', 35, 7780.0, 535, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Lajedinho', 29, 291900, 29011, 'ITABERABA', '2020-07-29 00:00:00', 31, 3783.0, 3, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'São Domingos', 29, 292895, 29025, 'SERRINHA', '2020-03-28 00:00:00', 13, 9058.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Apuiarés', 23, 230090, 23002, '2ª REGIAO CAUCAIA', '2020-05-24 00:00:00', 22, 14600.0, 19, 0, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Uruoca', 23, 231390, 23011, '11ª REGIAO SOBRAL', '2020-07-30 00:00:00', 31, 13840.0, 453, 16, 15, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-06-05 00:00:00', 23, 3015268.0, 14208, 1285, 202, 6, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-02 00:00:00', 14, 3015268.0, 370, 15, 4, 1, ' ', ' ', 1.0], ['Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '2020-06-10 00:00:00', 24, 30586.0, 108, 4, 7, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-06-03 00:00:00', 23, 30867.0, 43, 1, 3, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Nova Roma', 52, 521490, 52007, 'NORDESTE II', '2020-08-10 00:00:00', 33, 3264.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Castelândia', 52, 520505, 52015, 'SUDOESTE I', '2020-05-26 00:00:00', 22, 3435.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Coroatá', 21, 210360, 21007, 'CODO', '2020-06-15 00:00:00', 25, 65296.0, 238, 0, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Vitorino Freire', 21, 211300, 21002, 'BACABAL', '2020-08-11 00:00:00', 33, 31523.0, 1392, 12, 24, 2, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Taquaraçu de Minas', 31, 316830, 31016, 'BELO HORIZONTE/ NOVA LIMA/ CAETE ', '2020-05-23 00:00:00', 21, 4077.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Sudeste', 'MG', 'Andrelândia', 31, 310280, 31090, 'LIMA DUARTE', '2020-08-18 00:00:00', 34, 12224.0, 49, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Dourados', 50, 500370, 50003, 'DOURADOS', '2020-06-01 00:00:00', 23, 222949.0, 306, 27, 2, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Paranhos', 50, 500635, 50003, 'DOURADOS', '2020-04-01 00:00:00', 14, 14228.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Rondonópolis', 51, 510760, 51013, 'SUL MATOGROSSENSE', '2020-06-14 00:00:00', 25, 232491.0, 497, 52, 12, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Feliz Natal', 51, 510370, 51014, 'TELES PIRES', '2020-05-30 00:00:00', 22, 14192.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Anajás', 15, 150070, 15014, 'MARAJO II', '2020-05-08 00:00:00', 19, 29277.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Breves', 15, 150180, 15014, 'MARAJO II', '2020-05-23 00:00:00', 21, 102701.0, 432, 7, 50, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Guarabira', 25, 250630, 25002, '2ª REGIAO', '2020-05-30 00:00:00', 22, 58833.0, 557, 12, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-07-29 00:00:00', 31, 22819.0, 309, 11, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Salgadinho', 26, 261210, 26006, 'LIMOEIRO', '2020-04-21 00:00:00', 17, 10919.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Terra Nova', 26, 261520, 26011, 'SALGUEIRO', '2020-07-16 00:00:00', 29, 10096.0, 6, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Currais', 22, 220323, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-04-18 00:00:00', 16, 4954.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Corrente', 22, 220290, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-05-01 00:00:00', 18, 26644.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Sabáudia', 41, 412270, 41016, '16ª RS APUCARANA', '2020-05-10 00:00:00', 20, 6827.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Porto Rico', 41, 412020, 41014, '14ª RS PARANAVAI', '2020-08-03 00:00:00', 32, 2559.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Santa Maria Madalena', 33, 330460, 33009, 'SERRANA', '2020-07-28 00:00:00', 31, 10404.0, 75, 0, 2, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Seropédica', 33, 330555, 33005, 'METROPOLITANA I', '2020-06-26 00:00:00', 26, 82312.0, 429, 4, 23, 0, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Pendências', 24, 240990, 24008, '8ª REGIAO DE SAUDE - ACU', '2020-06-16 00:00:00', 25, 15129.0, 93, 6, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'São José do Campestre', 24, 241230, 24005, '5ª REGIAO DE SAUDE - SANTA CRUZ', '2020-05-25 00:00:00', 22, 12856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-20 00:00:00', 17, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Alvorada DOeste', 11, 110034, 11003, 'CENTRAL', '2020-07-01 00:00:00', 27, 14411.0, 18, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '2020-05-18 00:00:00', 21, 21926.0, 12, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '2020-08-19 00:00:00', 34, 11950.0, 237, 3, 4, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Jari', 43, 431113, 43002, 'REGIAO 02', '2020-08-12 00:00:00', 33, 3503.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Vila Flores', 43, 432330, 43025, 'REGIAO 25', '2020-08-23 00:00:00', 35, 3385.0, 77, 5, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Porto Belo', 42, 421350, 42005, 'FOZ DO RIO ITAJAI', '2020-06-06 00:00:00', 23, 21388.0, 26, 2, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Presidente Nereu', 42, 421410, 42004, 'ALTO VALE DO ITAJAI', '2020-04-13 00:00:00', 16, 2287.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Nossa Senhora Aparecida', 28, 280445, 28003, 'ITABAIANA', '2020-06-11 00:00:00', 24, 8796.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Japoatã', 28, 280340, 28007, 'PROPRIA', '2020-04-28 00:00:00', 18, 13434.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sud Mennucci', 35, 355230, 35022, 'LAGOS DO DRS II', '2020-06-11 00:00:00', 24, 7718.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sandovalina', 35, 354550, 35112, 'ALTA SOROCABANA', '2020-06-13 00:00:00', 24, 4302.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Gurupi', 17, 170950, 17005, 'ILHA DO BANANAL', '2020-07-23 00:00:00', 30, 86647.0, 717, 39, 7, 1, ' ', ' ', 0.0], ['Norte', 'TO', 'Riachinho', 17, 171855, 17002, 'BICO DO PAPAGAIO', '2020-05-20 00:00:00', 21, 4645.0, 2, 0, 0, 0, ' ', ' ', 0.0]]

a=0
while a <= 54:
    print(lista[a][1],':',lista[a][12])
    a = a+1
print('Acabou o programa')


print(lista[0][3])
lista[0][3]=13
print(lista[0][3])

# lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]


#Operador append

livros = ['Java', 'Python', 'SqlServer', 'Delphy']
livros2 = ['HP', 'LOTR', 'AI']

print(livros)
#livros.append(livros2)
livros.insert(3,livros2)
print(livros)


#Operador insert e pop

livros.insert(0,'Oracle')
print(livros)


#lista = [['Norte', 'AC', 'Sena Madureira', 12, 120050, 12002, 'BAIXO ACRE E PURUS', '2020-04-11 00:00:00', 15, 45848.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'AC', 'Rodrigues Alves', 12, 120042, 12003, 'JURUA E TARAUACA/ENVIRA', '2020-07-04 00:00:00', 27, 18930.0, 97, 0, 4, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '2020-04-25 00:00:00', 17, 17722.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'AL', 'Piranhas', 27, 270710, 27010, '10ª REGIAO DE SAUDE', '2020-07-10 00:00:00', 28, 25039.0, 45, 0, 2, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Itamarati', 13, 130195, 13007, 'REGIONAL JURUA', '2020-06-11 00:00:00', 24, 7851.0, 78, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'AM', 'Amaturá', 13, 130006, 13009, 'ALTO SOLIMOES', '2020-07-11 00:00:00', 28, 11536.0, 464, 8, 8, 0, ' ', ' ', 0.0], ['Norte', 'AP', 'Santana', 16, 160060, 16003, 'AREA SUDOESTE', '2020-07-02 00:00:00', 27, 121364.0, 4090, 36, 66, 1, ' ', ' ', 1.0], ['Norte', 'AP', 'Ferreira Gomes', 16, 160023, 16001, 'AREA CENTRAL', '2020-08-25 00:00:00', 35, 7780.0, 535, 0, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'Lajedinho', 29, 291900, 29011, 'ITABERABA', '2020-07-29 00:00:00', 31, 3783.0, 3, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'BA', 'São Domingos', 29, 292895, 29025, 'SERRINHA', '2020-03-28 00:00:00', 13, 9058.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Apuiarés', 23, 230090, 23002, '2ª REGIAO CAUCAIA', '2020-05-24 00:00:00', 22, 14600.0, 19, 0, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'CE', 'Uruoca', 23, 231390, 23011, '11ª REGIAO SOBRAL', '2020-07-30 00:00:00', 31, 13840.0, 453, 16, 15, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-06-05 00:00:00', 23, 3015268.0, 14208, 1285, 202, 6, ' ', ' ', 1.0], ['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '2020-04-02 00:00:00', 14, 3015268.0, 370, 15, 4, 1, ' ', ' ', 1.0], ['Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '2020-06-10 00:00:00', 24, 30586.0, 108, 4, 7, 0, ' ', ' ', 0.0], ['Sudeste', 'ES', 'Guaçuí', 32, 320230, 32004, 'SUL', '2020-06-03 00:00:00', 23, 30867.0, 43, 1, 3, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Nova Roma', 52, 521490, 52007, 'NORDESTE II', '2020-08-10 00:00:00', 33, 3264.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'GO', 'Castelândia', 52, 520505, 52015, 'SUDOESTE I', '2020-05-26 00:00:00', 22, 3435.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Coroatá', 21, 210360, 21007, 'CODO', '2020-06-15 00:00:00', 25, 65296.0, 238, 0, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'MA', 'Vitorino Freire', 21, 211300, 21002, 'BACABAL', '2020-08-11 00:00:00', 33, 31523.0, 1392, 12, 24, 2, ' ', ' ', 0.0], ['Sudeste', 'MG', 'Taquaraçu de Minas', 31, 316830, 31016, 'BELO HORIZONTE/ NOVA LIMA/ CAETE ', '2020-05-23 00:00:00', 21, 4077.0, 0, 0, 0, 0, ' ', ' ', 1.0], ['Sudeste', 'MG', 'Andrelândia', 31, 310280, 31090, 'LIMA DUARTE', '2020-08-18 00:00:00', 34, 12224.0, 49, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Dourados', 50, 500370, 50003, 'DOURADOS', '2020-06-01 00:00:00', 23, 222949.0, 306, 27, 2, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MS', 'Paranhos', 50, 500635, 50003, 'DOURADOS', '2020-04-01 00:00:00', 14, 14228.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Rondonópolis', 51, 510760, 51013, 'SUL MATOGROSSENSE', '2020-06-14 00:00:00', 25, 232491.0, 497, 52, 12, 0, ' ', ' ', 0.0], ['Centro-Oeste', 'MT', 'Feliz Natal', 51, 510370, 51014, 'TELES PIRES', '2020-05-30 00:00:00', 22, 14192.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Anajás', 15, 150070, 15014, 'MARAJO II', '2020-05-08 00:00:00', 19, 29277.0, 1, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'PA', 'Breves', 15, 150180, 15014, 'MARAJO II', '2020-05-23 00:00:00', 21, 102701.0, 432, 7, 50, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Guarabira', 25, 250630, 25002, '2ª REGIAO', '2020-05-30 00:00:00', 22, 58833.0, 557, 12, 3, 0, ' ', ' ', 0.0], ['Nordeste', 'PB', 'Areia', 25, 250110, 25003, '3ª REGIAO', '2020-07-29 00:00:00', 31, 22819.0, 309, 11, 2, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Salgadinho', 26, 261210, 26006, 'LIMOEIRO', '2020-04-21 00:00:00', 17, 10919.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PE', 'Terra Nova', 26, 261520, 26011, 'SALGUEIRO', '2020-07-16 00:00:00', 29, 10096.0, 6, 0, 1, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Currais', 22, 220323, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-04-18 00:00:00', 16, 4954.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'PI', 'Corrente', 22, 220290, 22002, 'CHAPADA DAS MANGABEIRAS', '2020-05-01 00:00:00', 18, 26644.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Sabáudia', 41, 412270, 41016, '16ª RS APUCARANA', '2020-05-10 00:00:00', 20, 6827.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'PR', 'Porto Rico', 41, 412020, 41014, '14ª RS PARANAVAI', '2020-08-03 00:00:00', 32, 2559.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Santa Maria Madalena', 33, 330460, 33009, 'SERRANA', '2020-07-28 00:00:00', 31, 10404.0, 75, 0, 2, 0, ' ', ' ', 0.0], ['Sudeste', 'RJ', 'Seropédica', 33, 330555, 33005, 'METROPOLITANA I', '2020-06-26 00:00:00', 26, 82312.0, 429, 4, 23, 0, ' ', ' ', 1.0], ['Nordeste', 'RN', 'Pendências', 24, 240990, 24008, '8ª REGIAO DE SAUDE - ACU', '2020-06-16 00:00:00', 25, 15129.0, 93, 6, 5, 0, ' ', ' ', 0.0], ['Nordeste', 'RN', 'São José do Campestre', 24, 241230, 24005, '5ª REGIAO DE SAUDE - SANTA CRUZ', '2020-05-25 00:00:00', 22, 12856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Primavera de Rondônia', 11, 110147, 11002, 'CAFE', '2020-04-20 00:00:00', 17, 2856.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RO', 'Alvorada DOeste', 11, 110034, 11003, 'CENTRAL', '2020-07-01 00:00:00', 27, 14411.0, 18, 0, 1, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '2020-05-18 00:00:00', 21, 21926.0, 12, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '2020-08-19 00:00:00', 34, 11950.0, 237, 3, 4, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Jari', 43, 431113, 43002, 'REGIAO 02', '2020-08-12 00:00:00', 33, 3503.0, 2, 0, 0, 0, ' ', ' ', 0.0], ['Sul', 'RS', 'Vila Flores', 43, 432330, 43025, 'REGIAO 25', '2020-08-23 00:00:00', 35, 3385.0, 77, 5, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Porto Belo', 42, 421350, 42005, 'FOZ DO RIO ITAJAI', '2020-06-06 00:00:00', 23, 21388.0, 26, 2, 1, 0, ' ', ' ', 0.0], ['Sul', 'SC', 'Presidente Nereu', 42, 421410, 42004, 'ALTO VALE DO ITAJAI', '2020-04-13 00:00:00', 16, 2287.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Nossa Senhora Aparecida', 28, 280445, 28003, 'ITABAIANA', '2020-06-11 00:00:00', 24, 8796.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Nordeste', 'SE', 'Japoatã', 28, 280340, 28007, 'PROPRIA', '2020-04-28 00:00:00', 18, 13434.0, 1, 1, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sud Mennucci', 35, 355230, 35022, 'LAGOS DO DRS II', '2020-06-11 00:00:00', 24, 7718.0, 5, 0, 0, 0, ' ', ' ', 0.0], ['Sudeste', 'SP', 'Sandovalina', 35, 354550, 35112, 'ALTA SOROCABANA', '2020-06-13 00:00:00', 24, 4302.0, 0, 0, 0, 0, ' ', ' ', 0.0], ['Norte', 'TO', 'Gurupi', 17, 170950, 17005, 'ILHA DO BANANAL', '2020-07-23 00:00:00', 30, 86647.0, 717, 39, 7, 1, ' ', ' ', 0.0], ['Norte', 'TO', 'Riachinho', 17, 171855, 17002, 'BICO DO PAPAGAIO', '2020-05-20 00:00:00', 21, 4645.0, 2, 0, 0, 0, ' ', ' ', 0.0]]
lista = [['norte', 2 , 3, 4], ['llll', 25, 24, 'kok'], ['lol', 2, 4, 6]]
print(lista[0][1])
lista[0].remove([1])

lista = [4, 6, 7, 8]
bl = [20]

if sum(lista) == sum(bl):
    print(sum(lista))
else:
    print('Os dados da soma dos municípios divergem do estado para data 18/08/2020')


listaMunicipios = [['Norte', 'RR', 'Amajari', 14, 140002, 14001, 'CENTRO NORTE', '18/08/2020', 34, 12796, 277, 0, 6, 0, ' ', ' ', 0], ['Norte', 'RR', 'Alto Alegre', 14, 140005, 14001, 'CENTRO NORTE', '18/08/2020', 34, 15510, 493, 25, 14, 0, ' ', ' ', 1], ['Norte', 'RR', 'Boa Vista', 14, 140010, 14001, 'CENTRO NORTE', '18/08/2020', 34, 399213, 29978, 408, 444, 5, ' ', ' ', 1],['Norte', 'RR', 'Bonfim', 14, 140015, 14001, 'CENTRO NORTE', '18/08/2020', 34, 12409, 609, 20, 11, 0, ' ', ' ', 1],['Norte', 'RR', 'Cantá', 14, 140017, 14001, 'CENTRO NORTE', '18/08/2020', 34, 18335, 839, 7, 9, 0, ' ', ' ', 1], ['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '18/08/2020', 34, 21926, 750, 2, 8, 0, ' ', ' ', 0], ['Norte', 'RR', 'Caroebe', '14', 140023, 14002, 'SUL', '18/08/2020', 34, 10169, 832, 4, 4, 0, ' ', ' ', 0],['Norte', 'RR', 'Iracema', 14, 140028, 14002, 'SUL', '18/08/2020', 34, 11950, 234, 1, 4, 0, ' ', ' ', 0],['Norte', 'RR', 'Mucajaí', 14, 140030, 14001, 'CENTRO NORTE', '18/08/2020', 34, 17853, 1036, 19, 12, 0, ' ', ' ', 1],['Norte', 'RR', 'Normandia', 14, 140040, 14001, 'CENTRO NORTE', '18/08/2020', 34, 11290, 272, 0, 9, 0, ' ', ' ', 0], ['Norte', 'RR', 'Pacaraima', 14, 140045, 14001, 'CENTRO NORTE', '18/08/2020', 34, 17401, 1246, 17, 26, 1, ' ', ' ', 0], ['Norte', 'RR', 'Rorainópolis', 14, 140047, 14002, 'SUL', '18/08/2020', 34, 30163, 1401, 8, 20, 0, ' ', ' ', 0], ['Norte', 'RR', 'São João da Baliza', 14, 140050, 14002, 'SUL', '18/08/2020', 34, 8201, 736, 0, 3, 0, ' ', ' ', 0],['Norte', 'RR', 'São Luiz', 14, 140060, 14002, 'SUL', '18/08/2020', 34, 7986, 197, 2, 2, 0, ' ', ' ', 0], ['Norte', 'RR', 'Uiramutã', 14, 140070, 14001, 'CENTRO NORTE', '18/08/2020', 34, 10559, 596, 2, 2, 0, ' ', ' ', 0]]

a=0
while a <= 14:
    print(listaMunicipios[a][2],':',listaMunicipios[a][10])
    a = a+1
else:
    print('Acabou o programa')

numerosEstadoRR = [40183]

numerosMunicipiosRR = [277, 493, 29978, 609, 839, 750, 832, 234, 1036, 272, 1246, 1401, 736, 197, 596]

if sum(numerosMunicipiosRR) == sum(numerosEstadoRR):
    print(sum(numerosMunicipiosRR))
else:
    print('Os dados da soma dos municípios divergem do estado para data 18/08/2020')

numerosMunicipiosRR = [277, 493, 29978, 609, 839, 750, 832, 234, 1036, 272, 1246, 1401, 736, 197, 596]
print(sum(numerosMunicipiosRR))