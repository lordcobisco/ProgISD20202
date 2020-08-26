from os import system
system('clear')

resolucao = 128
tipoCelula = 'eucarionte'
reagente = 'Tipo 1'
interruptorArgonio = False
startSystem = False
larguraLasers = 7  # 7~10nm
digitalOffSet = 0
digitalGain = 0
speedAquisicao = 20
salvarFile = '/Documents'

print('Esse programa tem como objetivo receber dados para automatizar o uso do miscroscópio confocal.')

print('CONFIGURAÇÃO DO EQUIPAMENTO')
nome = input(
    'Olá, antes de configurar o equipamento gostaria de saber seu nome: ')

print('\nOlá, ' + nome+'!' + ' Agora vamos configurar o equipamento.')
# Deve ter 10 inputs
temp = resolucao
resolucao = int(input('Por favor, informe a resolução da imagem desejada' +
                      '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', resolucao != temp)

temp = tipoCelula
tipoCelula = input('\nTipo de celula a ser escaneada' +
                   '[Valor setado: ' + str(temp) + ']: ')
print('Houve alteração na variável inserida? ', tipoCelula != temp)

temp = reagente
reagente = input('\nInforme o tipo de reagente a utilizar' +
                 '[Valor setado: ' + str(temp) + ']: ')
print('Houve alteração na variável inserida? ', reagente != temp)

temp = interruptorArgonio
interruptorArgonio = bool(input(
    '\nInforme algum dado se deseja habilitar o interruptor de argônio' + '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', interruptorArgonio != temp)

temp = startSystem
startSystem = bool(input(
    '\nInforme algum dado se deseja habilitar o Start System' + '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', startSystem != temp)

temp = larguraLasers
larguraLasers = float(input(
    '\nInforme a largura dos lasers [7~9]' + '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', larguraLasers != temp)

temp = digitalOffSet
digitalOffSet = int(input('\nInforme o Digital OffSet' +
                          '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', digitalOffSet != temp)

temp = digitalGain
digitalGain = int(input('\nInforme o Digital Gain' +
                        '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', digitalGain != temp)

temp = speedAquisicao
speedAquisicao = int(input(
    '\nInforme a velocidade de aquisição' + '[Valor setado: ' + str(temp) + ']: '))
print('Houve alteração na variável inserida? ', speedAquisicao != temp)

temp = salvarFile
salvarFile = input('\nInforme a parsta de destino onde deseja salvar as imagens' +
                   '[Valor setado: ' + str(temp) + ']: ')
print('Houve alteração na variável inserida? ', salvarFile != temp)

print('\nAs informações de configuração setadas pelo usuário são: ')
print('Resolução: ', resolucao)
print('Tipo de Celula: ', tipoCelula)
print('Area de Pesquisa: ', reagente)
print('Interruptor do Argônio: ', interruptorArgonio)
print('Sistema iniciado: ', startSystem)
print('Largura dos Lasers: ', larguraLasers)
print('Digital OffSet: ', digitalOffSet)
print('Digital Gain: ', digitalGain)
print('Velocidade de Aquisição: ', speedAquisicao)
print('Pasta de Destino: ', salvarFile)

# CALIBRAÇÃO DO EQUIPAMENTO
print('\nVamos agora calibrar o equipamento.')

# Calibração Horizontal 1
calHorizontal = input(
    '\nDigite a primeira letra do seu nome 10x [letra ' + nome[0].lower() + ']:')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome 10x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 2
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 9x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 9x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 3
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 8x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 8x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 4
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 7x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 7x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 5
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 6x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 6x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 6
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 5x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 5x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 7
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 4x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 4x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 8
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 3x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 3x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 9
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais 2x [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais 2x [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Horizontal 10
calHorizontal = input(
    '\nDigite a primeira letra do seu nome mais uma vez [letra ' + nome[0].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[0].lower() + '] é', calHorizontal == nome[0].lower())
calHorizontal = input(
    'Digite a ultima letra do seu nome mais uma vez [letra ' + nome[-1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calHorizontal +
      '] e a letra de calibração horizontal [' + nome[-1].lower() + '] é', calHorizontal == nome[-1].lower())

# Calibração Vertical 1
print('\nVamos para calibração vertical agora.')

calVertical = input(
    '\nDigite a segunda letra do seu nome 10x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome 10x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 2
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 9x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 9x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 3
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 8x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 8x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 4
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 7x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 7x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 5
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 6x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 6x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 6
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 5x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 5x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 7
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 4x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 4x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 8
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 3x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 3x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 9
calVertical = input(
    '\nDigite a segunda letra do seu nome mais 2x [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais 2x [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

# Calibração Vertical 10
calVertical = input(
    '\nDigite a segunda letra do seu nome mais uma vez [letra ' + nome[1].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[1].lower() + '] é', calVertical == nome[1].lower())
calVertical = input(
    'Digite a penultima letra do seu nome mais uma vez [letra ' + nome[-2].lower() + ']: ')
print('O resultado da comparação entre a tecla pressinada [' + calVertical +
      '] e a letra de calibração vertical [' + nome[-2].lower() + '] é', calVertical == nome[-2].lower())

print('Fim da calibração. Equipamento pronto para utilização.')