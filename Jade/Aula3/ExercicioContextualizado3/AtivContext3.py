import math
#Declaração variaveis
Contraste= 30
Iluminacao=2
ProfundidadeCampo=50
QuantidadeLentes=4
Obturador= 10
Ampliacao= 400
Marcador="sem marcador"
TipoEscaner="galvanômetro"
ModoEscaneamento="XT"
ResolucaoImagem="64x64"

#Inicio
print("Esse programa tem como objetivo receber dados para a configuração de microscopio confocal de varredura \n")

#Comparacao entre as variaveis padrao e as setadas pelo usuario
Contraste_novo= input("Informe o contraste: ")
print("“Houve alteração na variável inserida?", str(Contraste)!= Contraste_novo)
Iluminacao_novo= input("Informe a iluminção: ")
print("“Houve alteração na variável inserida?", str(Iluminacao)!= Iluminacao_novo)
ProfundidadeCampo_novo= input("Informe a Profundidade de Campo: ")
print("“Houve alteração na variável inserida?", str(ProfundidadeCampo) != ProfundidadeCampo_novo)
QuantidadeLentes_novo= input("Informe a Quantidade de Lentes: ")
print("“Houve alteração na variável inserida?", str(QuantidadeLentes) != QuantidadeLentes_novo)
Obturador_novo= input("Informe o obturador: ")
print("“Houve alteração na variável inserida?", str(Obturador) != Obturador_novo)
Ampliacao_novo= input("Ampliação: ")
print("“Houve alteração na variável inserida?", str(Ampliacao)!= Ampliacao_novo)
Marcador_novo= input("Informe o marcador utilizado ")
print("“Houve alteração na variável inserida?", str(Marcador)!= Marcador_novo)
TipoEscaner_novo= input("Informe o tipo de escaner utilizado: ")
print("“Houve alteração na variável inserida?", str(TipoEscaner)!= TipoEscaner_novo)
ModoEscaneamento_novo= input("Informe o modo de escaneamento: ")
print("“Houve alteração na variável inserida?", str(ModoEscaneamento)!= ModoEscaneamento_novo)
ResolucaoImagem_novo=input("Informe a resolução da imagem: ")
print("“Houve alteração na variável inserida?",str(ResolucaoImagem)!= ResolucaoImagem_novo)

#Mostrar informações setadas
print("\n As informações de configurações setadas pelo usuário são:")
print("Constraste: ", Contraste_novo)
print("Iluminação: ", Iluminacao_novo)
print("Profundidade de Campo:", ProfundidadeCampo_novo)
print("Quantidade de Lentes:",QuantidadeLentes_novo)
print("Obturador:",Obturador_novo)
print("Ampliação:",Ampliacao_novo)
print("Marcador:",Marcador_novo)
print("Tipo do escaner:",TipoEscaner_novo)
print("Modo de escaneamento: ", ModoEscaneamento_novo)
print("Resolução da imagem:", ResolucaoImagem_novo)

#Ajuste na horizontal 
prim=input("Qual a primeira letra do seu nome?")
ult=input("Qual a ultima letra do seu nome?")
print("\n Para realizar a calibração na horizontal, insira 10 x a primeira e ultima letra do seu nome ")


primeira=input("Primeira letra do seu nome:")
ultima=input("Ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide: " + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide: " + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide: " + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide: " + str(ult==u) + ".  O caracter digitado foi:" + str(u))

p=input("primeira letra do seu nome:")
u=input("ultima letra do seu nome:")
print("A primeira letra coincide:" + str(prim==p )+ ". O caracter digitado foi:" + str(p))
print("A ultima letra coincide:" + str(ult==u) + ".  O caracter digitado foi:" + str(u))

#Ajuste na Vertical
Seg=input("Qual a segunda letra do seu nome?")
Pen=input("Qual a Penultima letra do seu nome?")
print("\n Para realizar a calibração na vertical, insira 10 x a Segunda e penultima letra do seu nome ")


s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

s=input("Segunda letra do seu nome:")
pe=input("penultima letra do seu nome:")
print("A Segunda letra coincide:" + str(Seg==s )+ ". O caracter digitado foi:" + str(s))
print("A Penultima letra coincide:" + str(Pen==pe) + ".  O caracter digitado foi:" + str(pe))

print("\n A calibração do sistema foi finalizada com sucesso")
