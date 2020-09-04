#######################
################Etapa 1
print('Inicio do procedimento de cirurgia esterotaxica.')

dic_anestesia = {'1': 'Ketamina e Xilazina', '2': 'Halotano (solucao gasosa)'}
sw_anestesia = input('\nDigite 1 para Ketamina e Xilazina, e 2 para Halotano (solucao gasosa): ')

if (sw_anestesia == '1'):
    print ('Foi selecionado o anestesico: ' + dic_anestesia['1'])
elif (sw_anestesia == '2'):
    print ('Foi selecionado o anestesico: ' + dic_anestesia['2'])

dose_anestesia = input('\nInsira a dosagem da ' + dic_anestesia[sw_anestesia] + ' desejada em mg: ')
print ('Sera administrado ' + str(dose_anestesia) + 'mg de ' + dic_anestesia[sw_anestesia])

#######################
################Etapa 2
fez_efeito = False; print('\n')

while (not fez_efeito):
    fez_efeito = input ('O animal ja esta adormecido? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar. ')

    if (fez_efeito):
        print('Animal pronto para continuidade da cirurgia.\n')

barras_posicionada = False

while (not barras_posicionada):
    barras_posicionada = input('Deseja posicionar as barras no ouvido externo? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar. ')
    
    if (barras_posicionada):
        print('Barras posicionadas\n')

bregma = 15
lamb = 32

while (bregma != lamb):
    print ('A orientacao do Bregma e do Lambda estao fora do eixo. Iguale-os para continuar a cirurgia.\n Bregma = ' + str(bregma) + ' Lambda = ' + str(lamb))

    bregma = bregma + int(input('Insira o valor de soma ou subtracao para deslocamento do Bregma: '))
    lamb = lamb + int(input('Insira o valor de soma ou subtracao para deslocamento do Lambda: '))

    if (bregma == lamb):
        print ('Bregma e Lambda alinhados\n')

#######################
################Etapa 3
print('Etapa de limpeza. É requerida a raspagem dos pelos do local, retirada de tecidos moles (epiderme, derme e tecido conjuntivo) para alcancar a parte ossea da caixa craniana.')

raspagem = False
while (not raspagem):
    raspagem = input('Raspar o local? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar. ')

    if (raspagem):
        print('Local devidamente sem pelos.')

lista_tecidos = ['Epiderme', 'Derme', 'Tecido conjuntivo']
h2o2 = 10

while (lista_tecidos):
    print ('O local ainda conta com as seguintes camadas de tecido mole: ' + str(lista_tecidos))
    
    if(input('Pressione algum caractere para retirar a camada ' + lista_tecidos[0])):
        lista_tecidos.pop(0)
    
    if (not lista_tecidos):
        while (h2o2 >= 0):
            h2o2 = h2o2 - int(input('\nLocal sem pelos e tecidos moles. Insira quantos volumes de H2O2 sao desejados para umedecer o algodao atual, ate utilizar os ' + str(h2o2) +' volumes restantes. '))

            if (h2o2 <= 0):
                print('Local totalmente limpo.\n')

#######################
################Etapa 4
poliacrilato = False

while(not poliacrilato):
    poliacrilato = input('\nEntre com algum caractere apos cobrir toda a superficie da cirurgia com Poliacrilato. ')

    if (poliacrilato):
        print('Poliacrilato aplicado.')

#######################
################Etapa 5
local_parafuso = 'Posterior da calota craniana'

