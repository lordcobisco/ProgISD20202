
#instrução True/false utilizando if:
logicValue = int(input("Você é uma pessoa inteligente?\n"))
if (logicValue):
    print("Não deixe de estudar gigante!\n")
print ("FIM DO PROGRAMA")

botao1Apertado = int(input("O rato apertou o botão 1?\n"))
botao2Apertado = int(input("O rato apertou o botão 2?\n"))
if (botao1Apertado and not botao2Apertado) :
    print ("Foram adicionados 10mg de comida")
if (not botao1Apertado and botao2Apertado) :
    print ("Foram adicionados 20mg de comida")
if (not botao1Apertado and not botao2Apertado) :
    print ("Nenhuma comida foi adicionada")
if (botao1Apertado and botao2Apertado) :
    print ("Foram adicionados 40mg de comida")
print ("FIM DO PROGRAMA")

#instrução True/false + operadores lógicos utilizando if:
logicLazy = int(input("Você é uma pessoa preguiçosa?\n"))
logicInteligent = int(input("Você é uma pessoa inteligente?\n"))
if(logicLazy and logicInteligent):
    print ("Você é preguiçoso e inteligente\n")
if(logicLazy and not logicInteligent):
    print ("Você é preguiçoso e não é inteligente\n")
if(not logicLazy and logicInteligent):
    print ("Você não é preguiçoso e é inteligente\n")
if(not logicLazy and not logicInteligent):
    print ("Você não é preguiçoso e não é inteligente\n")
print ("FIM DO PROGRAMA")

#instrução string + operadores lógicos e relacionais utilizando if:
logicLazy = (input("Você é uma pessoa preguiçosa?\n"))
logicInteligent = (input("Você é uma pessoa inteligente?\n"))
if(logicLazy == "s" and logicInteligent == "s"):
    print ("Você é preguiçoso e inteligente\n")
if(logicLazy == "s" and logicInteligent == "n"):
    print ("Você é preguiçoso e não é inteligente\n")
if(logicLazy == "n" and logicInteligent == "s"):
    print ("Você não é preguiçoso e é inteligente\n")
if(logicLazy == "n" and logicInteligent == "n"):
    print ("Você não é preguiçoso e não é inteligente\n")
print ("FIM DO PROGRAMA")

#true e false utilizando if e else
logicValue = int(input("Você é uma pessoa inteligente?\n"))
if (logicValue):    
    print("Você é inteligente!\n")
else:
    print("Você não é inteligente!\n")
print ("FIM DO PROGRAMA") 
numeroMenor = int(input("Digite um número menor que 5: "))
if numeroMenor > 5:
    print("O número digitado é maior que 5\n")
else:
    print("O numero digitado foi", numeroMenor)
print ("FIM DO PROGRAMA") 

#true e false utilizando if, elif e else
acao = int(input("Digite '1' para sim e '2' para não: \n"))
if (acao==1):
    print ("Você disse que sim!")
elif (acao ==2):
    print ("Você disse que não")
else:    
    print("O número digitado estrá fora dos padrões solicitados!")
print("FIM DO PROGRAMA") 

#true e false utilizando if, elif e else
botao1Apertado = int(input("O rato apertou o botão 1?\n"))
botao2Apertado = int(input("O rato apertou o botão 2?\n"))

if (botao1Apertado and not botao2Apertado):
    print ("Foram adicionados 10mg de comida")
elif (not botao1Apertado and botao2Apertado):
    print ("Foram adicionados 20mg de comida")
elif (not botao1Apertado and not botao2Apertado):
    print ("Nenhuma comida foi adicionada")
else:
    print ("Foram adicionados 40mg de comida")
print ("FIM DO PROGRAMA")
