'''
    Arquivo Atualizado em 13 de setembro de 2020.
    Incrementado:
    Inclua no exercício de Método de discriminação de estímulos auditivos para primatas através do condicionamento operante uma atualização
    (com commit e documentação atualizada(seguir o fluxo padrão de atualização de códigos, documente a necessidade de uma nova funcionalidade
    no programa, cadastre ao projeto um novo milestone com issues associados)):

    Requisito:
    1. Solicitar ao usuário a forma de salvar os dados
    2. Salvar os dados gerados em um arquivo txt
    3. Salvar os dados gerados em um arquivo csv

'''
from os import system
system('clear')

def armazenar(arquivo, tipo, texto):
    if(tipo == 'txt'):
        arquivo.write(texto)
    elif(tipo == 'csv'):
        spamwriter = csv.writer(arquivo, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(texto)

# INICIANDO VARIÁVEIS
toqueBarra = 0  # Número de toques na barra
distanciaEstabelecida = 30  # Distância em cm do animal às barras
som1 = False  # Som Phee - Indica que o som Phee está sendo emitido
som2 = False  # Som Trill - Indica que o som Trill está sendo emitido
animalHabituado = False
etapaAproximacao = False
etapaSomToque = False
distanciaEstabelecida = 30  # 30cm
barraEsquerda = False  # Indica o toque na barra esquerda
barraDireita = False  # Indica o toque na barra direita
tempoValido = True  # Experimento sendo realizado dentro de 30min
proximaEtapa = False

arquivo = open('arquivo.txt','w')
saida = ''
while(True):
    tipo = input('\nVocê deseja salvar a saída em um arquivo txt ou csv? ')
    if(tipo=='txt'):
        arquivo = open('arquivo.txt', 'w')
        break
    elif(tipo=='csv'):
        import csv
        arquivo = open('arquivo.csv', 'w', newline='')
        break


while(True):
    # RECEBENDO INFORMAÇÃO SE O ANIMAL ESTÁ HABITUADO (Questão 2 - letra a)
    resposta = input('Informe se o animal está habituado [sim ou não]: ')
    if(resposta[0].lower() == 's'):
        animalHabituado = True
        etapaAproximacao = True
        saida = 'Animal Habituado!'
        print(saida)
        armazenar(arquivo, tipo, saida)

    elif (resposta[0].lower() == 'n'):
        animalHabituado = False
        saida = 'Animal não habituado ainda.\n'
        print(saida)
        armazenar(arquivo, tipo, saida)
    else:
        saida = 'Não entendi sua resposta. Vou considerar que o animal está habituado...\n'
        print(saida)
        armazenar(arquivo, tipo, saida)
        animalHabituado = True
        etapaAproximacao = True
        break
    # FIM DE RECEBENDO INFORMAÇÃO SE O ANIMAL ESTÁ HABITUADO (Questão 2 - letra a)

    # ETAPA DE APROXIMAÇÃO
    if(animalHabituado and etapaAproximacao and tempoValido):
        distanciaEntrada = float(
            input('\nInforme a distância entre o animal e a barra: '))
        if(distanciaEntrada < distanciaEstabelecida):
            saida = 'Distância menor que 30cm.'
            armazenar(arquivo, tipo, saida)
            print(saida)
            saida = 'Animal aproximou. Liberado 0,5ml de rec...\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
            resposta = input('O animal tocou a barra? ')
            if(resposta[0].lower() == 's'):
                toqueBarra += 1
                saida = 'O animal tocou a barra '+str(toqueBarra)+'x.\n'
                print(saida)
                armazenar(arquivo,tipo, saida)
                if(toqueBarra >= 20):
                    etapaAproximacao = False
                    etapaSomToque = True
                    saida = 'Procedimento passou para próxima etapa.\n'
                    print(saida)
                    armazenar(arquivo,tipo, saida)
                    toqueBarra = 0
            else:
                saida = 'O animal se aproximou mas não tocou a barra.\n'
                print(saida)
                armazenar(arquivo, tipo, texto)
        else:
            saida = 'O animal não se aproximou.\n'
            print(saida)
            armazenar(arquivo, tipo, texto)
    # FIM ETAPA DE APROXIMAÇÃO

    # ETAPA DE SOM_E_TOQUE
    if(animalHabituado and not etapaAproximacao and etapaSomToque and tempoValido):
        resposta = input('Para emitir som Phee digite 1, para emitir som Trill digite 2: ')
        if(resposta == '1'):
            som1 = True
            saida = 'Emitindo som Phee...'
            print(saida)
            armazenar(arquivo, tipo, saida)
        elif(resposta == '2'):
            som2 = True
            saida = 'Emitindo som Trill...'
            print(saida)
            armazenar(arquivo, tipo, saida)
        else:
            saida = 'Resposta não identificada, tente novamente.'
            print(saida)
            armazenar(arquivo, tipo, saida)

        if(som1 or som2):
            saida = '\nSe o animal tocou a barra esquerda digite 1.'
            print(saida)
            armazenar(arquivo, tipo, saida)
            saida = 'Se o animal tocou a barra direita digite 2.'
            print(saida)
            armazenar(arquivo, tipo, saida)
            resposta = input('Respostas diferentes indicarão que o animal não tocou a barra: ')
            if(resposta == '1'):
                barraEsquerda = True
            elif(resposta == '2'):
                barraDireita = True
            else:
                barraDireita = False
                barraEsquerda = False

            if(som1 and barraEsquerda):
                toqueBarra += 1
                saida = '\nO animal acertou '+str(toqueBarra)+'x até agora.'
                print(saida)
                armazenar(arquivo, tipo, saida)
                saida = 'Liberado 0,5 de rec.'
                print(saida)
                armazenar(arquivo, tipo, saida)
            elif(som2 and barraDireita):
                toqueBarra += 1
                saida = '\nO animal acertou '+str(toqueBarra)+'x até agora.'
                print(saida)
                armazenar(arquivo, tipo, saida)
                saida = 'Liberado 0,5 de rec.'
                print(saida)
                armazenar(arquivo, tipo, saida)
            else:
                saida = '\nO animal não tocou a barra correspondente.'
                print(saida)
                armazenar(arquivo, tipo, saida)
                saida = 'Não foi liberado nada.'
                print(saida)
                armazenar(arquivo, tipo, saida)
            som1 = False
            som2 = False

        # VERIFICAR SE O PROCEDIMENTO IRÁ PARA PRÓXIMA ETAPA
        resposta = input('\nJá faz 30min que iniciou o experimento [sim ou não]? ')
        if(resposta[0].lower() == 's'):
            tempoValido = False
            saida = '\nNão habilitado a seguir para próxima etapa.'
            print(saida)
            armazenar(arquivo, tipo, saida)
            saida = 'O animal precisa descansar. Repita o experimento em outro momento.\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
        elif(toqueBarra >= 50 and not proximaEtapa):
            saida = '\nEtapa finalizada. Seguir para próxima etapa do experimento.\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
            etapaSomToque = False
            proximaEtapa = True
            break
        else:
            saida = '\nContinue o experimento...\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
        # FIM DA VERIFICAÇÃO SE O PROCEDIMENTO IRÁ PARA PRÓXIMA ETAPA
    # FIM ETAPA DE SOM_E_TOQUE

arquivo.close()


