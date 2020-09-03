# Atividade Contextalizada 06
from os import system
system('clear')

# Variáveis
# Usada para verificar que o animal está posicionado corretamente
posicionamento = list()
resposta = ''  # Variável auxiliar
parafusos = 0  # Quantidade de parafusos a serem fixados
posicaoParafusos = list()  # Posição onde os parafusos serão posicionados
# Posições utilizadas no posicionamento da agulha
posicoesAgulha = ('AP', 'LL1', 'LL2', 'DV') # Uso de tupla
# Dicionário contendo o posicionamento da agulha
posicionamentoAgulha = {'AP': 6.42, 'LL1': -3.23, 'LL2': 3.23, 'DV': 4.2} #Uso de dicinário
# Valores de CA1 para AP, LL(esquerda) e LL(direita) e DV
hipocampo = [-0.42, -0.3, 0.3, -0.2] # Uso de lista
farmaco = dict()
animal = dict()


print('Bem vindo(a) à cirurgia esterotáxica.')
print('Este programa vai automatizar o procedimento.')
print('Por favor, observe atentamente as perguntas e preencha os parâmetros conforme solicitado.')
resposta = input('Está pronto para começar [sim]?  ')

while(resposta.lower() != 'sim'):
    resposta = input(
        "\nNão entendi sua resposta. Digite 'sim' para dar inicio ao procedimento: ")

print('\nVamos iniciar!')
resposta = ''

# PROCEDIMENTO 1
while(resposta.lower() != 'sim'):
    farmaco['nome'] = input('Digite o fármaco que será utilizado: ')
    farmaco['quantidade'] = int(input('Quantidade (ml): '))
    animal['peso'] = float(input('Digite o peso do animal: '))
    resposta = input('A quantidade de ' + str(farmaco['quantidade'])+'ml de ' + str(
        farmaco['nome'])+' é adequada para um animal de '+str(animal['peso'])+'gramas? ')
    if(resposta != 'sim'):
        print('Informe os parâmetros novamente...\n')
# FIM DO PROCEDIMENTO 1

# PROCEDIMENTO 2
resposta = ''
while(True):
    resposta = input('\nO anestésico fez efeito? ')
    if(resposta.lower() == 'sim'):
        break
    print('Vamos aguardar...')

print('\nPosicione o animal no esterotáxico.')
while(True):
    while(True):
        resposta = input(
            '\nAs barras que suportam o peso do animal estão posicionadas no ouvido externo? ')
        if(resposta.lower() == 'sim'):
            posicionamento.append(True)
            break
        print('Por favor, posicione as barras no ouvido externo do animal.')

    resposta = input('\nO animal deu uma piscada ao posicionar as barras? ')
    if(resposta.lower() == 'sim'):
        posicionamento.append(True)
    else:
        posicionamento.append(False)

    print('Verifique a angulação da cabeça do animal.')
    resposta = input(
        '\nA cabeça do animal está na mesma angulação que o bregma e o lambda? ')
    if(resposta.lower() == 'sim'):
        posicionamento.append(True)
    else:
        posicionamento.append(False)

    resposta = input('\nO animal está posicionado corretamente? ')
    if(resposta.lower() == 'sim'):
        posicionamento.append(True)
    else:
        posicionamento.append(False)

    if(False not in posicionamento):
        break
    else:
        print('Reposicione...')
# FIM DO PROCEDIMENTO 2

# INICIO DO PROCEDIMENTO 3
print('Vamos realizar agora a limpeza do campo de trabalho.')

while(True):
    resposta = input(
        '\nA pelagem do animal que cobre a parte superior da calota craniana foi retirada? ')
    if(resposta.lower() == 'sim'):
        limpeza.append(True)
    else:
        limpeza.append(False)

    resposta = input(
        '\nOs tecidos moles foram retirados até o alcane do tecido ósseo? ')
    if(resposta.lower() == 'sim'):
        limpeza.append(True)
    else:
        limpeza.append(False)

    resposta = input(
        '\nA catola craniana foi limpa com 10 volumes de H2O2 para retirar qualquer resto de pele que esteja sobrando? ')
    if(resposta.lower() == 'sim'):
        limpeza.append(True)
    else:
        limpeza.append(False)

    if(False in not limpeza):
        print('Limpeza concluída.')
    else:
        print('Limpeza não concluída, vamos repetir todos os passos.')
# FIM DO PROCEDIMENTO 3

# INÍCIO DO PROCEDIMENTO 4
resposta = ''
while(resposta.lower() != 'sim'):
    print('\nAplique poliacrilato em todo o perímetro externo para evitar sangramentos.')
    resposta = input('Concluiu [sim]? ')
# FIM DO PROCEDIMENTO 4


# INÍCIO DO PROCEDIMENTO 5
while(True):
    parafusos = 0
    while(not parafusos):
        parafusos = int(
            input('\nDigite a quantidade de parafusos a serem fixados: '))

    print('\nCerto, vamos fixa-los.')
    for i in range(parafusos):
        resposta = input('Informe onde o parafuso '+str(i+1) +
                         ' de '+str(parafusos)+' será posicionado: ')
        posicaoParafusos.append(resposta)

    print('\nOs parafusos serão fixados conforme descrito abaixo:')
    for i in range(parafusos):
        print('Parafuso '+str(i+1)+': '+posicaoParafusos[i])
    resposta = input('Digite sim para confirmar as posições: ')
    if(resposta.lower() == 'sim'):
        print('\nParafusos fixados. Foram dadas até três voltas em cada parafuso.')
        break
    else:
        print('\nVamos reiniciar a fixação.')
