print("*****Guia para procedimento de cirurgia esterotáxica*****")
regiaoAgulha= ("AnteroPosterior","LateroLateral","DorsoVentral")
#Inicializaçao das regiões
posicionamentoinicial= [6.42, 3.23, 4.2]
print("Posicionamento Inicial", posicionamentoinicial)
#Calculo do Posicionamento
AP= posicionamentoinicial[0] - 0.42
DV= posicionamentoinicial[2] - 0.2
hemis= int(input("Qual dos hemisférios vai ser colocada a primeira cânula?(1 para direito, 2 para esquerdo)"))

if(hemis==1):
    LL= posicionamentoinicial[1] + 0.30
else:
    LL= posicionamentoinicial[1] - 0.30

posicionamentocalculado= {"AP": AP, "LL": LL, "DV": DV}
print("Regiões de posicionamento da agulha:", regiaoAgulha  )
print("Posicionamento calculado da agulha:", posicionamentocalculado)
print("Posicionando...")
print("Agulha posicionada!")

Distanciadaaguhaparameninge=5

for i in range(Distanciadaaguhaparameninge):
    ang=45
    print("Descer broca em ângulo de ", ang, "°")
    

print("Perfuração alcançou a meninge. Introduzir cânula-guia.")

for i in range(int(DV)):
    print("Introduzindo cânula-guia")

fluido= int(input("Está saindo algum fluido (licuor ou sangue) pelo orifício do crânio?"))
if(fluido==1):
    print("Instruções: Drenar o líquido utilizando pequenos rolos de papel absorvente.")
    print("Faça uma mistura de acrílico polimerizante com o solvente.")
else:
    print("Prossiga. Faça uma mistura de acrílico polimerizante com o solvente")

textura=0

while(textura==0):
    textura= int(input("A textura da mistura está espessa e maleável?"))
    if(textura==0):
        print("Continue misturando")
print("Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso e deixe secar.")

#####SEGUNDA CANULA
print("Introduza a segunda cânula guia ")

if(hemis==1):
    LL_oposto= posicionamentoinicial[1] - 0.30
else:
    LL_oposto= posicionamentoinicial[1] + 0.30
posicionamentooposto= {"AP": AP,"LL": LL_oposto,"DV": DV}

print("Levantar braço do estereotáxico")
print("Posicionamento da segunda agulha:", posicionamentooposto)
  
for j in range(int(DV)):
    print("Introduzindo a segunda cânula-guia")

fluido2= int(input("Está saindo algum fluido (licuor ou sangue) pelo orifício do crânio?"))
if(fluido2==1):
    print("Instruções: Drenar o líquido utilizando pequenos rolos de papel absorvente.")
    print("Faça uma mistura de acrílico polimerizante com o solvente.")
else:
    print("Prossiga. Faça uma mistura de acrílico polimerizante com o solvente")

textura2=0

while(textura2==0):
    textura2= int(input("A textura da mistura está espessa e maleável?"))
    if(textura2==0):
        print("Continue misturando")
print("Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso e deixe secar.")

print("*********Fim da cirurgia. Pode acomodar o animal em uma caixa aquecida por uma lâmpada.**********")
acordou=int(input("Animal acordou?"))
if(acordou==0):
    while(acordou==0):
        if(acordou==1):
            print("Colocar o animal de volta a sua caixa-moradia")
            break
        acordou=int(input("Animal acordou?"))
else:
  print("Colocar o animal de volta a sua caixa-moradia")  