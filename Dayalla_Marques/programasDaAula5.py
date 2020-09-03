#############################################
# AQUI ESTÃOS OS PROGRAMAS FEITOS NA AULA 5 #
#############################################

listaAula = []
print(listaAula)

listaAula = list()
print(listaAula)

listaAula = ['praia', 'calçada', 4536, 2222.77, False]
print(listaAula)
novaListaAula = ['NovalistaAula', listaAula]
print(novaListaAula)
lista3 = [listaAula, novaListaAula, 2345]
print(lista3)

###########################
# Para acessar a lista
###########################

nomedalista = listaAula[0]
print(nomedalista)
print(listaAula[0])
print(listaAula[1])
print(listaAula[2])
print(listaAula[3])
print(listaAula[4])
'''
Se a lista tivesse mais elementos:

print(listaAula[5]) 
print(listaAula[6])
print(listaAula[7])
print(listaAula[8])
print(listaAula[9])
'''

print(novaListaAula[0])
print(novaListaAula[1])
print(novaListaAula[1][0])
print(novaListaAula[1][1])
print(novaListaAula[1][2])


##############################
# Tamanho da lista
#####################

listaAula = ['praia', 'calçada', 4536, 2222.77, False]
print(listaAula)
novaListaAula = ['NovalistaAula', listaAula]
print(novaListaAula)
lista3 = [listaAula, novaListaAula, 2345]
print(lista3)

print(len(listaAula))
print(len(novaListaAula))
print(len(lista3[1]))

################################
# Operadores "+" e "*"
#################################

listaAula = ['praia', 'calçada', 4536, 2222.77, False]
novaListaAula = ['NovalistaAula', listaAula]

print(listaAula+listaAula)
print(len(listaAula+listaAula))
print(len(listaAula+[1]))

print(listaAula*6)
print(len(listaAula*10))

#######################
#  in
#######################
listaAula = ['praia', 'calçada', 4536, 2222.77, False]

print('calçada' in listaAula)
#if('calçada' in lista):
    #print('calçada tá na lista')

#######################
# max, min, sum
#######################

numbers = [345, 56, 5.4, 4, 6]

print(max(numbers))

print(min(numbers))

print(sum(numbers)/len(numbers))


listaAula = ['praia', 'calçada', 4536, 2222.77, False]
print(listaAula[-1])
print(listaAula[-2])
print(listaAula[-3])

####################
#operador append - exemplos os mesmos que estavam nos slide, refiz
####################
livros = ['Java','SqlServer','Delphi','Python']
print(livros)
livros.append('Python')
print(livros)

##########################
#operador insert e pop
##########################

livros.insert(0,'Oracle')
print(livros)
print(livros.pop())
print(livros)
print(livros.pop(1))
print(livros)

livros.remove('Python')
print(livros)
livros.sort()
print(livros)
livros.reverse()
print(livros)

listadenumeros = [4,5,6,3,2,4,5,6,7]
listadenumeros.sort()
listadenumeros.reverse()
print(listadenumeros)


listaAula = ['praia', 'calçada', 4536, 2222.77, False]
print(listaAula.count('praia'))
listaAula.remove('praia')
print(listaAula)


a = [22, 23, 24]
b = a
print(b is a)
b[1] = 999
print(a)

a = [22, 23, 24]
b = [22, 23, 24]
print(b is a)
print(b == a)

listanumerica = [10,20,30,40,50,60,70,80,90]
print(listanumerica.index(60))
print(listanumerica[2:7])

tupla1 = (1,2,3,4)
print(tupla1)
tupla1 = (1,)
print(tupla1)
tupla1 = ()
print(tupla1)
tupla1 = tuple()
print(tupla1)

tupla = ('Engenharia', 'Matemática', 'Ciência','Física', 'Computação')
print(tupla[2:4])


d = 'violao'
print(d[0:0])
print(d[0:1])
print(d[1:2])
print(d[2:3])
print(d[3:4])
print(d[4:5])
print(d[5:6])
print(d[6:6])
print('\n')

print(d[:1])
print(d[:2])
print(d[:3])
print(d[:4])
print(d[:5])
print(d[:6])
print('\n')

print(d[0:0])
print(d[0:1])
print(d[0:2])
print(d[0:3])
print(d[0:4])
print(d[0:5])
print(d[0:6])

print('\n\n')

print(d[:])
print(d[1:])
print(d[2:])
print(d[3:])
print(d[4:])
print(d[5:])
print(d[6:])

##################
# Dicionário
##################
dadosd = {}
print(dadosd)
dadosd = dict()
print(dadosd)

dadosNovos = {'BRASIL':[0,0,0,0,0,0], 'NordesE':[0,0,7, 7, 7, 7]}
print(dadosNovos)
print(dadosNovos['BRASIL'])


variavelPopulacao={

  "Brasil": 210147125,
  "Nordeste": {'MA':7075181, 'PI':3273227, 'CE':9132078, 'RN':3506853, 'PB':4018127, 'PE':9557071, 'AL':3337357, 'SE':2298696, 'BA':14873064}, 
  "Norte": {'RO':1777225, 'AC':881935, 'AM':4144597, 'RR': 605761, 'PA':8602865, 'AP':845731, 'TO':1572866}, 
  "Suldeste": {'MG':21168791,'ES':4018650, 'RJ':17264943, 'SP':45919049}, 
  "Sul": {'PR':11433957, 'SC':7164788, 'RS':11377239},
  "Centro-Oeste": {'MS':2778986, 'MT':3484466, 'GO':7018354, 'DF':3015268}
}

print(variavelPopulacao['Sul']['RS'])



lista = [['Brasil',	76,'25/02/2020',9,210147125,0,0,0,0],['Brasil',76,'26/02/2020',9,210147125,1,1,0,0]]


# Casos acumulados na região Norte

regiaoNorte = list()
regiaoNorte.append(lista[176][10])
regiaoNorte.append(lista[177][10])
regiaoNorte.append(lista[350][10])
print(regiaoNorte)


