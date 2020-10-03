import math
print("Anestesia")
anestesicos = ["Ketamina", "xilazina", "Halotano gasoso"]
peso = float(input("\n Insira o peso do animal em gramas: "))
dosagem = (80, 100, 200) 
posicionamentos = {"Antero-posterior (AP)": [6.42], "Latero-lateral (LL)": [3.23], "Dorso-ventral (DV)":[4.2]}
valores = {"Antero-posterior": [0.42], "Latero-lateral": [0.3], "Dorso-ventral":[0.20]}
vias = ('1 - intraoral', '2 - oral', '3 - subcutânea', '4 - intravenosa', '5 - intramuscular')

if(peso <= 300):
    print("Use Ketamina e xilazina como anestésico")
    print("Coloque", dosagem[0], "mg de anestésico\n ")

elif(peso >= 400):
    print("Use xilazina como anestésico")
    print("Coloque", dosagem[1], "mg de anestésico\n ")

else: 
    print("Use halotano como anestésico")
    print("Coloque", dosagem[2], "mg de anestésico\n ")

print("Posicione o animal no estereotáxico")

print("\n Posição dos parafusos:")

posicionamentoAP = float(input('Insira o posicionamento em centimetros da região AP ')) 
valor = float(input('Insira os valores encontrados na régua '))
localAP = posicionamentoAP-valor 

posicionamentoLL=float(input('Insira o posicionamento em centimetros da região LL')) 
valor=float(input('Insira os valores encontrados na régua'))
localLL = posicionamentoLL-valor 

posicionamentoDV=float(input('Insira o posicionamento em centimetros da região DV ')) 
valor=float(input('Insira os valores encontrados na régua '))
localDV = posicionamentoDV-valor 

print("Esses são os valores do posicionamento: \n")
print("Antero-posterior:", localAP)
print("Latero-lateral:", localLL)
print("Dorso-ventral:", localDV)

print("Perfuração")
angulacao = int(input("Insira o valor de angulação: "))
while angulacao != 45:
    print("A angulação não está adequada") 
    angulacao = int(input("Insira o valor de angulação: "))
else:
    print("A angulação está na posição adequada.")


