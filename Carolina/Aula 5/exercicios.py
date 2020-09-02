'''
Carolina Karla de Souza Evangelista
Matricula 202002003

>>>> Reproduzindo exercicos da aula 5 <<<<

'''

### listas ###
lista = ['O carro', 'o peixe', 123, 111]
print(lista)
nova_lista = ['pedra', lista]
print(nova_lista)
print(lista[0])
print(lista[1])
print(nova_lista[1])
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(len(lista))
print(len(nova_lista))
print(nova_lista+lista)
print(nova_lista*3)
print('o peixe' in lista)
num = [10, 20, 27, 32, 38, 42, 13]
print(max(num))
print(min(num))
print(sum(num))
livros = ['java', 'python', 'odisseia no espaco', '1984']
livros.append('admiravel mundo novo')
print(livros)
livros.insert(0, 'admiravel mundo novo')
print(livros)
livros.remove('1984')
print(livros)
livros.sort()
print(livros)
livros.reverse()
print(livros)
print(livros.count('python'))

a = [81, 82, 83]
b = a
print(a is b)


### tuplas ###

tupla = (1, 2, 3, 4)
print(tupla)
tupla_2 = ("maria", "joao", "carlos")
print(tupla_2[0])

### dicionarios ###
agenda = {}
print(agenda)
agenda = {"Maria": [99887766, 889977888], "Pedro": [32324455]}
print(agenda)