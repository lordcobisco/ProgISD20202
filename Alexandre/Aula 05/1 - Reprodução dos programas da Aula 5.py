#LISTAS:
lista = ['O carro','peixe',99,True]
print(lista)
novalista = [lista, "O carro","joao","peixe"]
print(novalista)

#OPERAÇÕES COM LISTAS: 

#Operações com listas - Operador de acesso
print(lista[0])
print(lista[2])
print(novalista[1])
print(novalista[0][2])

#Operações com listas - Comprimento de uma lista
print(len(lista))
print (len(novalista))

#Operações com listas - Concatenação e multiplicação 

print(lista+lista)
print(len(lista+lista))
print(lista*3)
print(len(lista*99))

#Operações com listas - Verificar existência de um item 
print('peixe' in lista)

##Operações com listas - Valores mínimos, máximos e soma
lista_numeros = [80, 30, 109.5, 25, 285.5]
print(sum(lista_numeros))
print(min(lista_numeros))
print(max(lista_numeros))

#Encontrar elemento em da posição final para inicial 
print(novalista[-1])
print(novalista[-2])
print(novalista[-3])
print(novalista[-4])

#MÉTODOS DAS LISTAS: 
# Append
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
livros.append('Android')
print(livros)

# Insert
livros = ['Java','SqlServer', 'Delphi','Python']
livros.insert(0,'Oracle')
print(livros)

# Pop
print(livros)
print(livros.pop())
print(livros)
print(livros.pop(1))
print(livros)

# Remove
livros.remove('SqlServer')
print(livros)

# Sort
livros.sort()
print(livros)

# Reverse 
livros.reverse()
print(livros)


# Count 
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android','Oracle']
print(livros.count('Oracle'))

# Index
lista = [10,20,30,40,50,60,70,80,90]
print(lista.index(60))

# Aliasing and cloning 
a = [81,82,83]
b = a
print(b is a)
b[1] = 999
print(a)

a = [81,82,83]
b = [81,82,83]
print(b is a)
print(b == a)

b = a[:]
print (a == b)
print (a is b)


#TUPLAS 

tupla = (1, 2, 3, 4)
print(tupla)
tupla = (1, )
print(tupla)
tupla = ()
print(tupla)

#Acesso aos valores de uma tupla
tupla = ("Maria", "Joao", "Carlos", "Alexandre", "André") 
print(tupla[3])
print(tupla[1:2])

#tupla[0] = "Ana" - Não é permitodo atualizar valores dentro de uma tupla, irá dar erro 

#Fatiamento 

p = "python"
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

print(p[:])
print(p[1:])
print(p[2:])
print(p[3:])
print(p[4:])
print(p[5:])
print(p[6:])

#DICIONÁRIOS:

#Manipulação de dicionários: 
agenda = {}
print(agenda)

agenda = {"Maria": [99887766, 99887755]}
print(agenda)

agenda = {"Maria": [99887766, 99887755], "Pedro": [92345678], "Joaquim": [99887711, 99665533]}
print(agenda)

print(agenda["Maria"])

agenda["Pedro"] = [87654433]
print(agenda)
