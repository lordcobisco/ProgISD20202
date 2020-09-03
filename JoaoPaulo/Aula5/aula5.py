

#criação de uma lista
'''
lista = ['o carro  ', 'peixe', 123,1111111, True]
'''
#print(lista)
'''
novalista = ['novalista', lista]

print(novalista)
'''

#Acessando uma lista
'''
string = lista[0]

print(string)

print(lista[3])

print(novalista[1][2])
'''
#Comprimento de uma lista
'''
#função len
lista = ['o carro', 'peixe',  123, 1097.1561, True]
novaLista = ['João', lista]

print(len(lista))
print(len(novaLista))#retorna apenas o tamanho dessa lista
print(len(novaLista[1]))#retorna quantos valores existem dentro do indice 1

'''''
#Concatenação de lista e multiplicação
'''
#operadores + e -
lista = ['o carro', 'peixe',  123, 1097.1561, True]
novaLista = ['João', lista]

print(lista+lista)
print(len(lista+lista))
print(len(lista+[1]))
print(lista*3) #triplica a mesma lista

'''
#Verificador de existência
'''
#operador in
lista = ['o carro', 'peixe',  123, 1097.1561, True]

#print('peixe' in lista)#verificando se existe a palavra na lista

if('peixe' in lista):
    print("existe peixe na lista")
'''
#Verificação de máximos e mínimos e soma
'''
listanumerica = [14.7,52,96,3,2]
print(max(listanumerica))#maximo
print(min(listanumerica))#menor
print(sum(listanumerica))#soma
'''
'''
lista = ['o carro', 'peixe',  123, 1097.1561, True]

print(lista[-1])#pega da direita para esquerda
'''
#operador apend
'''

livros = ['java',  'sqlserver', 'delph', 'python']

print(livros)

livros.append('Android')#anexa novo conteudo
print(livros)

'''
#operador insert e pop
'''
livros.insert(0,'Oracle') #escolhe a posição e diz o que vai adicionar
print(livros)

print(livros.pop(2))#remove um elemento na posicao do parentenses
print(livros)
'''
#operador remove
'''
livros.remove("java")#remove elemento especifico
print(livros)
'''
#Operador index

'''
lista = [1,20,3,34,5,60,7]
print(lista.index(60)) #retorna a posicao daquele valor

print(lista[1:6])#diz os elementos que se quer pegar ate a posicao imediatamente antes
'''

'''
#tupla = ('maria', 'joao', 'carlos')

print(tupla[0:2])#tupla nao pode ser alterada

p = 'python'

print(p[0:1])
print(p[0:2])
print(p[0:3])
print(p[0:4])
print(p[0:5])
print(p[0:6])

'''
#criação de dicionario
'''
dicCovid = {}
print(dicCovid)
dicCovid = dict()
print(dicCovid)

dicCovid_novos = {'Brasil':[0,1,0,0,1,0,0,0,1,4,6], 'Nordeste':[0,0,4,4,6,17]}
print(dicCovid_novos)
print(dicCovid_novos['Brasil'])
'''

