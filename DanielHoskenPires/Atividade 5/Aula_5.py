#Criação de listas
'''
lista = ['O carro ','Peixe', 123, 7.7, True, "Atualização"]
print (lista)

lista2 = [input ("Digite sua lista")]
print (lista2)

lista3 = [lista, lista2, "Daniel", 3,14, 7]
print (lista3)

#Operações com listas
#Operador de acesso

lista4 = ["O carro", "peixe", 123, 111]
novalista = ['pedra', lista4]
print (novalista)
print (lista4[0])
print (lista4[2])
print (novalista[1])
print (novalista[1][2]) 

#Comprimento de uma lista
lista = ["O carro", "peixe", 123, 111]
novalista = ['pedra', lista]
print (len(novalista))

#Concatenação e multiplicação
lista = ["O carro", "peixe", 123, 111]
novalista = ['pedra', lista]
print (lista+novalista)
print (lista*3)

#Verificando a existência de  itens em uma lista
lista = ["O carro", "peixe", 123, 111]
novalista = ['pedra', lista]
print (["O carro", "peixe", 123, 111] in novalista)
print (123 in novalista)
print ("pedra" in novalista)

#Valores mínimos, máximos e soma
numeros = [14.55, 67, 89.88, 10, 21.5]
print (min(numeros))
print (max(numeros))
print (sum(numeros))

#Métodos das listas
#Append (adicionar caractere na útlima posição)
livros = ["Java", 'Sqserver', "Delphi", "Python"]
livros.append ("Android")
print (livros)

#insert (insere caractere em posição especificada)
livros = ["Java", 'Sqserver', "Delphi", "Python"]
livros.insert (0, "Oracle")
print (livros)

#pop (deleta caracter em posição especificada)
livros = ["Java", 'Sqserver', "Delphi", "Python"]
print (livros)
print (livros.pop())
print (livros)

lista = ["O carro", "peixe", 123, 111]
print (lista)
print (lista.pop(2))
print (lista)

#remove (deleta caracter especificado)
livros = ["Oracle", "Java", 'Sqserver', "Delphi", "Python", "Android", "Oracle"]
print (livros)
livros.remove("Oracle")
print (livros)
livros.remove("Oracle")
print (livros)

#index (informa posição do caractere)
lista = [66.25, 333, -1, 333, 1, 1234.5, 333]
print (lista.index(1)) 

#sort (Organiza a lista em ordem)
livros = ["Oracle", "Java", 'Sqserver', "Delphi", "Python", "Android", "Oracle"]
livros.sort ()
print (livros)

#reverse (inverte a ordem da lista)
livros = ["Oracle", "Java", 'Sqserver', "Delphi", "Python", "Android", "Oracle"]
livros.reverse ()
print (livros) 

#count (conta a quantidade de caractere específico)
livros = ["Oracle", "Java", 'Sqserver', "Delphi", "Python", "Android", "Oracle"]
print (livros.count("Oracle")) 

#aliasing 
a = [81, 82, 83]
b = a 
print (a is b)

a = [81, 82, 83]
b = [81, 82, 83]

print (a == b)
print (a is b)
a = b
print (a == b)
print (a is b)

b[0] = 5
print (a) 

#cloning
a = [81, 82, 83]
b = a[:]

print (a == b)
print (a is b)
b[0] = 5
print (a)
print (b) 

#Tupla
#Criação de tuplas
tupla = (1, 2, 3, 4)
print (tupla)

tupla = (1, )
print (tupla)

tupla = ()
print (tupla) 

#Acesso a elementos da tupla
tupla = ("Maria", "João", "Carlos")
print (tupla[0])
print (tupla[0:2]) 

#Fatiamento
p = "python"
print (p[0:1])
print (p[1:2])
print (p[2:3])
print (p[3:4])
print (p[4:5])
print (p[5:6])

print (p[:1])
print (p[:2])
print (p[:3])
print (p[:4])
print (p[:5])
print (p[:6])

print (p[0:1])
print (p[0:2])
print (p[0:3])
print (p[0:4])
print (p[0:5])
print (p[0:6])

print (p[0:])
print (p[1:])
print (p[2:])
print (p[3:])
print (p[4:])
print (p[5:]) 

#Dicionários
agenda = {}
print (agenda)
agenda = {"Maria": [99887766, 99887755]}
print (agenda)
agenda = {"Maria": [99887766, 99887755], "Pedro": [92345678], "Joaquim": [99887711, 99665533]}
print (agenda)
print (agenda["Maria"]) 

agenda = {"Maria": [99887766, 99887755], "Pedro": [92345678], "Joaquim": [99887711, 99665533]}
agenda ["Pedro"] = [87654433]
print (agenda) 

agenda = {}
print (agenda)
agenda ["Tereza"] = [65443322]
print (agenda)
print (agenda["Tereza"])

musica = ["Pink Floyd", "Metallca", "Led Zeppelin", "Iron Maiden"]
musica.insert (1, "Creedence")
print (musica) '''

