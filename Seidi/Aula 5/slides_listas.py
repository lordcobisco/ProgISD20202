# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:07:42 2020

@author: seidi
"""

# criando lista e lista de listas
lista = ['O carro', 'peixe', 123, 111]
nova_lista = ['pedra', lista]
print(lista[0])
print(lista[2])
print(nova_lista[1])
print(nova_lista[1][2])

# ordem inversa de acesso
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# concatenação e multiplicação
outra_lista = lista + nova_lista
print(outra_lista)
print(3*lista)

# verificando existencia de elemento em lista
print('peixe' in lista)

numeros = [14.55, 67, 89.88, 10, 21.5]
print(min(numeros))
print(max(numeros))
print(sum(numeros))

# Append, insert e pop
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.append('Android')
print(livros)

livros.insert(0, 'Oracle')

livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
print(livros.pop())
print(livros)

livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros.pop(1))

# Remove
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Andoird', 'Oracle']
print(livros)
livros.remove('Oracle')
print(livros)
livros.remove('Oracle')
print(livros)
livros.remove('Oracle') # erro

# Index
lista = [66.25, 333, -1, 333, 1, 1234.5]
print(lista.index(333))


# Sort, Reverse e Count
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Andoird', 'Oracle']
livros.sort()
print(livros)

livros.reverse()
print(livros)

print(livros.count('Oracle'))

# Aliasing e Cloning
# Aliasing
a = [81,82,83]
b = a
print(a is b)

a = [81,82,83]
b = [81,82,83]

print(a == b)
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

# Cloning
a = [81,82,83]

b = a[:]
print(a == b)
print(a is b)

b[0] = 5
print(a)
print(b)