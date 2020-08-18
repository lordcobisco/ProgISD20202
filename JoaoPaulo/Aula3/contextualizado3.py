

#Tipos de laser que podem ser emitidos
laser450nm = 0
laser532nm = 0
laser630nm = 1
#Aberturas circulares que podem ser selecionadas
aberturacircular_50um = 0
aberturacircular_75um = 1
#Ampliação das lentes objetivas
objetiva_1x = 1
objetiva_50x = 0
objetiva_500x = 0
objetiva_5000x = 0
#Resolução da imagem a ser obtida
resolucao_alta = 1
resolucao_media = 0

print(laser630nm)
print(aberturacircular_75um)
print(objetiva_1x)
print(resolucao_alta)


print ("Este programa tem o objetivo de contar as células da lâmina colocada no microscópio confocal")

laser = int(input("Selecione o comprimento de onda que deseja utilizar \n 1)450nm \n 2)532nm \n 3)630nm \n "))
print ("Houve alteração de variável?")
if (laser == 3):
    print(bool(False))
    laser = str("630nm")
if(laser == 2):
    print(bool(True))
    laser = str("532nm")
if(laser == 1):
    print(bool(True))
    laser = str("450nm")
abertura = int(input("Selecione a abertura circular que deseja utilizar \n 1)50um \n 2)75um \n"))
print ("Houve alteração de variável?")
if (abertura == 2):
    print(bool(False))
    abertura = str("75um")
else:
    print(bool(True))
    abertura = str("50um")

objetiva = int(input("Selecione a objetiva que deseja utilizar \n 1)1x \n 2)50x \n 3)500x \n 4)5000x \n"))
print ("Houve alteração de variável?")
if (objetiva == 1):
    print(bool(False))
    objetiva = str("1x")
if(objetiva == 2):
    print(bool(True))
    objetiva = str("50x")
if(objetiva == 3):
    print(bool(True))
    objetiva = str("500x")
if(objetiva == 4):
    print(bool(True))
    objetiva = str("5000x")

resolucao = int(input("Selecione a resolução que deseja utilizar \n 1)Alta \n 2)Média \n"))
print ("Houve alteração de variável?")
if (resolucao == 1):
    print(bool(False))
    resolucao = str("Alta")
else:
    print(bool(True))
    resolucao = str("Baixa")


print("Resumindo as suas escolhas: \n Laser " + laser + "\n Abertura " + abertura + "\n Objetiva " + objetiva + "\n Resolução " + resolucao)

nome = str(input("Agora vamos calibrar o microscópio. Para isso, preciso do seu nome: "))
tamanho = len(nome)
primeira_letra = str(nome[0])
segunda_letra = str(nome[1])
penultima_letra = str(nome[tamanho-2])
ultima_letra = str(nome[tamanho-1])

print("primeira letra: " + primeira_letra + " Última: " + ultima_letra)
contador = 0
vezes_primeira_letra = str(input("Para calibrar o microscópio na horizontal, digite a PRIMEIRA LETRA do seu nome 10X: "))
while(contador < 9):
    if (vezes_primeira_letra == primeira_letra):
        contador+=1
        resto = 10 - contador
        resto = str(resto)
        print("Boa. Você digitou corretamente. A tecla digitada foi " + primeira_letra +". Continue digitando, só faltam "+ resto + " vezes")
        vezes_primeira_letra = str(input("Digite a primeira letra do seu nome: "))


vezes_ultima_letra = str(input("Estamos quase lá. Agora digite ÚLTIMA LETRA do seu nome 10X: "))
contador_ultima = 0
while(contador_ultima < 9):
    if (contador == 9 and vezes_ultima_letra == ultima_letra):
        contador_ultima+=1
        resto_ultima = 10 - contador_ultima
        resto_ultima = str(resto_ultima)
        print("Boa. Você digitou corretamente. A tecla digitada foi " + ultima_letra +". Continue digitando, só faltam "+ resto_ultima + " vezes")
        vezes_ultima_letra = str(input("Digite a última  letra do seu nome: "))
if(contador_ultima == 9 and contador == 9):
    print("Horizontal calibrada")


vezes_segunda_letra = str(input("Para calibrar o microscópio na horizontal, digite a SEGUNDA LETRA do seu nome 10X: "))
contador_segunda = 0
while(contador_segunda < 9):
    if (vezes_segunda_letra == segunda_letra):
        contador_segunda+=1
        resto_segunda = 10 - contador_segunda
        resto_segunda = str(resto_segunda)
        print("Boa. Você digitou corretamente. A tecla digitada foi " + segunda_letra +". Continue digitando, só faltam "+ resto_segunda + " vezes")
        vezes_segunda_letra = str(input("Digite a segunda letra do seu nome: "))

vezes_penultima_letra = str(input("Estamos quase lá. Agora digite PENÚLTIMA LETRA do seu nome 10X: "))
contador_penultima = 0
while(contador_penultima < 9):
    if (contador_segunda == 9 and vezes_penultima_letra == penultima_letra):
        contador_penultima+=1
        resto_penultima = 10 - contador_penultima
        resto_penultima = str(resto_penultima)
        print("Boa. Você digitou corretamente. A tecla digitada foi " + penultima_letra +". Continue digitando, só faltam "+ resto_penultima + " vezes")
        vezes_penultima_letra = str(input("Digite a última  letra do seu nome: "))
if(contador_penultima == 9 and contador_segunda == 9):
    print("Vertical calibrada")
if(contador_penultima == 9 and contador_segunda == 9 and contador == 9 and contador_ultima == 9):
    print("Microscopio calibrado com sucesso!!")
'''
if(vezes_primeira_letra[0] == primeira_letra and vezes_primeira_letra[1] == primeira_letra and vezes_primeira_letra[2] == primeira_letra and vezes_primeira_letra[3] == primeira_letra
and vezes_primeira_letra[4] == primeira_letra and vezes_primeira_letra[5] == primeira_letra and vezes_primeira_letra[6] == primeira_letra and vezes_primeira_letra[7] == primeira_letra
and vezes_primeira_letra[8] == primeira_letra and vezes_primeira_letra[9] == primeira_letra):
    print("Eixo horizontal calibrado")

vezes_ultima_letra = str(input("Agora, para calibrar o microscópio na vertical, digite a ÚLTIMA LETRA do seu nome 10X: "))
if(vezes_ultima_letra[0] == ultima_letra and vezes_ultima_letra[0][1] == ultima_letra and vezes_ultima_letra[0][2] == ultima_letra and vezes_ultima_letra[0][3] == ultima_letra
and vezes_ultima_letra[0][4] == ultima_letra and vezes_ultima_letra[0][5] == ultima_letra and vezes_ultima_letra[0][6] == ultima_letra and vezes_ultima_letra[0][7] == ultima_letra
and vezes_ultima_letra[0][8] == ultima_letra and vezes_ultima_letra[0][9] == ultima_letra):
    print("Eixo vertical calibrado")
'''