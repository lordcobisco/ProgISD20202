anestesico = ["Xilazina", "Ketamina", "Isoflurano"]
dosagem = ("Xilazina - 5 a 10 mg/kg","Ketamina - 50 a 90 mg/kg", "Isoflurano - 3 a 4%")
via = ["Xilazina - intraperitoneal", "Ketamina - intraperitoneal", "Isoflurano - Inalatória"]

#Anestesia

pesoanimal = float(input("Qual o peso (g) do animal utilizado? "))
print(pesoanimal)

print("Anestésicos disponíveis: ", anestesico)
anestesicousado = input("Qual anestésico será utilizado?\n")

print("Dosagens recomendadas: ", dosagem)
dosagemusada = float(input("Qual dosagem será utilizada? "))

print("Vias de administração recomendadas: ", via)
viaadministrada = input("Qual a via de administração? ")

print("O anestésico selecionado foi : ", anestesicousado)
print("A dosagem selecionada foi: ", dosagemusada)
print("A via de administração selecionada foi: ", viaadministrada)

#Posicionamento estereotáxico

print("O animal deverá ser posicionado de modo que as barras sejam posicionadas no ouvido externo")
print("Verificar posicionamento do animal no minímo 3 x")

posicionado = 0
for posicionado in range (3):
    posicionamento = int(input("O animal foi posicionado no estereotáxico corretamente? 0 (Não) - 1 (Sim): "))

if posicionamento == 0:
    print("O animal não foi posicionado corretamente.")
elif posicionamento == 1:
    print("O animal foi posicionado corretamente sem diferenças na angulação entre o bregma e o lambda.")
else: 
    print("Inválido")

#Parafuso

print("Informe os valores encontrados na régua a partir do posicionamento da agulha")
reguaAP = float(input("Digite o valor presente na régua referente ao posicionamento AnteroPosterior (AP): " ))
reguaLL = float(input("Digite o valor presente na régua referente ao posicionamento LateroLateral (LL): " ))
reguaDV = float(input("Digite o valor presente na régua referente ao posicionamento DorsoVentral (DV): " ))

print("Informe os valores referentes as áreas de cada estrutura selecionada")
estrutAP = float(input("Informe o valor AnteroPosterior: "))
estrutLL = float(input("Informe o valor LateroLateral: "))
estrutDV = float(input("Informe o valor DorsoVentral: "))

print("O valor presente na régua foi (AP): ", reguaAP)
print("O valor presente na régua foi (LL): ", reguaLL)
print("O valor presente na régua foi (DV): ", reguaDV)

print("O valor da estrutura é (AP): ", reguaAP)
print("O valor da estrutura é (LL): ", reguaLL)
print("O valor da estrutura é (DV): ", reguaDV)

#Pós cirúrgico

print("Após realização de todo o procedimento cirúrgico o animal deverá ser acomodado de forma isolada em uma caixa")
print("Verificar estado do animal no pós cirúrgico por no minímo 6 x, levando em consideração as seguintes observações: \n - Ingestão hidríca  \n - Mobilidade  \n - Alimentação  \n - Comportamento (Geral)")

poscirurgico = 0
for poscirurgico in range (6):
    poscirurgia = int(input("O animal apresenta alguma alteração que esteja comprometendo seu estado geral? 0 (Não) - 1 (Sim): "))

if posicionamento == 0:
    print("O animal segue em bom estado geral")
elif posicionamento == 1:
    print("O animal apresenta alterações que podem estar comprometendo seu estado geral.")
else: 
    print("Inválido")
