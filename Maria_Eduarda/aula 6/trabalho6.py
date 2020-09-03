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
antibioticos=("buprenorfina","aspirina","indometicina","diclofenaco","paracetamol")

##Etapa Anestesia e informado na tela para o usuário a cada passo (b)
print("\n*****Etapa Anestesia****")
print("# Nesta etapa serão informadas a quantidade e a substância adequada para a anestesia do animal escolhido")
#Entradas (a)
animal=int(input("Informe o animal que será submetido a cirugia, para rato aperte 1 e para camundongo 0: "))
Peso=float(input("Informe o peso do animal em gramas: "))
#If,else (c)
if(animal):
    print("Medicamento Pré-Anestésico",anestesicos[0],"\nDosagem:100X10^(-6)l")
    gramatura=round(Peso/100,2)
    cetamina=round(0.075*gramatura,4)
    xilazina=round(0.05*gramatura,4)
    agua=round(0.075*gramatura,4)
    total=round(cetamina+xilazina+agua,4)
    print("Mistura:","Cetamina:",cetamina,"mL\nXilazina: ",xilazina,"mL\nágua para injeção ",agua,"mL\nDose",total,"mL")
    reflexo=int(input("Depois de passados 30min o animal ainda tem reflexos, 1 para sim e 0 para não: "))
    if(reflexo):
        total=round(total*0.1,4)
        print("Injetar mais",total,"da substância anestesica")
else:
    print("Medicamento Pré-Anestésico",anestesicos[1],"\nDosagem:0,5mg/kg")
    print("Medicamento Pré-Anestésico",anestesicos[2],"\nDosagem:0,04mg/kg")
    print("Medicamento Pré-Anestésico",anestesicos[3],"\nDosagem:2a 40mg/kg")
    gramatura=round(Peso/10,2)
    cetamina=round(0.01*gramatura,4)
    xilazina=round(0.005*gramatura,4)
    agua=round(0.085*gramatura,4)
    total=round(cetamina+xilazina+agua,4)
    print("Mistura:","Cetamina:",cetamina,"mL\nXilazina: ",xilazina,"mL\nágua para injeção ",agua,"mL\nDose",total,"mL")
    reflexo=int(input("Depois de passados 30min o animal ainda tem reflexos, 1 para sim e 0 para não: "))
    if(reflexo):
        total=round(total*0.1,4)
        print("Injetar mais",total,"da substância anestesica")

##Operátório-Posição da agulha
print("\n****Etapa do posicionamento da agulha****")
print("# Nesta etapa agulha será movida até o ponto desejado, ajustado o ângulo e por fim a inserção da cânula guia")
APAgulha=0
LLAgulha=0
DVagulha=0
AP=float(input("Informe a coordenada AnteroPosterior: "))
LL=float(input("Informe a coordenada LateroLateral: "))
DV=float(input("Informe a coordenada DorsoVentral: "))
estruturaAP=float(input("Informe o tamanho da estrutura desejada na visão AnteroPosterior:"))
estruturaLL=float(input("Informe o tamanho da estrutura desejada na visão LateroLateral:"))
estruturaDV=float(input("Informe o tamanho da estrutura desejada na visão DorsoVentral:"))
x=round(AP-estruturaAP,2)
y=round(DV+estruturaDV,2)
z=round(LL+estruturaLL,2)
condição=int(input("Iniciar o posicionamento, 1 para sim e 0 para não: "))
while(condição):
     if(APAgulha<x):
         APAgulha=round(APAgulha+0.1,2)
         print("Em ajuste,posição (AP): ", APAgulha)
     if( LLAgulha<z):
         LLAgulha=round(LLAgulha+0.1,2)
         print("Em ajuste,posição (LL): ",LLAgulha)
     if(APAgulha==x and LLAgulha==z):
         print("Agulha no ponto correto!!")
         print("\n***Ajustando a angulação***")
         for i in range(0,46,15):
             if(i==45):
                 print("Angulação ajustada")
                 print("***Iniciar a introdução da cânula-guia***")
                 contador=0.0
                 while(contador<y):
                     contador=contador+0.1
                     if(contador==z):
                         print("#Cânula-guia devidamente introduzida")
                         print("Dê continuidade aos procedimentos cirugícos respeitando o código de higiene")
                     
         break

##Pós-operátório
print("\n*****Etapa Pós-Operatório****")
print("# Nesta etapa serão informadas os medicamentos de pós operatório")
eutanasia=int(input("Foi realizado eutanásia? 1 para sim e 0 para não:"))
Antiinflamatorio=("aspirina ","indometacina","diclofenaco","paracetamol")
contador=0
if(not eutanasia):
     posoperatorio=int(input("Será necessário medicamento de pós operatório? 1 para sim e 0 para não:"))
     while(posoperatorio):
         if (animal):
             buprenorfina=round(0.05*(Peso*0.001),4)
             aspirina=round(100*(Peso*0.001),4)
             indometicina=round(2*(Peso*0.001),4)
             diclofenaco=round(10*(Peso*0.001),4)
             paracetamol=round(200*(Peso*0.001),4)
             for hora in range(0,48,4):
                 contador=contador+1
             print("O rato precisará de  buprenorfina dosagem de (mg):",buprenorfina,"a cada 4 horas, ou seja,",contador,"aplicações")
             print("#Anti-inflamatório e antibióticos")
             print(" ",antibioticos[1],":",aspirina,"mg\n"+antibioticos[2],":",indometicina,"mg\n",antibioticos[3],":",diclofenaco,"mg ou ",antibioticos[4],":",paracetamol)
             posoperatorio=int(input("\nAinda é necessário medicação de pós-operátório?1 para sim e 0 para não"))
         elif(not animal):
             buprenorfina=round(0.01*(Peso*0.001),4)
             aspirina=round(120*(Peso*0.001),4)
             indometicina=round(1*(Peso*0.001),4)
             diclofenaco=round(8*(Peso*0.001),4)
             paracetamol=round(200*(Peso*0.001),4)
             for hora in range(0,48,4):
                 contador=contador+1
             print("O camundongo precisará de  buprenorfina dosagem de (mg):",buprenorfina,"a cada 4 horas, ou seja,",contador,"aplicações")
             print("#Anti-inflamatório e antibióticos")
             print(" ",antibioticos[1],":",aspirina,"mg\n",antibioticos[2],":",indometicina,"mg\n",antibioticos[3],":",diclofenaco,"mg ou ",antibioticos[4],":",paracetamol)
             posoperatorio=int(input("\nAinda é necessário medicação de pós-operátório?1 para sim e 0 para não"))
