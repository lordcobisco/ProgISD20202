#### PROGRAMA PARA CIRURGIA ESTEREOTAXICA ####

#### ANESTESIA ####
import math
print("Anestesia - 1ª etapa da cirugia estereotaxica")
anestesicos = ["Ketamina", "xilazina", "Halotano gasoso"] # utilizando lista
peso=float(input("\n Insira o peso do animal em gramas: "))
dosagem = (80, 100, 200) # utilizando tupla
posicionamentos = {"Antero-posterior (AP)": [6.42], "Latero-lateral (LL)": [3.23], "Dorso-ventral (DV)":[4.2]} # valores de referencia
valores = {"Antero-posterior": [0.42], "Latero-lateral": [0.3], "Dorso-ventral":[0.20]} # utlizando dicionario
vias = ('1 - intraoral', '2 - oral', '3 - subcutânea', '4 - intravenosa', '5 - intramuscular')

if(peso <= 300): # utilizando if-elif-else
    print("Use Ketamina e xilazina como anestésico")
    print("Coloque", dosagem[0], "mg de anestésico\n ")

elif(peso >= 400):
    print("Use xilazina como anestésico")
    print("Coloque", dosagem[1], "mg de anestésico\n ")

else: 
    print("Use halotano como anestésico")
    print("Coloque", dosagem[2], "mg de anestésico\n ")

for v in vias: # utilizando for-else
    print(v)
else:
    vias=int(input('\n Digite o numero correspondente a via de administração: '))
    print("A via escolhida foi: %s" %(vias))

print("\n******Posicine o animal no estereotáxico******")

#### POSICIONAMENTO #####
print(posicionamentos, valores)
print("\n Posicionamento dos parafusos - 2ª etapa da cirurgia estereotexica")
posicionamentoAP=float(input('Insira o posicionamento em centimetros da região AP ')) 
valor=float(input('Insira os valores encontrados na régua '))
localAP = posicionamentoAP-valor 
posicionamentoLL=float(input('Insira o posicionamento em centimetros da região LL')) 
valor=float(input('Insira os valores encontrados na régua'))
localLL = posicionamentoLL-valor 
posicionamentoDV=float(input('Insira o posicionamento em centimetros da região DV ')) 
valor=float(input('Insira os valores encontrados na régua '))
localDV = posicionamentoDV-valor 
print("Esses são os valores do posicionamento: \n")
print("Antero-posterior:", localAP, "---", "Latero-lateral:", localLL, "---", "Dorso-ventral:", localDV )

#### PERFURAÇÃO #####
print(" \n Perfuração - 3ª etapa da cirurgia estereotáxica\nNesta etapa, para o procedimento ser bem sucedido, não deve haver perfuração das meninges. \nPara que isso não aconteça, a perfuração do crânio deverá ser realizada com 45º de angulação")

angulacao=int(input("Insira o valor de angulação: ")) # utilizando while
while angulacao != 45:
    print("A angulação não está adequada") 
    angulacao=int(input("Insira o valor de angulação: "))
else:
    print("A angulação está na posição adequada\nProssiga com a cirurgia")


