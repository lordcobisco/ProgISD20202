#Atividade Contextualizada - Aula 06

#Programa para cirurgia estereotáxica em animais 

# Primeiro vamos definir as variáveis

#Variáveis para posição do animal 

posicao = list()
parafusos = 0 
posicaoParafusos = list()
resp = ''

#Posições das agulhas (Valores em cm)

#Uso do dicionário
posicionamentoAgulhas = {'AP': 6.42, 'LL1': -3.23, 'LL2': 3.23, 'DV': 4.2}
#Uso da Tupla
posicoesdasAgulhas = ('AP', 'LL1', 'LL2', 'DV')
#Uso da lista
hipo = [-0.42, -0.3, 0.3, -0.2] 
anestesia = dict()
limpezaCranio=list()

#Início do programa

print('Bem-vindo(a) ao programa de cirurgia estereotáxica em animais.')
print('')
print('Este programa irá automatizar e auxiliar no procedimento cirúrgico.\n', 'Por favor, responda todas as perguntas da forma que são solicitdas. \n')

resp = input('Vamos começar a operação? Responda "sim" para continuar.\n')

while (resp != 'sim'):
    resp = input('Quando estiver pronto, digite "sim" para continuar.\n')

print('O programa foi iniciado e iremos continuar com a operação.')

#1ª Etapa

resp = ''

while (resp != 'sim'):
    anestesia['peso'] = float(input('Qual o peso do animal em gramas?\n'))
    anestesia['nome'] = input('Qual será o fármaco utilizado?\n')
    anestesia['quant'] = float(input('Qual a quantidade em ml?\n'))
    resp = input('Peso: %s \nFármaco: %s\nQuantidade em ml:%s \nDigite "sim" caso os parâmetros estejam corretos.\n' %(anestesia['peso'], anestesia['nome'], anestesia['quant']))
    if(resp != 'sim'):
	    print('Verifique e insira os parâmetros corretos\n')

#Fim da 1ª Etapa.

####################################################################

#2ª Etapa.

resp = ''

while (True):
    resp = input('O anestésico teve efeito?\n')
    if(resp == 'sim'):
        break
    print('Aguarde por um tempo para continuar.\n')

print('Por favor, posicione o animal no estereotáxico.\n')

while (True):
    while (True):  
        resp = input('As barras foram colocadas no ouvido externo do animal?\n')
        if(resp == 'sim'):
            posicao.append(True)
            break
        print ('Por favor, realize o posiocionamento das barras no ouvido externo do animal.\n')
        
    print ('Por favor, verifique a angulação da cabeça do animal. \n')
    resp = input('A angulação entre o bregma e o lambda é igual?\n')
    if (resp == 'sim'):
        posicao.append(True)
    else:
        posicao.append(False)

    if(False not in posicao):
        break
    else: 
        print('Realize o reposiocionamento.')

#Fim da 2ª Etapa. 


####################################################################


#3ª Etapa. 

print('Nesta etapa iremos realizar a limpeza do campo de trabalho.\n')

while(True):
    resp = input('Foi feita a retirada da pelagem que recobre a parte superior da calota craniana?\n')
    if(resp == 'sim'):
        limpezaCranio.append(True)
    else: 
        limpezaCranio.append(False)
    
    resp = input('Foi feita a retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até a parte óssea da caixa craniana?\n')
    if(resp == 'sim'):
        limpezaCranio.append(True)
    else: 
        limpezaCranio.append(False)
    
    resp = input('Foi realizada a limpeza da calota craniana com 10 volumes de H2O2? \n')
    if(resp == 'sim'):
        limpezaCranio.append(True)
    else:
        limpezaCranio.append(False)
    
    if(False not in limpezaCranio):
        print('Limpeza realizada com sucesso.')
        break
    else:
        print('A limpeza não foi concluída. Todos os passos devem ser realizados novamente.')

#Fim da 3ª Etapa.


####################################################################

#4ª Etapa.

resp=''

while(resp != 'sim'):
    print('Realize a aplicação de uma pequena camada de poliacrilato em todo o perímetro externo.\n')
    resp = input('A aplicação foi terminada? \n')

#Final da 4ª Etapa.


####################################################################

#5ª Etapa. 

while(True):
    while(not parafusos):
        parafusos = int(input('Quantos parafusos serão fixados?'))
    
    print('Hora de parafusa-los')
    for i in range(parafusos):
        resp = input('Informe onde o parafuso'+str(i+1)+'de'+str(parafusos)+'será posiocionado:\n')
        posicaoParafusos.append(resp)
    
    print('A fixação dos parafusos será: \n')
    for i in range(parafusos):
        print('Parafuso'+str(i+1)+':' +posicaoParafusos[i])
    resp = input('Você confirma as posições dos parafusos?\n')
    if(resp == 'sim'):
        print('Os parafusos foram fixados.')
        break
    else:
        print('Iremos reiniciar a fixação dos parafusos.')

