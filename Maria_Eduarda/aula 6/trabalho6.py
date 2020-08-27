import math

##Dicionário (E)
print("****Bem vindo ao cirurgia estereotáxica para ratos e camundongo")

print("Para mais informações sobre SUBSTÂNCIAS ANESTÉSICAS para cirugia estereotáxica em animais clique no número equivalente")
print("1-ACEPROMAZINA\n2-ATROPINA\n3-CLORPROMAZINA\n4-DIAZEPAN\n5-FENTANIL,6-FENTANIL- DROPERIDOL")
print("7-HALOTANO\n8-LEVOMEPROMAZINA\n9-MEPERIDINA\n10-METOXIFLURANO\n11-MIDAZOLAN")
print("12-PENTOBARBITAL\n13-QUETAMINA\n14-TILETAMINA- ZOLAZEPAN\n15-TIOPENTAL\n16-XILAZINA")
x=input("Informe o número da substância anestésica: ")
anestesias={"1":["ACEPROMAZINA", "ACEPRAM 0,2%", "UNIVET" ,"2,0 mg/ml"],"2":["ATROPINA", "SULFATO DE ATROPINA",
"APSET", "0,25mg/ml"],"3":["CLORPROMAZINA", "AMPLICTIL", "RHODIA","25mg/5ml"],"4":["DIAZEPAN","VALIUM", "ROCHE","5mg/ml"],
"5":["FENTANIL", "FENTANIL", "JHONSON&JHONSON", "0,05mg/ml"],"6":["FENTANIL- DROPERIDOL","INOVAL","JHONSON&JHONSON ","------"],
"7":["HALOTANO", "HALOTANO", "HOESCHT", "Frasco de 50,100 e 250ml"],"8":["LEVOMEPROMAZINA", "NEOZINE", "RHODIA", "25mg/5ml"],
"9":["MEPERIDINA", "DOLANTINO", "HOESCHT","50mg/ml"],"10":["METOXIFLURANO", "PENTRANE","ABBOTT","Frasco 100ml"],
"11":["MIDAZOLAN", "DORMONID", "ROCHE", "15 mg/3ml"],"12":["PENTOBARBITAL", "HYPRIOL", "CRISTÁLIA", "30 mg/ml"],
"13":["QUETAMINA", "KETALAR", "PACKE-DAVIS", "50 mg/ml"],"14":["TILETAMINA- ZOLAZEPAN","ZOLETIL", "VIRBAC","50 mg/ml"],
"15":["TIOPENTAL", "THIONEMBUTAL", "ABBOTT", "0,5 e 1g"],"16":["XILAZINA","ROMPUM","BAYER","20 mg/ml"]}
print("Substância:",anestesias[x][0],"\nPrincipio ativo:",anestesias[x][1],"\nLaboratório:",anestesias[x][2],"\nApresentação:",anestesias[x][3])

anestesicos=["Acepran 0.2%","Diazepam","Atropina","Cloripromazina"]#Lista(e)
##Etapa Anestesia e informado na tela para o usuário a cada passo (b)
print("*****Etapa Anestesia****")
print("# Nesta etapa serão informadas a quantidade e a substância adequada para a anestesia do animal escolhido")
#Entradas (a)
animal=int(input("Informe o animal que será submetido a cirugia, para rato aperte 1 e para camundongo 2"))
Peso=float(input("Informe o peso do animal em gramas"))
#If,else (c)
if(animal==1):
    print("Medicamento Pré-Anestésico",anestesicos[0],"\nDosagem:100X10^(-6)l")
    gramatura=int(Peso/100)
    cetamina=0.075*gramatura
    xilazina=0.05*gramatura
    agua=0.075*gramatura
    total=cetamina+xilazina+agua
    print("Mistura:","Cetamina:",cetamina,"mL\nXilazina: ",xilazina,"mL\nágua para injeção ",agua,"\nDose",total,"mL")
    reflexo=int(input("Depois de passados 30min o animal ainda tem reflexos, 1 para sim e 2 para não"))
    if(reflexo==1):
        total=total*0.1
        print("Injetar mais",total,"da substância anestesica")
else:
    print("Medicamento Pré-Anestésico",anestesicos[1],"\nDosagem:0,5mg/kg")
    print("Medicamento Pré-Anestésico",anestesicos[2],"\nDosagem:0,04mg/kg")
    print("Medicamento Pré-Anestésico",anestesicos[3],"\nDosagem:2a 40mg/kg")
    gramatura=int(Peso/10)
    cetamina=0.01*gramatura
    xilazina=0.005*gramatura
    agua=0.085*gramatura
    total=cetamina+xilazina+agua
    print("Mistura:","Cetamina:",cetamina,"mL\nXilazina: ",xilazina,"mL\nágua para injeção ",agua,"\nDose",total,"mL")
    reflexo=int(input("Depois de passados 30min o animal ainda tem reflexos, 1 para sim e 2 para não"))
    if(reflexo==1):
        total=total*0.1
        print("Injetar mais",total,"da substância anestesica")


"""ACEPROMAZINA ACEPRAM 0,2% UNIVET 2,0 mg/ml
ATROPINA SULFATO DE
ATROPINA
APSET 0,25mg/ml
CLORPROMAZINA AMPLICTIL RHODIA 25mg/5ml
DIAZEPAN VALIUM ROCHE 5mg/ml
FENTANIL FENTANIL JHONSON&JHONSON 0,05mg/ml
FENTANIL- DROPERIDOL
INOVAL JHONSON&JHONSON ----------------- HALOTANO HALOTANO HOESCHT Frasco de 50,100 e
250ml
LEVOMEPROMAZINA NEOZINE RHODIA 25mg/5ml
MEPERIDINA DOLANTINO HOESCHT 50mg/ml
METOXIFLURANO PENTRANE ABBOTT Frasco 100ml
MIDAZOLAN DORMONID ROCHE 15 mg/3ml
PENTOBARBITAL HYPRIOL CRISTÁLIA 30 mg/ml
QUETAMINA KETALAR PACKE-DAVIS 50 mg/ml
TILETAMINA- ZOLAZEPAN
ZOLETIL VIRBAC 50 mg/ml
TIOPENTAL THIONEMBUTAL ABBOTT 0,5 e 1g
XILAZINA ROMPUM BAYER 20 mg/ml"""