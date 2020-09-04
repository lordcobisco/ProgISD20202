#Inicialmente vamos verificar se o anomal está anestesiado

anestesiado = input("O animal está anestesiado? Para responder 'Sim' digite 1, para 'Não' digite 0 ")

if(anestesiado):
    ("Agora vamos posicionar o animal no estereotáxico ")

    piscada = int(input("O animal piscou? 1 para Sim e 0 para Não "))


    while(piscada != 1):
        piscada = int(input("O animal piscou? 1 para Sim e 0 para Não "))
    
    print("Vamos verificar se a superfície está plana. Para isso o ângulo do bregma e lamba precisam ser iguais.")
    bregma = float(input("Qual a angulação do bregma? "))
    lambdah = float(input("Qual a angulação do lambda? "))
    
    if(bregma == lambdah):
        print("Agora vamos realizar a limpeza do campo cirúrgico. Para isso, comece retirando a pelagem do animal")
        pelagem = int(input("A pelagem do animal foi removida?"))

        while(pelagem != 1):
            pelagem = int(input("A pelagem do animal foi removida?"))

        print("Agora retire os tecidos moles")
        tecidos = int(input("Os tecidos do animal foram removidos?"))

        while(tecidos != 1):
            tecidos = int(input("Os tecidos do animal foram removidos?"))

        print("Limpe a região com H2O2")
        limpeza = int(input("A região foi limpa?"))
        while(limpeza != 1):
            limpeza = int(input("Os tecidos do animal foram removidos?"))

        print("Passe acrilato na região para evitar sangramentos")
        acrilato = int(input("Você passou o acrilato?"))
        while(acrilato != 1):
            acrilato = int(input("Você passou o acrilato?"))

        print("Agora com todas essas etapas cumpridas, vamos posicionar escolher um ponto para fixação dos parafusos")

        #usando valores do hipocampo, conforme atividade contextualizada 
        AP = float(input("Digite o valor marcado na régua do estereotáxico para o posicionamento Antero Posterior "))
        LL = float(input("Digite o valor marcado na régua do estereotáxico para o posicionamento Latero Lateral "))
        DV = float(input("Digite o valor marcado na régua do estereotáxico para o posicionamento Dorso Ventral "))

        tupla_referencia = [-0.42, -0.3,  0.3, -0.2] #optei pela tupla, pois esses valores são fixos

        posicoes = [AP + tupla_referencia[0], LL + tupla_referencia[1],  LL + tupla_referencia[2], DV + tupla_referencia[3]]
        
        hemisferio = input("Em qual dos hemisférios você colocará a primeira cânula?")
        print("Você deverá localizar os pontos de inserção conforme a indicação a seguir: ")
        print("AP", posicoes[0])
        print("LL", posicoes[1], " ", posicoes[2])
        print("DV", posicoes[3])

        print("Para que a perfuração seja feita, busque deixar a mão apoiada ao assoalho e mantenha a inclinação de 45o")

        angulacao = float(input("Qual inclinação está a sua mão?"))

        if(angulacao > 0 and angulacao < 40):
            print("A angulacão está abaixo do ideal")
        elif(angulacao >= 40 and angulacao <= 50):
            print("Ótimo, continue as perfurações")
        else:
            print("A angulacão está acima do ideal")
        
        print("Agora que a perfuração foi feita, insira a  cânula-guia até ", posicoes[3])

        sangue = int(input("Está saindo sangue ou cefalorraquidiano?"))

        if(sangue):
            print("Utilize rolos de papel absorvente para limpar")

        print("Agora que os parafusos já estão inseridos, é hora de confeccionar o capacete que dará suporte à estrutura\n misture o acrílico com solvente até obter uma textura suficiente para nao escorrer pelo crânio\n do animal")

        textura = int(input("Chegou na textura desejada?"))

        while(textura != 1):
            print("Continue misturando")
            textura = int(input("E agora, chegou na textura desejada?"))   

        print("Agora aplique a mistura na região com cuidado para que não escorra. Abarque o crânio, a cânula-guia e o parafuso.")

        #adaptei o tempo de secagem para o tipo de solvente e nao temperatura e umidade da sala
        tempos_solventes = {'solventeA':10,  'solventeB':20,  'solventeC':30, 'solventeD':40}

        tipo_solvente = input("Qual o tipo de solvente que está sendo usado? Responda entre solventeA, solventeB, solventeC ou solventeD   ")

        tempo_secagem = int(input("Há quanto tempo a resina foi aplicada? "))

        while(tempo_secagem<tempos_solventes[tipo_solvente]):
            print("Aguarde mais um pouco")
            tempo_secagem = int(input("Há quanto tempo a resina foi aplicada? "))
        else:
            print("Podemos seguir a diante")
        
        print("Agora iremos fixar a outra cânula. Levante o braço do esteriotaxico com cuidado, sem movimentar a cânula ja colocada.\n Posicione a cãnula na região ja estabelecida e introduza-a até ", posicoes[3])

        sangue = int(input("Está saindo sangue ou cefalorraquidiano?"))

        if(sangue):
            print("Utilize rolos de papel absorvente para limpar")

        print("Agora que já inseriu a cânula, é hora de espalhar um pouco mais do cimento criado do produto entre o solvente e acrilato")

        textura = int(input("Chegou na textura desejada?"))

        while(textura != 1):
            print("Continue misturando")
            textura = int(input("E agora, chegou na textura desejada?"))   

        print("Agora aplique a mistura na região com cuidado para que não escorra. Abarque o crânio, a cânula-guia e o parafuso.")
        
        tempo_secagem = int(input("Há quanto tempo a resina foi aplicada? "))

        if(tempo_secagem<tempos_solventes[tipo_solvente]):
            print("Aguarde mais um pouco")
        else:
            print("Agora chegamos na última etapa")

        print("Remova os braços do estereotáxico lentamente")

        print("Levante o animal cuidadosamente e coloque-o em uma caixa aquecida")
        
        outros_animais = int(input("Os outros animais estão acordados?"))






        
        