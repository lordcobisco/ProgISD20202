

logicValue = int(input("Você está usando máscara?\n"))

if(logicValue):
    print("Parabéns!\n")



print("Fim do programa!!")

################################################################################### 

logicChocolate = int(input("Você gosta de chocolate?\n"))
logicCafe = int(input("Você gosta de café?\n"))

if(logicChocolate and not logicCafe):
    print("Você gosta de chocolate e não gosta de café\n")

if(not logicChocolate and not logicCafe):
    print("Você não nao gosta de chocolate e não gosta de café\n")

if(logicChocolate and logicCafe):
    print("Você gosta de chocolate e de café\n")

if(not logicChocolate and logicCafe):
    print("Você não gosta de chocolate e nem de café\n")

print("Fim de programa!!")

#####################################################################################


strChocolate  = input("Você gosta de chocolate?\n")
strCafe = input("Você gosta de café?\n")

if(strChocolate == "s" and strCafe == "n"):
    print("Você gosta de chocolate e não gosta de café\n")

if(strChocolate == "n" and strCafe == "n"):
    print("Você não gosta de chocolate e nem de café\n")

if(strChocolate == "s" and strCafe == "s"):
    print("Você gosta de chocolate e de café\n")

if(strChocolate == "n" and strCafe == "s"):
    print("Você não gosta de chocolate e sim de café\n")

print("Fim de programa!!")

######################################################################################

encostouBarra1 = int(input("O rato encostou na barra 1?\n"))
encostouBarra2 = int(input("O rato encostou na barra 2?\n"))

if ( encostouBarra1  and not encostouBarra2 ):
    print("Foram adicionados 10mg de comida")
if (not encostouBarra1 and encostouBarra2):
    print("Foram adicionados 20mg de comida")
if (not encostouBarra1 and not encostouBarra2):
    print("Nenhuma comida foi adicionada")
if (encostouBarra1 and encostouBarra2):
    print("Foram adicionados 40mg de comida")

print("Fim de programa!!")

####################################################################################

encostouBARRA1 = int(input("O rato encostou na barra 1?\n"))
encostouBARRA2 = int(input("O rato encostou na barra 2?\n"))

if ( encostouBARRA1  and not encostouBARRA2 ):
    print("Recebeu uma gota de líquido")
elif (not encostouBARRA1 and encostouBARRA2):
    print("Recebeu duas gotas de líquido")
elif (not encostouBARRA1 and not encostouBARRA2):
    print("Não recebeu nada")
elif (encostouBARRA1 and encostouBARRA2):
    print("Recebeu comida")
else:

    print("Fim de programa!!")

##############################################################


variavelLogica = int(input("Você é uma pessoa legal?\n"))

if(variavelLogica):
    print("Que bom. Continue assim\n")
else:
    print("Seja legal\n")

print("Fim de programa!!")


numeroMenordigite = int(input('Digite um numero menor que 60: '))
if numeroMenordigite < 60:
    print ("Isso aí. Digitou certo\n")
    
else:
    print ("Digitou errado")

print("Fim de programa!!")

########################################################################################

escolhaAnimais = int(input("Digite '1' para rato e digite '2' para coelho: "))
if(escolhaAnimais==1):
    print("Você escolheu rato!")
elif(escolhaAnimais==2):
    print("Você escolheu coelho!")
else:
    print("Escolha um dos animaizinhos")



print("Fim de programa!!")



