
#explicação do if
#palavra_chave = int(input("Você é inteligente? Responda 0 para nao e 1 para sim  "))

#if(palavra_chave):
#    print("Não deixe o trabalho para depois!")
#else:    #se a resposta for 0
#    print("Então seja")

#programa da  alimentação do rato
'''
botao1apertado = int(input("O rato apertou o botão 1? "))
botao2apertado = int(input("O rato apertou o botão 2? "))


if(botao1apertado and botao2apertado):
    print("Os dois botoões  foram apertados")

if(not botao1apertado and not botao2apertado):
    print("Nenhum dos botões foram apertados")

if(not botao1apertado and botao2apertado):
    print("Somente o botão 2 foi apertado")

if(botao1apertado and not botao2apertado):
    print("Somente o botão 1 foi apertado")
'''
#Usando string como variável
'''
botao1apertado = input("O rato apertou o botão 1? Responda S para sim ou N para não ")
botao2apertado = input("O rato apertou o botão 2? Responda S para sim ou N para não ")

if(botao1apertado == 's' and botao2apertado == 's'):
    print("Os dois botoões  foram apertados")

if(botao1apertado == 'n' and botao2apertado == 'n'):
    print("Nenhum dos botões foram apertados")

if(botao1apertado == 'n' and botao2apertado == 's'):
    print("Somente o botão 2 foi apertado")

if(botao1apertado == 's' and  botao2apertado != 's'): #tambem podemos usar != como diferente. 
    print("Somente o botão 1 foi apertado")

'''

#Instrução IF, ELSE
'''
botao1apertado = int(input("O rato apertou o botão 1? "))

if(botao1apertado):
    print("Botão apertado")
else:
    print("Botão nao apertado")

'''
#comparação numéria
'''
numero = int(input("Digite um numero " ))

if (numero>=5):
    print("Numero maior igual a 5")
else:
    print("Numero menor que 5")
'''

#laço aninhado

numero = int(input("Digite um numero " ))

if (numero<5):
    print("Numero é menor que 5")
elif(numero<10):
    print("Numero menor que 10")
elif(numero<15):
    print("Numero menor que 15")    
elif(numero<20):
    print("Numero menor que 20")    
else:
    print("Numero maior ou igual a 20")
    #elif executa apenas um entre todas