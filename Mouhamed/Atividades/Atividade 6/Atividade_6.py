import math


print('Cirurgia esterotáxica em animais')

antiflamatorios_ratos = (("Aspirina", "100mg/kg"), ("Indometacina" , "2mg/kg"), ("Diclofenaco" , "10mg/kg"))
antiflamatorios_camundongo = (("Aspirina", "120mg/kg"), ("Indometacina" , "1mg/kg"), ("Diclofenaco" , "8mg/kg"))

animal = int(input("Qual o animal? Digite 0 para rato e 1 para camundongo "))
lista = ['rato', 'camundongo']
if animal == 0:
    print ( "O animal é: ", lista[0])
    print("Antiflamatórios recomendados: ", antiflamatorios_ratos)
elif animal == 1:
    print ( "O animal é: ", lista[1])
    print("Antiflamatórios recomendados: ", antiflamatorios_camundongo)

#Retirado da bibliografia - Fazendo um dicionário
referencia_anestesias = { "Ketamina", "90 a 120mg/kg", "Xilazina" , "5 a 16mg/kg"  }
nome = input("Para informações sobre a dosagem de anestesticos de acordo com o peso, digite 'Ketamina' ou 'Xilazina': ")

antiflamatorios_ratos = (("Aspirina", "120mg/kg"), ("Indometacina" , "1mg/kg"), ("Diclofenaco" , "8mg/kg"))

if nome == "Ketamina":
    referencia_anestesias = { "Ketamina" : "90 a 120 mg/kg" }
    print(referencia_anestesias)
else:
    referencia_anestesias = { "Xilazina" : "5 a 16 mg/kg" }
    print(referencia_anestesias)

peso_animal = float(input('Qual o peso do animal?'))

dose_ketamina = peso_animal*90 #Mg
dose_xilazina = peso_animal*10 #Mg

print(" A dosagem de ketamina deve ser: ", dose_ketamina)
print(" A dosagem de xilazina deve ser: ", dose_xilazina)

anestesiado = input('O animal está anestesiado? Digite S ou N ' )

if anestesiado == "S":
    print("Posicionar o animal no estereotáxico")
    ang_bregma = input("Digite o valor da angulação bregma: ")
    ang_lambda = input("Digite o valor da angulação lambda:  ")

    while ang_bregma != ang_lambda:
        print("A posição não esta correta. As angulações de bregma e lambda devem ser iguais")
        ang_bregma = input("Digite o valor da angulação bregma ")
        ang_lambda = input("Digite o valor da angulação lambda ")

    print("O animal está posicionado! Superfície de cirurgia plana")

    #Limpeza do campo de trabalho
    print("1 - Retire a pelagem que recobre a parte superior da calota craniana")
    print ("2 - Retire os tecidos moles: epiderme, derme e tecido conjuntivo")
    resposta1 = input("Alcançou a parte óssea da caixa craniana: (Responda S ou N) ")

    while resposta1 != "S":
        print("Continue retirando os tecidos moles")
        resposta1 = input("Alcançou a parte óssea da caixa craniana: (Responda S ou N) ")

    print("3 - Retire o resto de pele utilizando H2O2 10 volumes")
    print("Pronto! O campo de trabalho está limpo!")

    #IV
    print("Aplique uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos") 

    #V
    fixacao_parafusos = int(input("Escolha o ponto de fixação do parafuso. Recomenda-se escolher na parte posterior da calota craniana "))
    voltas = 1
    for i in range (1, 4): 
        print("Você deu :" , i, "volta(s) no parafuso")

    agulha_antero =0
    agulha_latero = 0
    agulha_dorso = 0

    antero_posterior=6
    latero_lateral=3.63
    dorso_ventral=4

    print("Ajustes definidos")

    #Furos para alcançar a meninge
    print(" Faça os furos para alcançar as meninges. Para isso, apoie a mão que segura a broca contra o assoalho em 45º")
    introducao_canula1 = 0

    while (introducao_canula1 != dorso_ventral):
        introducao_canula1 += 1
        print("Aguarde! Inserindo cânula 1")
        if (introducao_canula1 == 4):
            break  #apenas para testar

    if introducao_canula1 == dorso_ventral:
        print("Cânula 1 inserida")
    print(" Drene o sangue e faça uma mistura de acrílico")

    introducao_canula2 = 0

    while (introducao_canula2 != dorso_ventral):
        introducao_canula2 += 1
        print("Aguarde! Inserindo cânula 2")
        if (introducao_canula2 == 4):
            break  #apenas para testar

    if introducao_canula2 == dorso_ventral:
        print("Cânula 2 inserida")


    print("Levar o animal até uma caixa aquecida por uma lâmpada")
    print("Ao acordar, colocar de volta na caixa-moradia")
    print ("Fim do procedimento")


