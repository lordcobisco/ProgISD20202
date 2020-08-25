'''
logicValue = int(input('Você é uma pessoa inteligente? (Responda 0 para não e 1 para sim)'))

if(logicValue):
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')
    print('Não deixe o trabalho para depois')

print('Depois do if')
'''
'''
botao1Apertado = int(input('O rato apertou o botão 1? (Responda 0 para não e 1 para sim)'))
botao2Apertado = int(input('O rato apertou o botão 2? (Responda 0 para não e 1 para sim)'))

if(botao1Apertado):
    print("O botão 1 foi apertado")
if(not botao1Apertado):
    print('O botão 1 não foi apertado')

if(botao2Apertado):
    print("O botão 2 foi apertado")
if(not botao2Apertado):
    print('O botão 2 não foi apertado')

if(not botao1Apertado and not botao2Apertado):
    print('Nenhum dos dois botões foram apertados')
if(botao1Apertado and botao2Apertado):
    print('Os dois botões foram apertados')
if(not botao1Apertado and botao2Apertado):
    print('Somente o botão 2 foi apertado')
if(botao1Apertado and not botao2Apertado):
    print('Somente o botão 1 foi apertado')

if(not botao1Apertado or not botao2Apertado):
    print('O botão 1 ou o botão 2 não foram apertados')
if(botao1Apertado or botao2Apertado):
    print('O botão 1 ou o botão 2 foram apertados')
if(not botao1Apertado or botao2Apertado):
    print('O botão 2 foi apertado ou o botão 1 não foi apertado')
if(botao1Apertado or not botao2Apertado):
    print('O botão 1 foi apertado ou o botão 2 não foi apertado')
'''

'''
botao1Apertado = (input('O rato apertou o botão 1? (Responda n para não e s para sim)'))
botao2Apertado = (input('O rato apertou o botão 2? (Responda n para não e s para sim)'))

if(botao1Apertado == 's'):
    print("O botão 1 foi apertado")
if(not botao1Apertado == 'n'):
    print('O botão 1 não foi apertado')

if(botao2Apertado == 's'):
    print("O botão 2 foi apertado")
if(not (botao2Apertado != 's')):
    print('O botão 2 não foi apertado')

if(not (botao1Apertado != 'n') and not (botao2Apertado != 'n')):
    print('Nenhum dos dois botões foram apertados')
if(botao1Apertado and botao2Apertado):
    print('Os dois botões foram apertados')
if(not botao1Apertado and botao2Apertado):
    print('Somente o botão 2 foi apertado')
if(botao1Apertado != 's' and not botao2Apertado != 'n'):
    print('Somente o botão 1 foi apertado')


if(not (botao1Apertado != 'n' or not botao2Apertado !='n')):
    print('O botão 1 ou o botão 2 não foram apertados')
if(botao1Apertado !='s' or botao2Apertado != 's'):
    print('O botão 1 ou o botão 2 foram apertados')
if(not (botao1Apertado != 'n' or botao2Apertado != 's')):
    print('O botão 2 foi apertado ou o botão 1 não foi apertado')
if(botao1Apertado != 's' or not botao2Apertado !='n'):
    print('O botão 1 foi apertado ou o botão 2 não foi apertado')
'''

'''
botao1Apertado = int(input('O rato apertou o botão 1? (Responda 0 para não e 1 para sim)'))

if(botao1Apertado):
    print('O botão foi apertado')
else:
    print('O botão não foi apertado')
if(True):
    print('true')

print('Depois do if')

'''
'''
numeroDigitado = float(input('Digite um numero'))

if(numeroDigitado > 5):
    print('O número é maior que 5 \n')
else:
    print('O número é menor ou igual a 5 \n')
'''

numeroDigitado = float(input('Digite um numero'))

if(numeroDigitado < 5):
    print('O número é menor que 5 \n')
elif(numeroDigitado < 10):
    print('O número é menor que 10 \n')
elif(numeroDigitado < 15):
    print('O número é menor que 15 \n')
elif(numeroDigitado < 20):
    print('O número é menor que 20 \n')
else:
    print('O número é maior ou igual a 20 \n')

print('Fim de programa')






    

    
