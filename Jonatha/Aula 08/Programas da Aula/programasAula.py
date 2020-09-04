from os import system
system('clear')
print(system('ls'))
system('cd \Documents')
print(system('ls'))
print('Escrevendo um arquivo: ')

'''
arquivo = open('arquivo.py','w')
arquivo.write("print('Hello World')")
arquivo.close()
system('python arquivo.py')

arquivo = open('arquivo.py','r')
arquivo.close()


# Armazenando linhas, e lendo linhas
arquivo = open('aula.txt','w')
linhas = ['\nprimeira linha', 'segunda linha', '\nterceira linha']
arquivo.writelines(linhas)
arquivo.close()

# Lendo linhas de um arquivo
arquivo = open('aula.txt', 'r')
for linha in arquivo:
  print(linha)
arquivo.close()

# Usando with para abrir um arquivo
with open('aula.txt','r') as arquivo:
  for linha in arquivo:
    print(linha)

# Usando with para abrir um arquivo
with open('aula.txt', 'r') as arquivo:
  texto = arquivo.readlines()

print(type(texto))
'''
