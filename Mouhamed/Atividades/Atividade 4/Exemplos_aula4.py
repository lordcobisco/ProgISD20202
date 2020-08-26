logicValue = int(input('Você é uma pessoa inteligente? \n'))

if(logicValue):
    print('Não deixe o trabalho para depois! \n')
print ( "Fim do programa")

botao1Apertado = int(input("O rato apertou o botão 1? (Responda 0 para não e 1 para sim)  "))
botao2Apertado = int(input("O rato apertou o botão 2? (Responda 0 para não e 1 para sim)  "))

if(botao1Apertado):
    print('O botão 1 foi apertado!')
if(not botao1Apertado):
    print('O botão 1 não foi apertado!')
if(botao2Apertado):
    print('O botão 2 foi apertado!')
if(not botao2Apertado):
    print('O botão 2 não foi apertado!')

if(not botao1Apertado and not botao2Apertado):
    print('Os dois botões não foram apertados!')
if(not botao1Apertado and botao2Apertado):
    print('Somente o botao 2 foi apertado')
if(botao1Apertado and not botao2Apertado):
    print('Somente o botao 1 foi apertado')
if(botao1Apertado and botao2Apertado):
    print('Os dois botões foram apertados!')

if(not botao1Apertado or not botao2Apertado):
    print('O botão 1 ou o botão 2 não foram apertados')
if(not botao1Apertado or botao2Apertado):
    print('O botão 1 não foi apertado ou o botão 2 foi apertado')
if(botao1Apertado or not botao2Apertado):
    print('O botão 1 foi apertado ou o botão 2 não foi apertado')
if(botao1Apertado or botao2Apertado):
    print('O botão 1 ou o botão 2 foram apertados')


botao1Apertado = input("O rato apertou o botão 1? \n  ")
botao2Apertado = input("O rato apertou o botão 2? \n ")


if(botao1Apertado  and not botao2Apertado):
    print('Adicionado 10mg de comida')
if(not botao1Apertado  and botao2Apertado ):
    print('Adicionado 20mg de comida')
if( not botao1Apertado  and not botao2Apertado):
    print('Nenhuma comida adicionada')
if(botao1Apertado and botao2Apertado ):
    print('Adicionado 40mg de comida')

print ("Fim do programa")

logicLazy = int(input("Você é preguiços@? \n  "))
logicInteligent = int(input("Você é inteligente? \n "))

if(logicLazy  and not logicInteligent):
    print('Preguiçoso e não muito inteligente \n')
if(not logicLazy  and not logicInteligent ):
    print('Não preguiçoso e não muito inteligente \n')
if( logicLazy  and logicInteligent):
    print('Preguiçoso e inteligente \n')
if(not logicLazy  and logicInteligent ):
    print('Não preguiçoso e inteligente \n')

print ("Fim do programa")

strLazy = input("Você é preguiços@? Digite s ou n\n  ")
strInteligent = input("Você é inteligente? Digite s ou n \n ")

if(strLazy == "s"  and strInteligent == "n"):
    print('Preguiçoso e não muito inteligente \n')
if(strLazy == "n"  and strInteligent == "n" ):
    print('Não preguiçoso e não muito inteligente \n')
if( strLazy == "s"  and strInteligent == "s"):
    print('Preguiçoso e inteligente \n')
if( strLazy =="n"  and strInteligent == "s" ):
    print('Não preguiçoso e inteligente \n')

print ("Fim do programa")


logicValue = int(input('Você é uma pessoa inteligente? \n'))

if(logicValue):
    print('Inteligente! \n')
else:
    print('Não inteligente! \n')

print ( "Fim do programa")


menor = int(input("Digite um numero menor que 5: \n"))

if menor > 5:
    print ("Ops, o numero digitado foi maior que 5 \n")
else:
    print(" Número digitado foi: ", menor)

print ("Fim do programa")


acao = int(input("Digite '1' para sim e '2' para não:"))

if (acao==1):
    print ("VocÊ disse sim")
elif (acao==2):
    print ("VocÊ disse nao")
else:
    print(" Você digitou um número diferente ")

print ("Fim do programa")


botao1Apertado = input("O rato apertou o botão 1? \n  ")
botao2Apertado = input("O rato apertou o botão 2? \n ")


if(botao1Apertado  and not botao2Apertado):
    print('Adicionado 10mg de comida')
elif(not botao1Apertado  and botao2Apertado ):
    print('Adicionado 20mg de comida')
elif( not botao1Apertado  and not botao2Apertado):
    print('Nenhuma comida adicionada')
else:
    print('Adicionado 40mg de comida')

print ("Fim do programa")