# FIM DO PROCEDIMENTO 5

# INÍCIO DO PROCEDIMENTO 6
print('\nPosicionamento inicial da agulha:')
for i in range(len(posicoesAgulha)):
    print(posicoesAgulha[i], ': ', posicionamentoAgulha[posicoesAgulha[i]])

print('\nEfetuando ajustes da agulha...')
for i in range(len(posicoesAgulha)):
    posicionamentoAgulha[posicoesAgulha[i]] += hipocampo[i]

print('\nPosicionamento da agulha após ajustes:')
for i in range(len(posicoesAgulha)):
    print(posicoesAgulha[i], ': ', posicionamentoAgulha[posicoesAgulha[i]])

print('\nAgulhas posicionadas.')
# FIM DO PROCEDIMENTO 6

# INÍCIO DO PROCEDIMENTO 7
print('\nAgora que as agulhas foram posicionadas vamos fazr o furo com a broca até alcançar as meninges.')
while(True):
    print('\nFuradeira funcionando... Apoe sua mão sobre o assoalho e perfure o crânio a 45º de angulação.')
    resposta = input('Chegou às meninges? ')
    if(resposta.lower() == 'sim'):
        print('Furadeira parada.')
        break
# FIM DO PROCEDIMENTO 7

# INÍCIO DO PROCEDIMENTO 8
print('\nCánula-guia introduzida até o DorsoLateral, posição:',
      posicionamentoAgulha[posicoesAgulha[3]])
# FIM DO PROCEDIMENTO 8

# INÍCIO DO PROCEDIMENTO 9
print('\nDrene todo o sangue ou líquido cefalorraquidiano que esteja saindo do orifício criado no crânio.')
print('Utilize para isso pequenos rolos de papel absorvente.')
resposta = ''
while(True):
    resposta = input('\nDrenagem finalizada? ')
    if(resposta.lower() == 'sim'):
        break
    else:
        print('Execute a drenagem...')
# FIM DO PROCEDIMENTO 9

# INÍCIO DO PROCEDIMENTO 10
print('\nFaça uma mistrura de crílico com solvente. ')

while(True):
    resposta = input('\nA mistura está espessa porém variável? ')
    if(resposta.lower() == 'sim'):
        print('\nCom a mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso.')
        break
    else:
        print('Ajuste a mistura...')

print('\nEspere a mistura secar...')
while(True):
    resposta = input('\nA mistura está suficientemente rídiga? ')
    if(resposta.lower() == 'sim'):
        break
    else:
        print('\nEspere maus um pouco. O tempo de secagem varia de acordo com a temperatura e umidade da sala.')
# FIM DO PROCEDIMENTO 10


# INÍCIO DO PROCEDIMENTO 11
print('\nVamos agora fixar a outra cânunla-guia.')
while(True):
    print('\nLevante o braço do estereotáxico com cuidado para que a cânuna-guia previamente fixada não se movimente.')
    resposta = input('\nA cánula-guia foi introduzida até o DorsoLateral, posição:' +
                     str(posicionamentoAgulha[posicoesAgulha[3]])+'? ')
    if(resposta.lower() == 'sim'):
        break
    else:
        print('\nVamos tentar introduzir a cânula-guia novamente...')
# FIM DO PROCEDIMENTO 11

# INÍCIO DO PROCEDIMENTO 12
print('\nDrene todo o sangue ou líquido cefalorraquidiano que esteja saindo do orifício criado no crânio.')
print('Utilize para isso pequenos rolos de papel absorvente.')
resposta = ''
while(True):
    resposta = input('\nDrenagem finalizada? ')
    if(resposta.lower() == 'sim'):
        break
    else:
        print('Execute a drenagem...')

print('\nFaça uma mistrura de crílico com solvente. ')

while(True):
    resposta = input('\nA mistura está espessa porém variável? ')
    if(resposta.lower() == 'sim'):
        print('Com a mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso.')
        print('\nEspalhe o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete devido a entrada de sangue ou outro líquido entre o capacete e o crânio.')
        break
    else:
        print('Ajuste a mistura...')

print('\nEspere a mistura secar...')
while(True):
    resposta = input('\nA mistura está suficientemente rídiga? ')
    if(resposta.lower() == 'sim'):
        break
    else:
        print('\nEspere maus um pouco. O tempo de secagem varia de acordo com a temperatura e umidade da sala.')
# FIM DO PROCEDIMENTO 12


# INCÍCIO DO PROCEDIMENTO 13
print('\nLevantar bem devagar cuidado para que a cânulas-guia fixadas não se movimentem.')
print('Acomode o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados.')
while(True):
    resposta = input('Procedimento executado? ')
    if(resposta.lower() == 'sim'):
        break
print('Assim que o animal despertar coloque-o de volta a sua caixa-moradia.')
# FIM DO PROCEDIMENTO
