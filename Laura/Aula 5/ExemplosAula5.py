#Exemplos realizados na Aula 05

lista = []
print(lista)

lista = list()
print(lista)

lista = ['O carro ', 'Peixe', 123, 1097.55, True]
print(lista)
novaLista = ['Novalista', lista]
print(novaLista)

#Acessando uma lista
string = lista[0] #acessou o elemento que está na posição 0 da string acima que, no caso, é O carro
print(string)
print(lista[1])
print(novaLista[1][2])

#função len
lista = ['O carro ', 'Peixe', 123, 1097.55, True]
novaLista = ['André', lista]
print(len(lista))
print(len(novaLista))
print(len(novaLista[1]))


#operadores + e *
lista = ['O carro ', 'Peixe', 123, 1097.55, True]
novaLista = ['André', lista]
print(lista+lista)
print(len(lista+lista))
print(len(lista+[1]))

print(lista*3)
print(len(lista*100))


#operador in
lista = ['O carro ', 'Peixe', 123, 1097.55, True]
print('Peixe' in lista) #verificar se existe o elemento peixe dentro da lista. Retorna verdadeiro ou falso
#Ou
print('Peixe' not in lista)
#Ou
if('Peixe' in lista):
    print('Existe a palavra Peixe como um dos elementos da lista')

#Operadores max, min, sum (soma)
listaDeNumeros = [56.3,96,23,4,8,2,9]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros))
print(sum(listaDeNumeros)/len(listaDeNumeros))


#Operadores de indexação
lista = ['O carro ', 'Peixe', 123, 1097.55, True]
print(lista[-1]) #quando usa o negativo, começa a acessar os elementos da direita para esquerda
print(lista[-2])
print(lista[-3])


#Operador append
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.append('Android') #adiciona o novo conteúdo aos livros
print(livros)

#Operador insert e pop
livros.insert(0, 'Oracle') #colocou oracle na posição 0 da lista
print(livros)

print(livros.pop()) #pega a última palavra do vetor e apaga (android). Tira o último elemento da lista
print(livros)

livros.remove('SqlServer')
print(livros)

livros.sort() #organiza os livros por ordem alfabética
print(livros)

livros.reverse() #inverte a ordem de apresentação da lista
print(livros)

a=[81,82,83]
b=a
print(b is a)
b[1] = 999
print(a)

a=[81,82,83]
b=[81,82,83] #caixas diferentes com o mesmo conteúdo
print(b is a) #vai retornar falso, pois não são a mesma caixa, apenas tem o mesmo conteúdo
print(b == a) #aqui está perguntando se o conteúdo dos vetores é o mesmo. Retorna verdadeiro


lista = [10,20,30,40,50,60,70,80,90]
print(lista.index(60)) #qual a posição do vetor que ele tem
print(lista[1:6]) #pegar do vetor 1 até a posição imediata antes da 6ª



tupla = (1,2,3,4)
print(tupla)
tupla = (1,)
print(tupla)
tupla = ()
print(tupla)
tupla = tuple()
print(tupla)

tupla = ('Maria', 'João', 'Carlos', 'André', 'Severino')
print(tupla[0:3])
#tupla[0] = 'Ana' - não pode, pois a tupla não pode alterar depois de criada, ou seja, alterar a posição com o nome ana não é possível


p = 'Python' 
print(p[0:0])
print(p[0:1])
print(p[1:2])
print(p[2:3])
print(p[3:4])
print(p[4:5])
print(p[5:6])
print(p[6:6])


#Dicionário
dadosCovid = {}
print(dadosCovid)
dadosCovid = dict()
print(dadosCovid)

dadosCovidCasosNovos = {'Brasil' :[0,1,0,0,1,0,0,0,1,4,6], 'Nordeste':[0,0,4,4,6,17]}
print(dadosCovidCasosNovos)
print(dadosCovidCasosNovos['Brasil']) #acessando os dados apenas do que quero, com base no dicionário que organizei
