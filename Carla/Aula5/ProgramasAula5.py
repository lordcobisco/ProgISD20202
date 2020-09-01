'''
lista = []
print(lista)

lista = list ()
print(lista)

lista = ['o carro ', 'o peixe', 123, 1097, 55, True]
print(lista)
novaLista = ['NovaLista', lista]
print(novaLista)


#Acessando uma lista

string = lista[0]
print(string)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(novaLista[0])
print(novaLista[1])
print(novaLista[1][0])
print(novaLista[1][1])
print(novaLista[1][2])
print(novaLista[1][3])
'''
'''
#Função Len
lista = ['o carro ', 'o peixe', 123, 1097, 55, True]
novalista = ['André', lista]
print(len(lista))
print(len(novalista))
print(len(novalista[1]))
'''
'''
#Operadores + e *

lista = ['o carro ', 'o peixe', 123, 1097, 55, True]
novalista = ['André', lista]
print(lista+lista)
print(len(lista+lista))
print(len(lista+[1]))
print(lista*3)
print(len(lista*3))
print(len(lista*100))
'''
'''
#Operador in

lista = ['o carro ', 'o peixe', 123, 1097, 55, True]
print('peixe' in lista)
print('o peixe' in lista)
print('o peixe' not in lista)
if('o peixe' in lista):
    print('Existe a palavra peixe como um dos elementos da lista')
'''
'''
#Operadores Max, Min, Sum
listaDeNumeros = [56,3,96,23,4,8,2,9]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros)/len(listaDeNumeros))

'''
'''
lista = ['o carro ', 'o peixe', 123, 1097, 55, True]
print(lista[-1])
print(lista[-2])
print(lista[-3])
'''
'''
#Operador Append

livros = ['Java', 'sqlServe', 'delphi', 'python']
print(livros)
livros.append('android')
print(livros)

#Operador insert e pop
livros.insert(0,'oracle')
print(livros)

print(livros.pop())
print(livros)

livros.remove('sqlServe')
print(livros)
livros.sort()
print(livros)
livros.reverse()
print(livros)

numeros = [1,2,3,8,2,4,8,2]
numeros.sort()
numeros.reverse()
print(numeros)
'''
'''
lista = ['Brasil', 76, '25/02/2020', 9, 210147125, 0, 0,	0,	0],[76,'26/02/2020', 9, 210147125,	1, 1, 0, 0]
casosAcumuladosNorte = list()
casosAcumuladosNorte.append(lista[176][10])
casosAcumuladosNorte.append(lista[177][10])
casosAcumuladosNorte.append(lista[350][10])
print(lista) 
'''
'''
lista = ['o carro ', 'o peixe', 'André','André']
print(lista.count('André'))
lista.remove('André')
print(lista)
'''
'''
a = [81,82,83]
b = a
print(b is a)
b[1] = 999
print(a)

a = [81,82,83]
b = [81,82,83]
print(b == a)
print(b is a)
'''
'''
lista = [10,20,30,40,50,60,70,80,90]
print(lista.index(60))
print(lista[1:6])
'''
'''
tupla = (1,2,3,4)
print(tupla)
tupla = (1,)
print(tupla)
tupla = ()
print(tupla)
tupla = tuple
print(tupla)

tupla = ('Maria', 'João', 'Carlos','André', 'Severino')
print(tupla[1:3])
tupla[0] = 'Ana'
'''
'''
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

print(p[0:0])
print(p[0:1])
print(p[0:2])
print(p[0:3])
print(p[0:4])
print(p[0:5])
print(p[0:6])
print(p[0:6])

print(p[0:])
print(p[1:])
print(p[2:])
print(p[3:])
print(p[4:])
print(p[5:])
print(p[6:])
'''
'''
dadosCovid = {}
print(dadosCovid)
dadosCovid = dict()
print(dadosCovid)

dadosCovidCasosNovos = {'Brasil':[0,1,0,0,1,0,0,0,1,4,6]'Nordeste':[0,0,4,6,17]}
print(dadosCovidCasosNovos)
'''
