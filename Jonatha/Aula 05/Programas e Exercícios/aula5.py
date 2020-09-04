# Os seguintes códigos foram executados pelo professor na aula 05
# Operações com LISTAS
# Cria e exibe uma lista
lista = []
print(lista)

# Cria uma lista com dados heterogêneos e printa
lista = ['O carro', 'peixe', 123, 111]
print(lista)

# Cria uma lista heterogênia e armazena essa lista no segundo campo de outra lista
lista = ['O carro', 'peixe', 123, 111]
nova_lista = ['pedra', lista]
print(nova_lista)

# Cria duas lista e realiza o acesso a elas
lista = ['O carro', 'peixe', 123, 111]
nova_lista = ['pedra', lista]
print(lista[0])
print(lista[2])
print(nova_lista[1])
print(nova_lista[1][2])

# Cria uma lista heterogênea, armazena dentro de outra lista e exibe o tamanho da segunda lista após o armazenamento
lista = ['O carro', 'peixe', 123, 111]
nova_lista = ['pedra', lista]
print(len(nova_lista))

# Cria duas listas, e printa elas concatenadas
lista = ['O carro', 'peixe', 123, 111]
nova_lista = ['pedra', lista]
print(lista+nova_lista)
print(lista*3)

# Exibe a utilização do comando in. Assim é possível saber se tem 'peixe' na lista
lista = ['O carro', 'peixe', 123, 111]
print('peixe' in lista)

# Aplica operadores matemáticos a uma lista criada
numeros = [14.55, 67, 89.88, 10, 21.5]
print(min(numeros))
print(max(numeros))
print(sum(numeros))

# Exibe o acesso a uma lista utilizando indices negativos. Assim é possível pegar elementos finais da lista
lista = ['O carro', 'peixe', 123, 111]
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# Mostra a utilziação do comando append que armazena um item ao final de uma lista.
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.append('Android')
print(livros)

# Mostra a utilizaçao do comando insert, que armazena um itens em uma posição específica dentro de uma lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.insert(0, 'Oracle')
print(livros)

# Exibe a utilização do comando pop que retira um elemento de uma lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros)
print(livros.pop())
print(livros)
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
print(livros.pop(1))
print(livros)

livros = ['Oracle', 'Java', 'SqlServer',
    'Delphi', 'Python', 'Android', 'Oracle']
print(livros)
livros.remove('Oracle')
print(livros)
livros.remove('Oracle')
print(livros)


livros = ['Oracle', 'Java', 'SqlServer',
    'Delphi', 'Python', 'Android', 'Oracle']
livros.sort()
print(livros)

livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android']
livros.reverse()
print(livros)

livros = ['Oracle', 'Java', 'SqlServer',
    'Delphi', 'Python', 'Android', 'Oracle']
print(livros.count('Oracle'))

a = [81, 82, 83]
b = a
print(a is b)

a = [81, 82, 83]
b = [81, 82, 83]

print(a == b)
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

a = [81, 82, 83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5
print(a)
print(b)

lista = [66.25, 333, -1, 333, 1, 1234.5, 333]
print(lista.index(333))

# Operações com tuplas
tupla = (1, 2, 3, 4)
print(tupla)

tupla = (1, )
print(tupla)

tupla = ()
print(tupla)

tupla = ("Maria", "Joao", "Carlos")
print(tupla[0])
print(tupla[0:2])


# tupla[0] = "Ana"

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

# Operações com DICIONÁRIOS
agenda = {}
print(agenda)

agenda = {"Maria": [99887766, 99887755]}
print(agenda)

agenda = {"Maria": [99887766, 99887755], "Pedro": [
    92345678], "Joaquim": [99887711, 99665533]}
print(agenda)

print(agenda["Maria"])

agenda["Pedro"] = [87654433]
print(agenda)

agenda = {}
print(agenda)
agenda["Teresa"] = [65443322]
print(agenda)
'''

lista = [1, 2, 3, 4, 5]
print(lista.remove(2))
print(lista)
