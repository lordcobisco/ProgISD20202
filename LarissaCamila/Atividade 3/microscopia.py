#Variáveis

objetiva = 40 #x#
fluoróforo = "DAPI"
laser = 458 #nm#
pinhole = "1AU" #Abertura#
lentes = 4 #Quantidade#
gain = 568
resolução = "1024 x 1024"
bit_depth = 12 #bit#
TLilumination = "ON" #Ligar luz branca#
RLilumination = "ON" #Ligar fluorescência#

#Início
print("Esse programa tem como objetivo receber dados para configurar o microscópio confocal")

#Comunicação com usuário

objetiva2 = int(input("Digite a objetiva a ser utilizada: "))
print("Houve alteração na variável inserida?",objetiva!=objetiva2)

fluoróforo2 = input("Digite o fluoróforo a ser utilizado: ")
print("Houve alteração na variável inserida?",fluoróforo!=fluoróforo2)

laser2 = int(input("Digite o laser a ser utilizado: "))
print("Houve alteração na variável inserida?",laser!=laser2)

pinhole2 = input("Digite o pinhole a ser utilizado: ")
print("Houve alteração na variável inserida?",pinhole!=pinhole2)

lentes2 = int(input("Digite as lentes a serem utilizadas: "))
print("Houve alteração na variável inserida?",lentes!=lentes2)

gain2 = int(input("Digite o gain a ser utilizado: "))
print("Houve alteração na variável inserida?",gain!=gain2)

resolução2 = input("Digite a resolução a ser utilizada: ")
print("Houve alteração na variável inserida?",resolução!=resolução2)

bit_depth2 = int(input("Digite o Bit Depth a ser utilizado: "))
print("Houve alteração na variável inserida?",bit_depth!=bit_depth2)

TLilumination2 = input("Digite o TLilumination a ser utilizado: ")
print("Houve alteração na variável inserida?",TLilumination!=TLilumination2)

RLilumination2 = input("Digite o RLilumination a ser utilizado: ")
print("Houve alteração na variável inserida?",RLilumination!=RLilumination2)

#Mostrar informações#
print("As informações setadas foram: ")

print("objetiva: ", objetiva2)
print("fluoróforo: ", fluoróforo2)
print("laser: ", laser2)
print("pinhole: ", pinhole2)
print("lentes: ", lentes2)
print("gain: ", gain2)
print("resolução: ", resolução2)
print("bit_depth: ", bit_depth2)
print("TLilumination: ", TLilumination2)
print("RLilumination: ", RLilumination2)

# Calibração Horizontal#
primeira = input("Digite a primeira letra do seu nome: ")
ultima = input("Digite a última letra do seu nome: ")

print("Para prosseguirmos com a calibração (HORIZONTAL) do equipamento, preciso que você digite a primeira e última letra do seu nome 10x. \n")

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

p = input("Primeira letra: \n")
print("Ambas as letras coincidem: " + str(primeira == p) + ". Essa foi a letra digitada: " + str(p))
u = input("Última letra: \n")
print("Ambas as letras coincidem: " + str(ultima == u) + ". Essa foi a letra digitada: " + str(u))

# Calibração Vertical#
Print("Concluímos a calibração horizontal, agora vamos para a vertical.")

segunda = input("Digite a segunda letra do seu nome: ")
penultima = input("Digite a penúltima letra do seu nome: ")

print("Para prosseguirmos com a calibração (Vertical) do equipamento, preciso que você digite a segunda e penúltima letra do seu nome 10x. \n")

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

s = input("Segunda letra: \n")
print("Ambas as letras coincidem: " + str(segunda == s) + ". Essa foi a letra digitada: " + str(s))
pe = input("Penúltima letra: \n")
print("Ambas as letras coincidem: " + str(penultima == pe) + ". Essa foi a letra digitada: " + str(pe))

print("A calibração do microscópio confocal foi realizada com sucesso.")