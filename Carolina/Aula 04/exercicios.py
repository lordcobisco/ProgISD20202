'''
botao1apertado = int(input("O rato apertou o botão 1?\n"))
botao2apertado = int(input("O rato apertou o botão 2?\n"))

if(botao1apertado and not botao2apertado):
    print("Foram adicionados 10mg de comida")
if(not botao1apertado and botao2apertado):
    print("Foram adicionados 20mg de comida")
if(not botao1apertado and not botao2apertado):
    print("Não foi adicionada nenhuma comida")
if(botao1apertado and botao2apertado):
    print("Foram adicionados 40mg de comida")

lazy = int(input("você é uma pessoa preguiosa?\n"))
intelligent = int(input("você é uma pessoa inteligente?\n"))

if(lazy and intelligent):
    print("Você é preguiçosa e inteligente")
if(not lazy and intelligent):
    print("Você é uma pessoa inteligente")
if(lazy and not intelligent):
    print("você é uma pessoa preguiçosa")
if(not lazy and not intelligent):
    print("você não é preguiçosa nem inteligente")

strlazy = input("você é uma pessoa preguiosa?\n")
strintelligent = input("você é uma pessoa inteligente?\n")

if(strlazy == "sim" and strintelligent == "sim"):
    print("Você é preguiçosa e inteligente")

if(not strlazy == "não" and strintelligent == "sim"):
    print("Você é uma pessoa inteligente")

if(strlazy == "sim" and not strintelligent == "não"):
    print("você é uma pessoa preguiçosa")

if(not strlazy == "não" and not strintelligent == "não"):
    print("você não é preguiçosa nem inteligente")

logicvalue = int(input("você é uma pessoa inteligente?\n"))
if(logicvalue):
    print("você é uma pessoa inteligente\n")
else: 
    print("você é uma pessoa preguiçosa\n")

numeromenor = int(input("digite um numero menor do que 5"))
if(numeromenor>5):
    print("ops!\n")
    print("o numero digitado foi maior do que 5!")
else:
    print("o numero digitado foi:", numeromenor)
'''
botao1apertado = int(input("O rato apertou o botão 1?\n"))
botao2apertado = int(input("O rato apertou o botão 2?\n"))

if(botao1apertado and not botao2apertado):
    print("Foram adicionados 10mg de comida")
elif(not botao1apertado and botao2apertado):
    print("Foram adicionados 20mg de comida")
elif(not botao1apertado and not botao2apertado):
    print("Não foi adicionada nenhuma comida")
else:
    print("Foram adicionados 40mg de comida")
