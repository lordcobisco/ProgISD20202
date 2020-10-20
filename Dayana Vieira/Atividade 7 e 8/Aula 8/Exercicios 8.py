arquivo = open("workfile", "w")

arquivo.write("Hello Word\n")
arquivo.write("This is our new text file\n")
arquivo.write("and this is another line.\n")
arquivo.write("Why? Because we can.\n")


arquivo.close()

arquivo = open("workfile", "r")
print(arquivo.read())

arquivo = open("workfile", "r")
print(arquivo.readline())
print(arquivo.readline())

arquivo = open ("workfile", "r")
print(arquivo.readline(3))

arquivo = open ("workfile", "r")
print(arquivo.readline())

arquivo = open("worfile", "r")
for linha in arquivo:
    print(linha)