else:
    #A literatura diz pra injetar + 10% da dose
    print ("Injete mais:" , dose_ketamina*0.1, "de ketamina")
    print ("Injete mais:" , dose_xilazina*0.1, "de xelazina")
    print ("O animal está anestesiado")

    print("Posicionar o animal no estereotáxico")
    ang_bregma = input("Digite o valor da angulação bregma: ")
    ang_lambda = input("Digite o valor da angulação lambda:  ")

    while ang_bregma != ang_lambda:
        print("A posição não esta correta. As angulações de bregma e lambda devem ser iguais")
        ang_bregma = input("Digite o valor da angulação bregma ")
        ang_lambda = input("Digite o valor da angulação lambda ")

    print("O animal está posicionado! Superfície de cirurgia plana")

    #Limpeza do campo de trabalho
    print("1 - Retire a pelagem que recobre a parte superior da calota craniana")
    print ("2 - Retire os tecidos moles: epiderme, derme e tecido conjuntivo")
    resposta1 = input("Alcançou a parte óssea da caixa craniana: (Responda S ou N) ")

    while resposta1 != "S":
        print("Continue retirando os tecidos moles")
        resposta1 = input("Alcançou a parte óssea da caixa craniana: (Responda S ou N) ")

    print("3 - Retire o resto de pele utilizando H2O2 10 volumes")
    print("Pronto! O campo de trabalho está limpo!")

    #IV
    print("Aplique uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos") 

    #V
    fixacao_parafusos = int(input("Escolha o ponto de fixação do parafuso. Recomenda-se escolher na parte posterior da calota craniana "))
    voltas = 1
    for i in range (1, 4): 
        print("Você deu :" , i, "volta(s) no parafuso")

    agulha_antero =0
    agulha_latero = 0
    agulha_dorso = 0

    antero_posterior=6
    latero_lateral=3.63
    dorso_ventral=4

    print("Ajustes definidos")

    #Furos para alcançar a meninge
    print(" Faça os furos para alcançar as meninges. Para isso, apoie a mão que segura a broca contra o assoalho em 45º")
    introducao_canula1 = 0

    while (introducao_canula1 != dorso_ventral):
        introducao_canula1 += 1
        print("Aguarde! Inserindo cânula 1")
        if (introducao_canula1 == 4):
            break  #apenas para testar

    if introducao_canula1 == dorso_ventral:
        print("Cânula 1 inserida")
    print(" Drene o sangue e faça uma mistura de acrílico")

    introducao_canula2 = 0

    while (introducao_canula2 != dorso_ventral):
        introducao_canula2 += 1
        print("Aguarde! Inserindo cânula 2")
        if (introducao_canula2 == 4):
            break  #apenas para testar

    if introducao_canula2 == dorso_ventral:
        print("Cânula 2 inserida")


    print("Levar o animal até uma caixa aquecida por uma lâmpada")
    print("Ao acordar, colocar de volta na caixa-moradia")
    print ("Fim do procedimento")






