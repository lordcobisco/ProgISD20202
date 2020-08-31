# Habituação
print ("## HABITUAÇÃO ##")
sessao_habituacao = input("Foi realizada as sessões de habituação no animal? (Responda 'sim' ou 'não', sem as aspas)")
if sessao_habituacao == "sim":
    print ("Animal habituado. Iniciar as sessões de treinamento")
    sessao_habituacao = True 
else:
    print ("realizar a etapa de habituação")
    sessao_habituacao = False

# Regime de aproximações sucessivas
if sessao_habituacao == True: 
    print ("## REGIME DE APROXIMAÇÕES SUCESSIVAS ##")
    aproximacao = 30
    aproximacao = float(input("Qual a aproximação do animal em cm? "))
    if aproximacao < 30:
        print ("Dar 0,5 mL de recompensa ao animal")
        animal_aproximado = True
    else:
        print ("Aguardar a aproximação ficar menor que 30 cm")
        animal_aproximado = False

# TOCAR NA BARRA 20 x PARA O ANIMAL PASSAR PARA A PRÓXIMA ETAPA. O CÓDIGO TEM UM TOTAL DE 50 REPETIÇÕES PARA TENTAR ATINGIR OS 20 TOQUES

if animal_aproximado == True:
    #1° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    numero_toques = 0
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #2° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #3° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #4° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #5° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #6° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #7° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #8° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
         print ("Dar 0,5 mL de recompensa ao animal")
         numero_toques = numero_toques + 1

    #9° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #10° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #11° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #12° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #13° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #14° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #15° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #16° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1
    #17° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #18° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #19° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #20° rodada
    tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
    if (tocar == "sim"):       
        print ("Dar 0,5 mL de recompensa ao animal")
        numero_toques = numero_toques + 1

    #21° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #22° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #23° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #24° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #25° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #26° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #27° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #28° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #29° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #30° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #31° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #32° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #33° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #34° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #35° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #36° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #37° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #38° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #39° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #40° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #41° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #42° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #43° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #44° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #45° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #46° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #47° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #48° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim") and (numero_toques < 20):       
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #49° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1

    #50° rodada
    if numero_toques<20:
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1
    if numero_toques >=20:
        print ("\n## O experimento passou para a próxima etapa ##")  
        toques = True 

# RECOMPENSA COM O LADO DO SOM #

if toques == True:
    som = int(input ("O som emitido foi o 1 ou 2 ?(Responda '1' ou '2', sem as aspas"))
    lado = input ("Qual lado da barra o animal tocou? (Responda 'direita' ou 'esquerda', sem as aspas")
    if som == 1 and lado == "esquerda":
        print ("Dar 0,5 mL de recompensa ao animal")
    elif som == 2 and lado == "direita":
        print ("Dar 0,5 mL de recompensa ao animal")
    else:
        print ("Não liberar nenhuma recompensa")

# Tempo e repetições do experimento
duracao = int(input("Qual foi a duração do experimento em minutos?"))
repeticoes = int(input("Qual foi o número de repetições do experimento? "))
if duracao <=30 and repeticoes >= 50:
    print ("O experimento seguirá para a próxima fase!")
else:
    print ("o experimento ainda não seguirá para a próxima fase")