mudar_local = bool(input('\nO ponto de fixacao padrao dos parafusos fica em \"' + local_parafuso + '\". Deseja alterar? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))

if (mudar_local):
    local_parafuso = input('\nInsira o nome do local desejado: ')
    print('Os parafusos serao fixados no seguinte local: ' + str(local_parafuso))

parafuso = 0.0
afixado = False

while (not afixado):
    parafuso = float(input('Quantas voltas deseja aplicar no parafuso, com casa decimal separada por \".\"? '))

    if (parafuso > 3):
        print ('NUMERO DE VOLTAS MAIOR QUE 3 NAO PERMITIDA'),

    elif (parafuso <= 0):
        print ('NUMERO DE VOLTAS 0, OU ABAIXO DE 0 NAO PERMITIDA')

    else:
        afixado = bool(input('Valor inserido: ' + str(parafuso) + ' voltas. Deseja confirmar? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))

        if (afixado):
            print('Confirmadas ' + str(parafuso) + ' voltas nos parafuso.\n')

tupla_posicoes = (6.42, 3.23, 4.2)

print('Insira os valores em cm, com casa decimal separada por \".\" encontrados nas reguas do estereotaxico para:')
AP = float(input('AP: '))
LL = float(input('LL: '))
DV = float(input('DV: '))

AP = tupla_posicoes[0] - AP
LL1 = tupla_posicoes[1] - LL; LL2 = tupla_posicoes[1] + LL
DV = tupla_posicoes[2] - DV

print('Respectivos valores de AP, LL1, LL2 e DV '); print(AP, LL1, LL2, DV)

#######################
################Etapa 6
print('Insersao das canulas-guia na ordem: LL (selecionar) -> LL (restante) -> AP')
flag_p = bool(input('Digite algum caractere para iniciar o procedimento por LL1, ou pressione enter sem nenhum caractere para iniciar por LL2: '))
if (flag_p):
    LL1_p = True
    print('Canula LL1 com a posicao definida')
    LL2_p = True
    print('Canula LL2 com a posicao definida')

else:
    LL2_p = True
    print('Canula LL2 com a posicao definida')
    LL1_p = True
    print('Canula LL1 com a posicao definida')

AP_p = True
print('Canula AP com a posicao definida')

#######################
################Etapa 7 ate Etapa 12
print('Furacao ate o alcance das meninges.')

angulo_broca = 0.0

profundidade_LL = 0.0
dic_dreno = {'1': 'Sangue', '2': 'Liquido Cefalorradiquiano', '3': 'Ambos'}
lista_LL = []
dreno = ''
braco_estereo = False # flag para checagem, caso seja a primeira ou segunda execucao da rotina
acrilico_polimerizante = 0
solvente = 0


if (flag_p):
    lista_LL = ['LL1', 'LL2']
else:
    lista_LL = ['LL2', 'LL1']

while (lista_LL):
    afixado = False
    meninge = False
    mistura_seca = False

    while (not afixado):
        angulo_broca = float(input('Qual angulo feito entre a posicao da broca com a superficie? Insira um valor maior que 44 e menor que 46 com casa decimal separada por \".\" para furar em ' + lista_LL[0]))

        if (angulo_broca >= 46):
            print ('ANGULACAO MAIOR OU IGUAL A 46 NAO PERMITIDA'),

        elif (angulo_broca <= 44):
            print ('ANGULACAO MENOR OU IGUAL A 44 NAO PERMITIDA')

        else:
            afixado = bool(input('Valor inserido: ' + str(angulo_broca) + ' graus. Deseja confirmar? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))

            if (afixado):
                print('Confirmadas ' + str(angulo_broca) + ' graus de inclinacao da broca em relacao a' + lista_LL[0] + '\n')

                while (not meninge):
                    profundidade_LL = round(profundidade_LL + float(input(str(round(DV-profundidade_LL, 4)) + 'cm de distancia ate o Dorso Ventral (DV). Insira algum valor de decremento com decimal separado por \".\" de modo a nao extrapolar o valor restante: ')), 4)

                    if (profundidade_LL > DV):
                        print('O VALOR INSERIDO PODE LESIONAR A MENINGE, INSIRA UM NOVO VALOR')
                        profundidade_LL = 0

                    elif (profundidade_LL == DV):
                        print('Profundidade de perfuracao ideal para ' + lista_LL[0])
                        meninge = True
                        profundidade_LL = 0

    #Etapa 9
    drenado = False

    while (not drenado):
        dreno = str(input('Quais fluidos estao presentes na area? 1 para Sangue, 2 para Liguido Cefalorraquidiano e 3 para ambos: '))

        if dreno in dic_dreno:
            print('Limpeza do(s) seguinte(s) fluido(s): ' + dic_dreno.get(dreno))

            if (bool(input('O local esta limpo? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))):
                drenado = True
        else:
            print('Fluido ' + str(dreno) + ' nao cadastrado.\n')

    #Etapa 10
    textura_ok = False
    lista_capacete = ['Cranio', 'Canula-guia', 'Parafuso']

    print('\nEtapa de manipulacao e moldagem do capacete de acrilico.')
    while (not mistura_seca):
        
        while (not textura_ok):
            
            if (braco_estereo):
                print('A mistura anterior esta seca. Preparar nova solucao, com quantidade reduzida apenas para cobrir os novos locais, mas com as mesmas proporcoes de antes:\n')
                print('Acrilico polimerizante: ' + str(acrilico_polimerizante) + 'g e Solvente: ' + str(solvente) + 'g Na proporcao de ' + str(round(acrilico_polimerizante/solvente, 2)) + ' medidas de acrilico polimerizante por 1 medida de solvente. \n')

            acrilico_polimerizante = round(acrilico_polimerizante + float(input('\nInsira, em gramas, a quantidade adicional desejada de acrilico polimerizante: ')), 2)
            solvente = round(solvente + float(input('Insira, em gramas, a quantidade adicional desejada de solvente: ')), 2)

            if (bool(input('\nA textura esta adequadamente espessa e maleavel? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))):
                print('Foram usados ' + str(acrilico_polimerizante) + 'g de acrilico polimerizante e ' + str(solvente) + 'g de solvente para a mistura')

                print('\nMontagem do capacete: ')

                while (lista_capacete):
                    
                    if (bool(input(lista_capacete[0] + ' esta completamente coberto?'))):
                        lista_capacete.pop(0)
                    else:
                        print('Realizar a cobertura completa de ' + lista_capacete[0] + '\n')
                    
                textura_ok = True

            
            else:
                print('Manipule mais acrilico e solvente.')

        mistura_seca = bool(input('\nO capacete esta seco? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))

        if (mistura_seca):
            
            braco_estereo = False
            while(not braco_estereo):
                braco_estereo = bool(input('\nA canula-guia pode ser retirada em seguranca? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))

                if (braco_estereo):
                    lista_LL.pop(0)
                else:
                    print('Condicione o paciente para retirada da canula-guia.')

        else:
            print('Aguarde o tempo de secagem. ')

#######################
################Etapa 13
print ('\nFim da cirurgia. Retirar o animalzinho devagar e coloca-lo em uma caixa segura e aquecida.')
lampada = False
outros_animais = True
dorimindo = True


while(not lampada):
    lampada = bool(input('\nA lampada esta acesa para aquecer a caixa? Insira qualquer caractere para continuar, ou pressione enter sem nenhum caractere para recusar: '))

    if (not lampada):
        print('Ligue a lampada.')

    else:
        print('Iluminacao e temperatura do local: Ok')

while(outros_animais):
    outros_animais = bool(input('\nExistem outros animais acordados na caixa? Insira qualquer caractere para indicar a presenca de outros animais, ou pressione enter sem nenhum caractere para continuar: '))

    if (outros_animais):
        print('Deixe a caixa em seguranca para uma melhor recuperacao do animal cirurgiado')
    
    else:
        print('Posicione o animal para o repouso.')

while(dorimindo):
    dorimindo = bool(input('\nO animal ainda esta dormindo? Insira qualquer caractere para indicar que o animal ainda esta dormindo, ou pressione enter sem nenhum caractere para continuar: '))

    if (dorimindo):
        print('Deixe o animal em repouso, ate ele despertar.')
    else:
        print('Retire-o cuidadosamente e aloque-o em sua caixa-moradia')

