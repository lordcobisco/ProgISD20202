import csv

filecsv= open('caixa.csv', 'w')
def menu():    
    print('\n0 = Sair\n1 = Habituação\n2 = Aproximação\n3 = Toque na barra\n4 = Estimulo auditivo\n5 = Tempo de experimento')
    return int(input('\nEntre com a opção desejada: '))


while True:
    opcao = menu()
    
    if opcao == 0:
        print ('Tchau!')
        break;
    
    elif opcao == 1:    
        print("\n-----------------HABITUAÇÃO----------------")
        habituado = 0
        habituacao = int(input("O animal foi habituado? 0 (Não) - 1 (Sim): "))

        if habituacao == 0:
            filecsv.write("O animal não passou por sessões de habituação.")
        elif habituacao == 1:
            filecsv.write("O animal foi habituado.")
        habituado = 1
    
    elif opcao == 2:    
        aproximado = 0
        for aproximado in range (10):
            aproximacao = 30
            sagui = float(input("Qual a distância de aproximação do animal (cm)? "))
    
            if sagui > 0 and sagui <= aproximacao:
                filecsv.write("0,5 ml de recompensa liberada")
                aproximado = 1
                break
            elif sagui == 0:
                filecsv.write("Nenhuma recompensa foi liberada")
            else:
                print("Inválido.")

    elif opcao == 3:  
        tocado = 0
        if aproximado == 1: 
            toque = int(input("O sagui realizou o toque na barra por 20x ? 0 (Não) - 1 (Sim): "))
        while toque == 0:
            filecsv.write("O animal não pode prosseguir para a próxima etapa.")
        if toque == 1:
            filecsv.write("O animal pode prosseguir para a próxima etapa")
        tocado = 1 

    elif opcao == 4:  
        sonoro = 0
        if tocado == 1: 
            print("Parabéns, você chegou na penúltima etapa!")
            print("Estas são suas opções: ")
            print("1- Phi")
            print("2- Trill")
            print("3-Esquerda")
            print("4-Direita")
            som = int(input("Qual o som que foi tocado: "))
            barra = int(input("O animal tocou em qual barra: "))
            while som == 1 and barra == 3:
                print("O animal foi recompensado!")
            sonoro = 1
            if som == 2 and barra == 4:
                print("O animal foi recompensado")
            sonoro = 1

    elif opcao == 5:  
        tempo = 0
        if sonoro == 1:
            xtempmin = int(input("O experimento foi realizado 50 vezes em uma duração de 30 minutos? 0 (Não) - 1 (Sim)"))
        while xtempmin == 0:
            filecsv.write("Continuar a realizar o experimento")
        if xtempmin == 1:
            filecsv.write("O experimento pode prosseguir para a próxima fase.")
        else: 
            print("Inválido.")
filecsv.close()