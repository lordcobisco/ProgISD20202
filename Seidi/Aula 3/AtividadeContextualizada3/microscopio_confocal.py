# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:34:02 2020
Este programa simula a entrada de parâmetros de configuração de um microscópio
confocal de varredura laser. O programa não lida com tratamento de erros de dados, e
como a simulação é apenas de entrada de dados e processamento básico, as variáveis
não necessariamente possuem o tipo e valor para uso em um caso real.

@author: seidi
"""

# a. Crie as variáveis necessárias para que o programa funcione corretamente
# b. Inicialize as variáveis com valores padrão adequados.

# variáveis de formatação
maxWidthInCharacters = 96
underLineRep         = '_'*maxWidthInCharacters

# variáveis de configuração do microscópio

# rótulo para a célula em estudo
tipo_celula          = 'embrião de drosófila'

# a resolução é escolhida em termos de pixels, variando de 32x1 até 6144x6144
resolucaoX           = 4096 #pixels
resolucaoY           = 4096 #pixels

# valor de ajuste de resolução da profundidade de imagem
resolucaoZ           = 5 # micrometros

# taxa de aquisição em frames por segundo
frame_taxa_aquisicao = 0 # pontos por mm

# valor contínuo de zoom entre 0.5x e 40x
zoom                 = 2

# valor de abertura confocal
abertura             = 1.0

# valor em graus de 0 a 360 do angulo de rotação do scanner com passo de 0.1 grau
rotacao              = 0

# modo de detecção, pelo odelo Zeiss LSM 900, pode ser confocal ou airyscan
modo_deteccao        = 'Confocal'

# comprimento de onda do laser utilizado, acessado por meio de índice em 
#lista com valores fixos
# 1 = 405nm
# 2 = 488nm
# 3 = 561nm
# 4 = 640nm
ind_laser           = 1

# c. Crie uma pequena mensagem de apresentação do programa para realizar uma interface
#com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”

msg = 'Este programa apresenta a configuração de um microscópio confocal de varredura laser \
 previamente à aquisição de imagem'
print(msg)

# d. Solicite algumas informações necessárias para a configuração de um microscópio dessa
#natureza. Buscar pelo menos 10 itens para essas informações de entrada. Ex.: resolução
#da imagem desejada, tipo de célula a ser escaneada, faixa de iluminação necessária.

# e. Para cada informação digitada, apresente na tela a seguinte mensagem: “Houve
#alteração na variável inserida? ”. Após a mensagem, apresentar verdadeiro ou falso com
#base no que foi digitado pelo usuário e o que estava armazenado na variável. Obs.: Não
#deve ser utilizado if aqui.

print(underLineRep)
msg = 'Seção de inserção doa parâmetros de configuração'
print(msg)

msg = 'Houve alteração na variável inserida? '

print('\nrótulo para a célula em estudo')
new_tipo_celula = input('Digite o tipo de célula: ')
print(msg, tipo_celula != new_tipo_celula)

print('\na resolução é escolhida em termos de pixels, variando de 32x1 até 6144x6144')
new_resolucaoX = input('Digite a resolução em x (1 a 6144 pixels): ')
print(msg, resolucaoX != new_resolucaoX)

new_resolucaoY = input('Digite a resolução em y (1 a 6144 pixels): ')
print(msg, resolucaoY != new_resolucaoY)

# chutei uma faiza de valores para resolução em z
print('\nvalor de ajuste de resolução da profundidade de imagem')
new_resolucaoZ = input('Digite a resolução em z (1um a 20um): ')
print(msg, resolucaoZ != new_resolucaoZ)

print('\ntaxa de aquisição em frames por segundo')
new_frame_taxa_aquisicao = input('Digite a taxa de aquisição (8 a 64fps): ')
print(msg, frame_taxa_aquisicao != new_frame_taxa_aquisicao)

print('\nvalor contínuo de zoom entre 0.5x e 40x')
new_zoom = input('Digite o valor de zoom (0.5 a 40): ')
print(msg, zoom != new_zoom)

print('\nvalor de abertura confocal')
new_abertura = input('Digite o valor de abertura: ')
print(msg, abertura != new_abertura)

print('\nvalor em graus de 0 a 360 do angulo de rotação do scanner com passo de 0.1 grau')
new_rotacao = input('Digite o valor de rotação (0.0 a 360.0): ')
print(msg, rotacao != new_rotacao)

print('\nmodo de detecção, pelo odelo Zeiss LSM 900, pode ser "Confocal" ou "Airyscan"')
new_modo_deteccao = input('Digite o modo de detecção ("Confocal" ou "Airyscan"): ')
print(msg, modo_deteccao != new_modo_deteccao)

print('\ncomprimento de onda do laser utilizado, acessado por meio de índice em lista com valores fixos')
print('1 = 405nm')
print('2 = 488nm')
print('3 = 561nm')
print('4 = 640nm')
new_ind_laser = input('Digite o tipo de laser utilizado (1-4): ')
print(msg, ind_laser != new_ind_laser)

# f. Retorne ao usuário de forma organizada as informações que foram digitadas. Ex.: “As
#informações de configurações setadas pelo usuário são: ...”

print(underLineRep)
msg = "As informações de configurações setadas pelo usuário são:"
print(msg)

print('Tipo de célula:              ', new_tipo_celula)
print('Resolução em X:              ', new_resolucaoX)
print('Resolução em Y:              ', new_resolucaoY)
print('Resolução em Z:              ', new_resolucaoZ)
print('Taxa de aquisição:           ', new_frame_taxa_aquisicao)
print('Valor de zoom:               ', new_zoom)
print('Valor de abertura:           ', new_abertura)
print('Angulo de rotação:           ', new_rotacao)
print('Modo de detecção:            ', new_modo_deteccao)
print('Índice de esolha do laser:   ', new_ind_laser)




# g. Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a
#calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla
#correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.

print(underLineRep)
msg = 'Seção de calibração do equipamento no sentido horizontal'
print(msg)

# h. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
#foi corretamente digitada e mostrar o caractere pressionado.

count = 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite S: ')
print('você digitou (', count, '/10): ' , stepX)

count = 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite I: ')
print('você digitou (', count, '/10): ' , stepX)


# i. Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento
#no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do
#seu nome 10x e à penúltima letra do seu nome 10x.


print(underLineRep)
msg = 'Seção de calibração do equipamento no sentido vertical'
print(msg)


# j. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
#foi corretamente digitada e mostrar o caractere pressionado.


count = 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite E: ')
print('você digitou (', count, '/10): ' , stepX)

count = 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)
count += 1
stepX = input('Por favor, digite D: ')
print('você digitou (', count, '/10): ' , stepX)


# k. Finalmente, o programa deverá apresentar na tela que houve o término da calibração do
#sistema.

print(underLineRep)
msg = "O sistema está devidamente calibrado!"
print(msg)



# l. Para verificar que o programa está funcionando corretamente, execute-o colocando um
#breakpoint na linha 15. Tire um print da tela mostrando a linha parada e as informações
#armazenadas nas variáveis até então.