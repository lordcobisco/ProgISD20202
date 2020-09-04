

list = []
print(list)

lista = (list)
print(lista) 

lista = ['0 carro ', ' peixe ', 123,  1097.50 , True ]
print(list) 
novalista = ['Novalista', lista]
print(novalista)

# Acessado um carro 

string = lista[0]
print(string)
print(lista[0])
print(lista[1])
print(lista[2])
print(novalista[0])
print(novalista[1])
print(novalista[1][0])
print(novalista[1][1])
print(novalista[1][2])


# função len
lista = ['0 carro ', ' peixe ', 123,  1097.50 , True ]
novalista = ['Andre', lista]
print(len(lista))
print(len(novalista))
print(len(novalista[1]))


#operadores + e - 

lista = ['0 carro ', ' peixe ', 123,  1097.50 , True ]
novalista = ['Andre', lista]
print(lista+lista)
print(len(lista+lista))
print(len(lista+[1])

print(lista*3)
print(len(lista*100)


#operador in

lista = ['0 carro ', ' peixe ', 123,  1097.50 , True ]
print('peixe' in lista)
print('peixe' not in lista)

print('peixe' in lista)
if('peixe' in lista):
    print('existe a palavra peixe como elemento na lista')

#lista de numeros 

listaDeNumeros = [ 56 , 3 , 96 , 23 , 4 , 8 , 2 ]
print(max(listaDeNumero))
print(min(listaDeNumeros))
print(sum(listaDeNumero)/len(listaDeNumeros))



lista = ['0 carro ', ' peixe ', 123,  1097.50 , True ]
print(lista[-1])
print(lista[-2])
print(lista[-3])


#Operador append

livros = ['java', ' sqlsever', 'delphi', 'python' ]
print(livros)
livros.append('android')
print(livros)

#operador insert e pop

livros.insert(0,'oracle')
print(livros)


print(livros.pop())
print(livros)
print(livros.pop(1))
print(livros)

livros.remove('sqlsever')
print(livros)
livros.sort()
print(livros)
livros.reverse()
print(livros)

numeros = [1,2,3,8,2,4,8,2]
numero.sort()
numero.reverse()
print(numeros)

lista = ['0 carro ', ' peixe ', 'andre',  'andre' ]
print(lista.count('andre'))
list.remove('andre')
print(lista)

a = [81,82,83]
b = a
print(b is a)
b[1] = 999
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
tupla = ()
print(tupla)
tupa = tupla()

tupla = ('Maria', 'João', 'Carlos', ' Andre', ' Severino')
print(tupla(1:3))
tupla[0] = 'Ana'

p = 'python'

print(p[0:0])
print(p[0:1])
print(p[1:2])
print(p[2:3])
print(p[3:4])
print(p[4:5])
print(p[5:6])
print(p[6:6])

print(p[:1])
print(p[:2])
print(p[:3])
print(p[:4])
print(p[:5])
print(p[:6])
print(p[:6])

print(p[0:1])
print(p[0:2])
print(p[0:3])
print(p[0:4])
print(p[0:5])
print(p[0:6])
print(p[0:6])

print('/n/n')

print(p[0:])
print(p[1:])
print(p[2:])
print(p[3:])
print(p[4:])
print(p[5:])
print(p[6:])



lista = ['Brasil', 76, '25/02/2020', 9, 210147125, 0, 0 , 0 , 0], ['Brasil', 76, '26/02/2020', 9, 210147125, 1, 1 , 0 , 0]
casosAcumuladosNorte.append(lista [176][10])
asosAcumuladosNorte.append(lista [176][10])
.
.
.
casosAcumuladosNorte.append(lista[350][10])

print(casosAcumulaodsNorte)

'''
'''

#dicionario

dadosCovid  {}
print(dadosCovid)
dadosCovid = dict()
print(dadosCovid)

dadosCovidCasosNovos = {'Brasil': [0,1,0,0,1,0,0,0,1,4,6], 'Nordeste': [0,0,4,4,6,17]}
print(dadosCovidCasosNovos)
print(dadosCovidCasosNovos['Brasil'])


population ={
    "Brasil": 210147125
    "Nordeste": "MA":7075181, 'PI':3273227, 'CE': 9132078, 'RN': 3506853, 'PE': 95577071, 'AL': 33763908},
    "Norte":{'RO': 1777225, 'AC': 881935, 'AM':4144597, 'RR': 605761, 'PA': 8602865, 'AP': 845731, 'TO':1572866},
    "Suldeste":{'MG': 21168791, 'ES':4018650, 'RJ':17264943, 'SP': 45919049},
    "Sul": {'PR': 11433957, 'SC': 7164788, 'RS': 11377239},
    "Centro-Oeste":{'MS': 2778986, 'MT': 3484466. 'GO':7018354, 'DF':3015268},
}
temp = population['Norte']
print(temp['AC'])