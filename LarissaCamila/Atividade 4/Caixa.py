habituado = 0
habituacao = int(input("O animal foi habituado? 0 (Não) - 1 (Sim): "))

if habituacao == 0:
    print("O animal não passou por sessões de habituação.")
elif habituacao == 1:
    print("O animal foi habituado.")
    habituado = 1
else: 
    print("Inválido")

aproximado = 0
if habituado == 1:
    aproximacao = 30
    sagui = float(input("Qual a distância de aproximação do animal (cm)? "))
    
    if sagui > 0 and sagui <= aproximacao:
        print("0,5 ml de recompensa liberada")
        aproximado = 1
    elif sagui == 0:
        print("Nenhuma recompensa foi liberada")
    else:
        print("Inválido.")

tocado = 0
if aproximado == 1: 
    toque = int(input("O sagui realizou o toque na barra por 20x ? 0 (Não) - 1 (Sim): "))
    if toque == 0:
        print("O animal não pode prosseguir para a próxima etapa.")
    elif toque == 1:
        print("O animal pode prosseguir para a próxima etapa")
        tocado = 1 
    else: 
        print("Inválido.")


sonoro = 0
if  tocado == 1: 
        print("Parabéns, você chegou na penúltima etapa!")
        print("Estas são suas opções: ")
        print("1- Phi")
        print("2- Trill")
        print("3-Esquerda")
        print("4-Direita")
        som = int(input("Qual o som que foi tocado: "))
        barra = int(input("O animal tocou em qual barra: "))
        if som == 1 and barra == 3:
            print("O animal foi recompensado!")
            sonoro = 1
        elif som == 2 and barra == 4:
            print("O animal foi recompensado")
            sonoro = 1
        else:
            print("Repetir teste.")


tempo = 0
if sonoro == 1:
    xtempmin = int(input("O experimento foi realizado 50 vezes em uma duração de 30 minutos? 0 (Não) - 1 (Sim)"))
    if xtempmin == 0:
        print("Continuar a realizar o experimento")
    elif xtempmin == 1:
        print("O experimento pode prosseguir para a próxima fase.")
    else: 
        print("Inválido.")