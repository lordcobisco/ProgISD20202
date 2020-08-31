import math
#Declarando variaveis
LarguraBanda= 30
ComprimentoOnda=2
DiametroPinhole=50
TamnhoMonitor= 30
Obturador= 10
Zoom=10
Filtro="sem filtro"
TipoEscaner="galvanômetro"
ModoEscaneamento="XT"
ResolucaoImagem="64x64"

#Informe Inicial
print("************Esse programa tem como objetivo receber dados para a configuração de microscopio confocal de varredura à laser*********** \n")
#Comparacao de variaveis padrao e setadas pelo usuario
LarguraBanda2= input("Informe a largura de banda do comprimento de onda em nm: ")
print("“Houve alteração na variável inserida?", str(LarguraBanda)!= LarguraBanda2)
ComprimentoOnda2= input("Informe a resolução do comprimento de onda em nm: ")
print("“Houve alteração na variável inserida?", str(ComprimentoOnda)!= ComprimentoOnda2)
DiametroPinhole2= input("Informe o diametro do pinhole em micrometros: ")
print("“Houve alteração na variável inserida?", str(DiametroPinhole) != DiametroPinhole2)
TamnhoMonitor2= input("Informe o tamanho do monitor: ")
print("“Houve alteração na variável inserida?", str(TamnhoMonitor) != TamnhoMonitor2)
Obturador2= input("Informe a energia máxima do laser: ")
print("“Houve alteração na variável inserida?", str(Obturador) != Obturador2)
Zoom2= input("Informe o zoom óptico: ")
print("“Houve alteração na variável inserida?", str(Zoom)!= Zoom2)
Filtro2= input("Informe o filtro utilizado ")
print("“Houve alteração na variável inserida?",  Filtro2 != "Sem filtro" and Filtro2!= "SEM FILTRO" and Filtro2 != Filtro)
TipoEscaner2= input("Informe o tipo de escaner utilizado: ")
print("“Houve alteração na variável inserida?", TipoEscaner != TipoEscaner2 and TipoEscaner2 != "Galvanômetro" and TipoEscaner2 != "GALVANÔMETRO")
ModoEscaneamento2= input("Informe o modo de escaneamento: ")
print("“Houve alteração na variável inserida?", ModoEscaneamento != ModoEscaneamento2 and ModoEscaneamento2 != "xt")
ResolucaoImagem2=input("Informe a resolução da imagem: ")
print("“Houve alteração na variável inserida?",ResolucaoImagem != ResolucaoImagem2 and ResolucaoImagem2 != "64 x 64" and ResolucaoImagem2 != "64 X 64" and ResolucaoImagem2 != "64X64")

#Mostrar informações setadas
print("\n As informações de configurações setadas pelo usuário são:")
print("Largura de banda do comprimento de onda : ",LarguraBanda2)
print("O comprimento de onda: ", ComprimentoOnda2)
print("Diametro do Pinhole:", DiametroPinhole2)
print("Tamanho do monitor:",TamnhoMonitor2)
print("Energia máxima do laser:",Obturador2)
print("Resolução da imagem:",ResolucaoImagem2)
print("Zoom óptico:",Zoom2)
print("Filtro:",Filtro2)
print("Tipo do escaner:",TipoEscaner2)
print("Modo de escaneamento: ", ModoEscaneamento2)

#Ajuste na horizontal 
#1
print("\nPara a calibração na horizontal seja efetuada você precisará informar a primeira e a ultima letra do seu nome.Vale deixar claro, que esse procedimento ocorrerá 10 vezes")
print("Primeira Interação:")
primeira=input("Primeira:")
ultima=input("Ultima:")
print("O caracter digitado foi:", primeira)
print("O caracter digitado foi:", ultima)
#2
print("Segunda Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#3
print("Terceira Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#4
print("Quarta Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#5
print("Quinta Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide: " + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#6
print("Sexta Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#7
print("Setima Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide: " + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#8
print("Oitava Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide: " + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#9
print("Nona Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ultima==u) + ".  O caracter digitado foi:" + str(u))
#10
print("Decima Interação:")
p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(primeira==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide:" + str(ultima==u) + ".  O caracter digitado foi:" + str(u))

#Ajuste na Vertical
#1
print("\nPara a calibração na vertical seja efetuada você precisará informar a segunda e a penultima letra do seu nome.Vale deixar claro, que esse procedimento ocorrerá 10 vezes")
print("Primeira Interação:")
Segunda=input("Segunda:")
Penultima=input("Penultima:")
print("O caracter digitado foi:", primeira)
print("O caracter digitado foi:", ultima)
#2
print("Segunda Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#3
print("Terceira Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#4
print("Quarta Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#5
print("Quinta Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#6
print("Sexta Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#7
print("Setima Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#8
print("Oitava Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#9
print("Nona Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))
#10
print("Decima Interação:")
s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Segunda==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Penultima==pe) + ".  O caracter digitado foi:" + str(pe))

print("\n ***********A calibração do sistema foi finalizada com sucesso**************************")
