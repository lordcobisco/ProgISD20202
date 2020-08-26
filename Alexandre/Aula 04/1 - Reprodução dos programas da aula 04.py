#True e false
logic_value = int(input("Você se acha inteligente? (Digite 0 para não e 1 para sim)"))
if (logic_value):
    print ("Faça sempre os trabalhos o mais antecipadamente possível")
print ("Fim do programa")

# True e false + operadores lógicos
botao_apertado1 = int(input("O botão 1 foi apertado? (Digite 0 para não e 1 para sim)"))
botao_apertado2 = int(input("O botão 2 foi apertado? (Digite 0 para não e 1 para sim)"))

if (botao_apertado1 and not botao_apertado2):
    print ("Somente o botão 1 foi pressionado")
if (not botao_apertado1 and botao_apertado2):
    print ("Somente o botão 2 foi pressionado")
if (not botao_apertado1 and not botao_apertado2):
    print ("Nenhum dos dois botões foram pressionados")
if (botao_apertado1 and botao_apertado2):
    print ("Os dois botões foram pressionados")
print ("Fim do programa")

#  Operadores relacionais
botao_apertado1 = input("O botão 1 foi apertado? (Digite n para não e s para sim)")
botao_apertado2 = input("O botão 2 foi apertado? (Digite n para não e s para sim)")

if(botao_apertado1 == 's'):
    print('O botão 1 foi apertado!')
if(botao_apertado1 == 'n'):
    print('O botão 1 não foi apertado!')
if(botao_apertado2 == 's'):
    print('O botão 2 foi apertado!')
if(botao_apertado2 == 'n'):
    print('O botão 2 não foi apertado!')  
if(not (botao_apertado1 == 's')):
    print('O botão 1 não foi apertado!')
print ("Fim do programa")

#  Opeadores lógicos + Operadores relacionais
botao_apertado1 = input("O botão 1 foi apertado? (Digite n para não e s para sim)")
botao_apertado2 = input("O botão 2 foi apertado? (Digite n para não e s para sim)")

if(botao_apertado1  == 's' and botao_apertado2  == 's'):
    print('Os dois botões foram apertados!')
if(not botao_apertado1 == 's' and not botao_apertado2 == 's'):
    print('Os dois botões não foram apertados!')
if(not botao_apertado1  == 's' and botao_apertado2 == 's'):
    print('Somente o botao 2 foi apertado')
if(botao_apertado1  == 's' and not botao_apertado2 == 's'):
    print('Somente o botao 1 foi apertado')

if(botao_apertado1  == 's' or botao_apertado2  == 's'):
    print('O botão 1 ou o botão 2 foram apertados')
if(not botao_apertado1  == 's' or not botao_apertado2  == 's'):
    print('O botão 1 ou o botão 2 não foram apertados')
print ("Fim do programa")

# If e else + True e false
botao_apertado1 = int(input("O botão 1 foi apertado? (Digite 0 para não e 1 para sim)"))
if (botao_apertado1):
    print ("O botao 1 foi pressionado")
else:
    print ("O botão 1 não foi pressionado")

#If e else + operadores relacionais
numero = float(input("Digite um número que seja menor do que 10"))
if numero<10:
    print ("O numéro é menor que 10")
else:
    print("Ops, o número é maior ou igual a 10")
print ("Fim do programa")

#If, elif e else
numero = float(input("Digite um número"))
if numero < 10:
    print ("O númer é menor do que 10")
elif numero <20:
    print ("O número é maior ou igual a 10 e menor que 20")
elif numero <30:
    print ("O número é maior ou igual a 20 e menor que 30")
else:
    print ("O número é maior ou igual a 30")
print ("Fim do programa!")

botao_apertado1 = int(input("O botão 1 foi apertado? (Digite 0 para não e 1 para sim)"))
botao_apertado2 = int(input("O botão 2 foi apertado? (Digite 0 para não e 1 para sim)"))

if (botao_apertado1 and not botao_apertado2):
    print ("Somente o botão 1 foi pressionado")
elif (not botao_apertado1 and botao_apertado2):
    print ("Somente o botão 2 foi pressionado")
elif (not botao_apertado1 and not botao_apertado2):
    print ("Nenhum dos dois botões foram pressionados")
else:
    print ("Os dois botões foram pressionados")
print ("Fim do programa")





