# Programas executados pelo professor André na Aula 04
'''
logicValue = int(input("Você é uma pessoa inteligente?\n"))

if(logicValue):
    print("Não deixe o trabalho para depois!\n")

print("Fim de programa!!")


logicLazy       = int(input("Você é uma pessoa Preguiçosa?\n"))
logicInteligent = int(input("Você é uma pessoa inteligente?\n"))

if(logicLazy and not logicInteligent):
    print("Você é preguiçoso(a) e não é muito inteligente\n")

if(not logicLazy and not logicInteligent):
    print("Você não é preguiçoso(a) e não é muito inteligente\n")

if(logicLazy and logicInteligent):
    print("Você é preguiçoso(a) e inteligente\n")

if(not logicLazy and logicInteligent):
    print("Você não é preguiçoso(a) e é inteligente\n")

print("Fim de programa!!")

strLazy       = input("Você é uma pessoa Preguiçosa?\n")
strInteligent = input("Você é uma pessoa inteligente?\n")

if(strLazy == "s" and strInteligent == "n"):
    print("Você é preguiçoso(a) e não é muito inteligente\n")

if(strLazy == "n" and strInteligent == "n"):
    print("Você não é preguiçoso(a) e não é muito inteligente\n")

if(strLazy == "s" and strInteligent == "s"):
    print("Você é preguiçoso(a) e inteligente\n")

if(strLazy == "n" and strInteligent == "s"):
    print("Você não é preguiçoso(a) e é inteligente\n")

print("Fim de programa!!")


botao1Apertado = int(input("O rato apertou o botão 1?\n"))
botao2Apertado = int(input("O rato apertou o botão 2?\n"))

if (botao1Apertado and not botao2Apertado):
    print("Foram adicionados 10mg de comida")
if (not botao1Apertado and botao2Apertado):
    print("Foram adicionados 20mg de comida")
if (not botao1Apertado and not botao2Apertado):
    print("Nenhuma comida foi adicionada")
if (botao1Apertado and botao2Apertado):
    print("Foram adicionados 40mg de comida")

print("Fim de programa!!")

logicValue = int(input("Você é uma pessoa inteligente?\n"))

if(logicValue):
    print("Você é inteligente!\n")
else:
    print("Você não é inteligente!\n")

print("Fim de programa!!")

numeroMenor = int(input('Digite um numero menor que 5: '))
if numeroMenor > 5:
    print ("ops!\n")
    print ("O numero digitado e maior que 5")
else:
    print ("Numero digitado foi: ", numeroMenor)

print("Fim de programa!!")


acao = int(input("Digite '1' para sim e digite '2' para não: "))
if(acao==1):
    print("Você disse que sim!")
elif(acao==2):
    print("Você disse que não!")
else:
    print("O número digitado não é '1' e nem '2'!!!")

print("Fim de programa!!")
'''

botao1Apertado = int(input("O rato apertou o botão 1?\n"))
botao2Apertado = int(input("O rato apertou o botão 2?\n"))

if (botao1Apertado and not botao2Apertado):
    print("Foram adicionados 10mg de comida")
elif (not botao1Apertado and botao2Apertado):
    print("Foram adicionados 20mg de comida")
elif (not botao1Apertado and not botao2Apertado):
    print("Nenhuma comida foi adicionada")
else:
    print("Foram adicionados 40mg de comida")

print("Fim de programa!!")
