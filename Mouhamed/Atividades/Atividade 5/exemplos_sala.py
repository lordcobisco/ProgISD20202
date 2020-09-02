
lista = []
print(lista)

lista = list()
print(lista)

lista = ['O carro   ', 'Peixe', 123, 1097.55, True]
print(lista)
novaLista = ['Novalista',lista]
print(novaLista)

'''
#Acessando uma lista
string = lista[0]
print(string)
print(lista[0])
print(lista[1])
print(lista[2])

print(novaLista[0])
print(novaLista[1])
print(novaLista[1][0])
print(novaLista[1][1])

print(novaLista[1][2])

'''

#função len
lista = ['O carro   ', 'Peixe', 123, 1097.55, True]
novaLista = ['Mouhamed', lista]
print(len(novaLista)) #2
print(len(lista)) #5


#operadores + e *
lista = ['O carro   ', 'Peixe', 123, 111]
novaLista = ['Mouhamed', lista]
print(lista+novaLista)
print(lista*3) #repete 3x o conteúdo


# operador in
lista = ['O carro   ', 'Peixe', 123, 1097.55]
print('Peixe' in lista) #true

if('Peixe' in lista):
    print('Existe a palavra Peixe como um dos elementos da lista')


#Operadores max, min, sum
listaDeNumeros = [56.3,96,23,4,8,2,9]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros)/len(listaDeNumeros)) #somatorio


lista = ['O carro   ', 'Peixe', 123, 1097.55, True] #inverso
print(lista[-1])
print(lista[-2])
print(lista[-3])


#operador append
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.append('Android')
print(livros)

#operador insert e pop

livros.insert(0,'Oracle')
print(livros)

print(livros.pop())
print(livros)
print(livros.pop(1))
print(livros)

livros.remove('SqlServer')
print(livros)
livros.sort()
print(livros)
livros.reverse()
print(livros)

numeros = [1,2,3,8,2,4,8,2]
numeros.sort()
numeros.reverse()
print(numeros)


lista = ['O carro   ', 'Peixe', 'André', 'André']
print(lista.count('André'))
lista.remove('André')
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
tupla = (1,)
print(tupla)
tupla = ()
print(tupla)
tupla = tuple()
print(tupla)

tupla = ('Maria', 'João', 'Carlos','andré', 'severinho')
print(tupla[1:3])
#tupla[0] = 'Ana'

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

print(p[0:0])
print(p[0:1])
print(p[0:2])
print(p[0:3])
print(p[0:4])
print(p[0:5])
print(p[0:6])

print('\n\n')

print(p[:])
print(p[1:])
print(p[2:])
print(p[3:])
print(p[4:])
print(p[5:])
print(p[6:])


dadosCovid = {}
print(dadosCovid)
dadosCovid = dict()
print(dadosCovid)

dadosCovidCasosNovos = {'Brasil':[0,1,0,0,1,0,0,0,1,4,6], 'Nordeste':[0,0,4,4,6,17]}
print(dadosCovidCasosNovos)
print(dadosCovidCasosNovos['Brasil'])


population ={
  "Brasil": 210147125,
  "Nordeste": {'MA':7075181, 'PI':3273227, 'CE':9132078, 'RN':3506853, 'PB':4018127, 'PE':9557071, 'AL':3337357, 'SE':2298696, 'BA':14873064}, 
  "Norte": {'RO':1777225, 'AC':881935, 'AM':4144597, 'RR': 605761, 'PA':8602865, 'AP':845731, 'TO':1572866}, 
  "Suldeste": {'MG':21168791,'ES':4018650, 'RJ':17264943, 'SP':45919049}, 
  "Sul": {'PR':11433957, 'SC':7164788, 'RS':11377239},
  "Centro-Oeste": {'MS':2778986, 'MT':3484466, 'GO':7018354, 'DF':3015268}
}

print(population['Norte']['AC'])



lista = [['Brasil',	76,'25/02/2020',9,210147125,0,0,0,0],['Brasil',76,'26/02/2020',9,210147125,1,1,0,0]]
casosAcumuladosNorte = list()
casosAcumuladosNorte.append(lista[176][10])
casosAcumuladosNorte.append(lista[177][10])
.
.
.
casosAcumuladosNorte.append(lista[350][10])

print(casosAcumuladosNorte)
'''