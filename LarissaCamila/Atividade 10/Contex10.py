
#Importando bibliotecas que serão utilizadas
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

#Importando formatação de texto (Negrito)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Cadastrar pesquisador responsável durante a pesquisa
#Verificar autorização

pesquisador = input("Qual o seu nome: ")
if pesquisador == "Larissa":
    print('Você está autorizado a executar a pesquisa, prossiga.')
    
else:
    print('Você não tem autorização para realizar a pesquisa')

#Criação do menu
print("--------------------------------------------------------------------------------------------------------------------------------------------")
def menu():    
    print('\n0 = Sair\n1 = Seleção do animal\n2 = Cirurgia estereotáxica\n3 = Preparo do tecido\n4 = Marcação\n5 = Microscopia')
    return int(input('\nEntre com a opção desejada: '))


#Estrutura de repetição para sempre retornar ao menu no final de cada etapa
while True:
    opcao = menu()
    
    #Finalizar programa
    if opcao == 0:
        print ('Tchau!')
        break;
    
    #Seleção do animal
    elif opcao == 1:    
        print("\n-----------------SELEÇÃO DO ANIMAL----------------")
        print("\n1 - Rato Wistar")
        print("2 - Camundongo")
        print("3 - Sagui")
        animal = float(input('\nDigite a opção desejada: '))

        if animal == 1:
            print("\nO animal selecionado foi: ", color.BOLD + 'RATO WISTAR' + color.END)
        elif animal == 2:
            print("\nO animal selecionado foi: ", color.BOLD + 'CAMUNDONGO' + color.END)
        elif animal == 3:
            print("\nO animal selecionado foi: ", color.BOLD + 'SAGUI' + color.END)
        else: 
            print("\nInválido")
    
    #Etapa de cirurgia estereotáxica
    elif opcao == 2:
        print("-----------------CIRURGIA ESTEREOTÁXICA----------------")

        anestesico = ["Xilazina", "Ketamina", "Isoflurano"]
        dosagem = ("Xilazina - 5 a 10 mg/kg","Ketamina - 50 a 90 mg/kg", "Isoflurano - 3 a 4%")
        via = ["Xilazina - intraperitoneal", "Ketamina - intraperitoneal", "Isoflurano - Inalatória"]

        pesoanimal = float(input("Qual o peso (g) do animal utilizado? "))
        print(pesoanimal)

        print("Anestésicos disponíveis: ", anestesico)
        anestesicousado = input("Qual anestésico será utilizado?\n")

        print("Dosagens recomendadas: ", dosagem)
        dosagemusada = float(input("Qual dosagem será utilizada? "))

        print("Vias de administração recomendadas: ", via)
        viaadministrada = input("Qual a via de administração? ")
        print("-------------------------------------------------------------------")
        print("\nO anestésico selecionado foi : ", anestesicousado)
        print("A dosagem selecionada foi: ", dosagemusada)
        print("A via de administração selecionada foi: ", viaadministrada)
        print("-------------------------------------------------------------------")

        print(color.BOLD + '\nPOSICIONAMENTO NO ESTEREOTÁXICO' + color.END)

        print("\nO animal deverá ser posicionado de modo que as barras sejam posicionadas no ouvido externo")
        print("Verificar posicionamento do animal no minímo 3 x")

        posicionado = 0
        for posicionado in range (3):
            posicionamento = int(input("O animal foi posicionado no estereotáxico corretamente? 0 (Não) - 1 (Sim): "))

        if posicionamento == 0:
            print("O animal não foi posicionado corretamente.")
        elif posicionamento == 1:
            print("\nO animal foi posicionado corretamente sem diferenças na angulação entre o bregma e o lambda.")
        else: 
            print("Inválido")
        print("----------------------------------------------------------------------")

        print(color.BOLD + '\nCOORDENADAS PARA IMPLANTE DA MATRIZ DE ELETRODOS' + color.END)
        print("\nInforme as coordenadas a serem utilizadas")

        AP = float(input("Digite o valor do posicionamento AnteroPosterior (AP): " ))
        LL = float(input("Digite o valor do posicionamento LateroLateral (LL): " ))
        DV = float(input("Digite o valor do posicionamento DorsoVentral (DV): " ))
        print("--------------------------------------------------------------------")
        print("\nO valor digitado foi (AP): ", AP)
        print("O valor digitado foi (LL): ", LL)
        print("O valor digitado foi (DV): ", DV)
        print("--------------------------------------------------------------------")
    
    #Processamento tecidual
    elif opcao == 3:
        print("------------------------------------------------------")
        print("\nDescreva as etapas do processamento tecidual.")
        perfusao = input("Qual o método de perfusão será utilizado: ")
        eutanasia = input("Qual o método de eutanásia será utilizado: ")

        print("------------------------------------------------------")
        print("Soluções a serem utilizadas durante a perfusão: \n-Salina heparinizada \n-Paraformaldeído")
        print("------------------------------------------------------")
        print("Soluções em que o cérebro deverá ser mantido: \n-Paraformaldeído tamponado (24 Horas) \n-Tampão fosfato (24 Horas) \n-Sacarose tamponada")
        print("------------------------------------------------------")

    #Etapa de Imuno
    elif opcao == 4:
        print("------------------------------------------------------")
        print("\nDescreva os procedimentos que serão realizados.")
        print("\n1 - Coloração de Nissl \n2 - Imunofluorescência \n3 - Outra")
        imuno = int(input("Qual o método a ser realizado? "))
        if imuno == 1:
            print("Você selecionou a coloração de Nissl que será utilizada para confirmar as regiões que foram atingidas pelo implante, a seguir estão as etapas que deverão ser realizadas.")
            print("------------------------------------------")
            print("ETAPAS: \n1º Colocar lâminas em cresil violeta \n2º Imersão em solução de ácido acético \n3º Imersão em baterias de álcoois 70, 80, 90 e 100% \n4º Imersão em baterias de xilol puro \n5º Fechamento das lâminas")
            print("------------------------------------------")
        elif imuno == 2:
            print("Você selecionou a imunofluorescência, onde as etapas serão mostradas a seguir.")
            print("------------------------------------------")
            print("ETAPAS: \n1º Reidratação dos tecidos em tampão fosfato \n2º Bloqueio de sítios inespecíficos \n3º Repetir procedimento de lavagem e hidratação, permanecendo em incubação OVERNIGHT com anticorpos primários: Iba1, CD68. \n4º Lavagem e será acrescido os anticorpos secundários: anti-rabbit e anti-mouse conjugados aos fluoróforos \n5º Lavagem dos tecidos e montagem de lâminas com ProLong Gold Antifade Mountant com DAPI.")
            print("------------------------------------------")
        else:
            print("Inválido")
    
    #Etapa de análise microscópica e quantitativa
    elif opcao == 5:
        print("------------------------MICROSCOPIA------------------------------")
        print("Discrimine qual a celula será analisada!")
        print("\n1 - Micróglia \n2 - Astrócitos")
        mic = int(input("Selecione a opção desejada:  "))
        if mic == 1:
            print("Você selecionou micróglia.")
            print("Estes são os seus resultados em relação a porcentagem de células ativas e inativas. ")
            microglia = pd.read_csv(r"C:/Users/ACER/Desktop/Arquivos-Quali/Microgliareal.csv")
            A = microglia['Microglias ativas']
            I = microglia['Microglias inativas']
            print("------------------------------------------")
            labels = 'Ativas', 'Inativas'
            sizes = [sum(A), sum(I)]
            explode = (0, 0.1)

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()

            print("------------------------------------------")
        elif mic == 2:
            print("Você selecionou astrócito.")
            print("------------------------------------------")
            print("Não possuimos dados referentes a quantidade de astrócitos.")
            print("------------------------------------------")
        else:
            print("Inválido")