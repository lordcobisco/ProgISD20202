# Habituação
print ("## HABITUAÇÃO ##")
habituacao_valor = "nao"
while habituacao_valor != "sim":
    habituacao_valor = input("Foi realizada as sessões de habituação no animal? (Responda 'sim' ou 'nao', sem as aspas)")
    if habituacao_valor == "sim":
        print ("\nAnimal habituado. Iniciar as sessões de treinamento")
        sessao_habituacao = True 
    else:
        print ("\nrealizar a etapa de habituação")
        sessao_habituacao = False

# Regime de aproximações sucessivas
if sessao_habituacao == True: 
    print ("\n## REGIME DE APROXIMAÇÕES SUCESSIVAS ##")
    aproximacao = 30
    while aproximacao>= 30:
        aproximacao = float(input("Qual a aproximação do animal em cm? "))
        if aproximacao < 30:
            print ("\nDar 0,5 mL de recompensa ao animal")
            animal_aproximado = True
        else:
            print ("\nAguardar a aproximação ficar menor que 30 cm")
            animal_aproximado = False

# TOCAR NA BARRA 20 x PARA O ANIMAL PASSAR PARA A PRÓXIMA ETAPA. O CÓDIGO TEM UM TOTAL DE 50 REPETIÇÕES PARA TENTAR ATINGIR OS 20 TOQUES
if animal_aproximado == True:
    numero_toques = 0
    while numero_toques < 20: 
        tocar = input("O animal tocou na barra? (Responda 'sim' ou 'não', sem as aspas")
        if (tocar == "sim"):
            print ("Dar 0,5 mL de recompensa ao animal")
            numero_toques = numero_toques + 1
    if numero_toques == 20:
        print ("\n## O experimento passou para a próxima etapa ##")  
        toques = True 

# RECOMPENSA COM O LADO DO SOM #

if toques == True:
    repeticoes_experimento = 0
    while repeticoes_experimento <= 50: 
        som = int(input ("O som emitido foi o 1 ou 2 ?(Responda '1' ou '2', sem as aspas"))
        lado = input ("Qual lado da barra o animal tocou? (Responda 'direita' ou 'esquerda', sem as aspas")
        if som == 1 and lado == "esquerda":
            print ("Dar 0,5 mL de recompensa ao animal")
            repeticoes_experimento = repeticoes_experimento + 1
        elif som == 2 and lado == "direita":
            print ("Dar 0,5 mL de recompensa ao animal")
            repeticoes_experimento = repeticoes_experimento + 1
        else:
            repeticoes_experimento = repeticoes_experimento + 1
            print ("Não liberar nenhuma recompensa")
# Tempo e repetições do experimento
    if repeticoes_experimento == 50:
        duracao = int(input("Qual foi a duração do experimento em minutos?"))
        if duracao <=30 and repeticoes_experimento >= 50:
            print ("O experimento seguirá para a próxima fase!")



