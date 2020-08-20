'''
lista = ['O carro','peixe',123,111]
print(lista)
#lista dentro de uma lista
nova_lista = ['pedra', lista]
print(nova_lista)

print(lista[0])
print(lista[2])
print(nova_lista[1])
print(nova_lista[1][2])

#len
print(len(nova_lista))

#operações
print(lista+nova_lista)
print(lista*3)

#busca
print('peixe' in lista)


numeros = [14.55, 67, 89.88, 10, 21.5]
print(min(numeros))
print(max(numeros))
print(sum(numeros))

#Acessar ao contrario
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
#append
livros = ['Java','SqlServer', 'Delphi','Python']
livros.append('Android')
print(livros)
#insert
livros = ['Java','SqlServer', 'Delphi','Python']
livros.insert(0,'Oracle')
print(livros)
#pop
livros = ['Java','SqlServer', 'Delphi','Python']
print(livros)
print(livros.pop())
print(livros)
livros = ['Java','SqlServer', 'Delphi','Python']
print(livros.pop(1))
print(livros)
#remove
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Oracle']
print(livros)
livros.remove('Oracle')
print(livros)
livros.remove('Oracle')
print(livros)
livros.remove('Oracle')
print(livros)
#sort
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Oracle']
livros.sort()
print(livros)
#reverse
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android']
livros.reverse()
print(livros)
#count
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android','Oracle']
print(livros.count('Oracle'))

a = [81, 82, 83]
b = a
print(a is b)
	
b[0] = 5
print(a)

b = a[:]  
print(a == b)
print(a is b)

b[0] = 5
print(a)
print(b)

lista = [66.25, 333, -1, 333, 1, 1234.5, 333]
print(lista.index(333))

tupla = (1, 2, 3, 4)
print(tupla)

tupla = (1, )
print(tupla)

tupla = ()
print(tupla)

tupla = ("Maria", "Joao", "Carlos") 
print(tupla[0])
print(tupla[0:2])


#tupla[0] = "Ana"

p = "python"
print(p[0:0])
print(p[0:1])
print(p[1:2])
print(p[2:3])
print(p[3:4]) 
print(p[4:5])
print(p[5:6])
print(p[6:6])

p = "python"
print(p[:1])
print(p[:2])
print(p[:3])
print(p[:4])
print(p[:5])
print(p[:6])

p = "python"
print(p[0:0])
print(p[0:1])
print(p[0:2])
print(p[0:3])
print(p[0:4])
print(p[0:5])
print(p[0:6])


p = "python"
print(p[:])
print(p[1:])
print(p[2:])
print(p[3:])
print(p[4:])
print(p[5:])
print(p[6:])

agenda = {}
print(agenda)

agenda = {"Maria": [99887766, 99887755]}
print(agenda)

agenda = {"Maria": [99887766, 99887755], "Pedro": [92345678], "Joaquim": [99887711, 99665533]}
print(agenda)

print(agenda["Maria"])

agenda["Pedro"] = [87654433]
print(agenda)
'''
#Implementar switch usando dicionario

switch = {"a": [99887766, 99887755], "b": [92345678], "c": [99887711, 99665533]}

print(switch["a"])
print(switch["b"])
print(switch["c"])