#Final da 5ª Etapa.

####################################################################

#6ª Etapa.

print('Nesta etapa vamos realizar o posicionamento das agulhas.\n')
print('\nPocionamento das agulhas:')
for i in range(len(posicoesdasAgulhas)):
    print(posicoesdasAgulhas[i], ':', posicionamentoAgulhas[posicoesdasAgulhas[i]])

print('Realizando os ajustes das agulhas: \n')
for i in range(len(posicoesdasAgulhas)):
    posicionamentoAgulhas[posicoesdasAgulhas[i]] += hipo[i]

print('Novo posicionamento das agulhas:\n')
for i in range(len(posicoesdasAgulhas)):
    print(posicoesdasAgulhas[i], ':' , posicionamentoAgulhas[posicoesdasAgulhas[i]])

print('As agulhas foram posicionadas')

#Fim da 6ª Etapa.

####################################################################

#7ª Etapa.
print('Hora de realizar um furo com a broca até alcançar as meninges. \n')
while(True):
    print('Apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +/- 45° de angulação.\n')
    resp = input('Alcançou as meninges?\n')
    if(resp == 'sim'):
        print('Desligue a furadeira.')
        break
#Final da 7ª Etapa

####################################################################

#8ª Etapa

print('Cânula-guia inserida até o Dorsolateral: ', posicionamentoAgulhas[posicoesdasAgulhas[3]])

#Fim da 8ª Etapa

####################################################################

#9ª Etapa.

print('Realize a drenagem de todo o sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício. \nPara isso, utilize rolos de papel absorvente.')
while(True):
    resp = input('Procedimento realizado?\n')
    if(resp == 'sim'):
        break
    else:
        print('Realize o procedimento de drenagem.')

#Fim da 9ª Etapa

####################################################################

#10ª Etapa

print('Faça uma mistura do acrílico polimerizante com o solvente.\n')

while(True):
    resp = input('A mistura está espessa e maleável? \n')
    if(resp == 'sim'):
        print('Com a mistura faça um capacete abrangendo a cânula-guia, parafuso e o crânio.')
        break
    else:
        print('Reveja as proporções e ajuste.')
print('Espere secar até ficar ficar sufientemente rígido.')
while(True):
    resp = input('A mistura está rígida? \n')
    if(resp == 'sim'):
        break
    else: 
        print('Espere um pouco mais.')

#Fim da 10ª Etapa

####################################################################

#11ª Etapa

print('Nesta etapa, vamos fixar a outra cânula-guia.\n')

while(True):
    print('Erga levemente o  braço do estereotáxico cuidando que a cânula-guia não se movimente.\n')
    resp = input('A cânula-guia foi introduzida até o DorsoLateral na posição:' +str(posicionamentoAgulhas[posicoesdasAgulhas[3]])+'?\n')
    if(resp == 'sim'):
        break
    else:
        print('Realize uma nova tentativa de introduzir a cânula-guia.')

#Fim da 11ª Etapa

####################################################################

#12ª Etapa. (Reprodução da 9ª etapa)

print('Realize a drenagem de todo o sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício. \nPara isso, utilize rolos de papel absorvente.')
while(True):
    resp = input('Procedimento realizado?\n')
    if(resp == 'sim'):
        break
    else:
        print('Realize o procedimento de drenagem.')

#Fim da 12ª Etapa

####################################################################

#13ª Etapa (Reprodução da 10ª etapa)

print('Faça uma mistura do acrílico polimerizante com o solvente.\n')

while(True):
    resp = input('A mistura está espessa e maleável? \n')
    if(resp == 'sim'):
        print('Com a mistura faça um capacete abrangendo a cânula-guia, parafuso e o crânio.')
        break
    else:
        print('Reveja as proporções e ajuste.')
print('Espere secar até ficar ficar sufientemente rígido.')
while(True):
    resp = input('A mistura está rígida? \n')
    if(resp == 'sim'):
        break
    else: 
        print('Espere um pouco mais.')

#Fim da 13ª Etapa

####################################################################

#14ª Etapa

print('Levante com cuidado para evitar a movimentação das cânulas-guias fixadas')
print('Acomode o animal em uma caixa aquecida por uma lâmpada sem a presença de outros animais acordados.')
while(True):
    resp = input('Animal acomodado?\n')
    if(resp == 'sim'):
        break
    else:
        print('Acomodar o animal corretamente é extremamente importante. Reveja os passos e acomode-o.')

print('Quando o animal acordar, coloque-o de volta a sua caixa-moradia.')

print('Fim do programa de auxílio a cirurgia extereotáxica em animais.')


####################################################################

#Fim do programa