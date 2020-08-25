'''
logicValue = int(input("Você é inteligente? (Responda 0 para não e 1 para sim)"))
#já é uma variavel logica

if(logicValue):
    print('Não deixe pra estudar depois')


# revisão: quando falo not o fica 1 ou 1 fica o, pois a variavel ja da como verdadeira


botao1Apertado = int(input("O rato apertou o botão 1? (Responda 1 para sim e 2 para não)\n"))
botao2Apertado = int(input("O rato apertou o botão 2? (Responda 1 para sim e 2 para não)\n"))
#se eu quiser deixar string, tirar o int.. ai tenho que fazer o == 's' or == 'n'


if (botao1Apertado):
    print (' Botão 1 foi apertado')
if (not botao1Apertado):
    print (' Botão 1 não foi apertado')
if (botao1Apertado and not botao2Apertado):
    print (' Botão 1 foi e 2 não foi apertado')
if (botao1Apertado or botao2Apertado):
    print (' Botão 1 ou 2 foram apertados')
    if (botao1Apertado):
        print('Foi o 1')
    else:
        print('Foi o 2')

'''



