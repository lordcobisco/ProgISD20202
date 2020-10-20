'''
fileObject = open('aula8.txt', 'w') #criando um arquivo .txt

print(fileObject)

fileObject.write("Este é o meu primeiro txt \\n \n")
fileObject.write("Usando a função .write é possível escrever coisas dentro do arquivo \n")

fileObject.close()

fileObject = open('aula8.txt', 'r')
print(fileObject.read())
'''
#Para ler o arquivo caracter a caracter
'''
fileObject = open('aula8.txt', 'r')
print(fileObject.read(10))#ler os 10 primeiros caracteres

fileObject.close() 
'''
#Para ler um arquivo em outras pasta
'''
fileObject = open('D:\\bochapp\\Assets\\Scripts\\localizacao.cs', 'r')
print(fileObject.read(10)) #ler os 10 primeiros caracteres de um arquivo fora da pasta
fileObject.close() 
'''

#Para ler uma quantidade x de caracteres e separar em linhas
'''
fileObject = open('aula8.txt', 'r')
print(fileObject.readline(10))
print(fileObject.readline(10))
print(fileObject.readline(10))
print(fileObject.readline(10))
print(fileObject.readline(10))
fileObject.close() 

'''
#Para ler as linhas, o parâmetro interno diz qual linha será lida. Tudo é adicionado em listas
'''
fileObject = open('aula8.txt', 'r')
print(fileObject.readlines(1))
fileObject.close() 
'''
#Para pegar várias linhas do arquivos
'''
fileObject = open('aula8.txt', 'r')
for line in fileObject:
    print(line)
fileObject.close() 
'''
#Para escrever/sobrescrever informações
'''
fileObject = open('aula8.txt', 'w')
Linhas = ['Substituir','ad','asas ']
fileObject.writelines(Linhas)
fileObject.close()
'''
#para abrir o arquivo usando with
with open('aula8.txt','r') as fileObject: #Não precisa ficar abrindo e fechando, ele ja faz isso
    for line in fileObject:
        print(line)

