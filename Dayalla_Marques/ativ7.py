import time

# DISPOSITIVO 1
def dispositivoA(rA, gA, bA):
    return rA, gA, bA
    

listaRed = list()
listaGreen = list()
listaBlue = list()

contadorA=0
while contadorA<32:
    pass
    
    sairdoExperimento1 = 0 # o nome dessa variável não significa que é o experimento 1, é apenas um nome aleatório
    while not sairdoExperimento1:
        sairdoExperimento1 = int(input(" Você deseja sair do experimento? Digite 1 pra continuar \n"))
       
           
    else: 
        
        
        rA = int(input("Dispositivo 1. Digite valores para R: \n"))
        listaRed.append(rA)
        if rA<5: print("Led vermelho, intensidade baixa \n")
        if rA==5: print("Led vermelho, intensidade média \n")
        if rA>5: print("Led vermelho, intensidade alta \n")
        x = int(input("Pr quanto tempo você quer que esse Led fique aceso?"))
        time.sleep(x)

    sairdoExperimento2 = 0 # o nome dessa variável não significa que é o experimento 2, é apenas um nome aleatório
    while not sairdoExperimento2:
        sairdoExperimento2 = int(input("Você deseja sair do experimento? Digite 1 pra continuar\n"))
        
    else: 
        gA = int(input("Dispositivo 1. Digite valores para G: \n"))
        listaGreen.append(gA)
    if gA<5: print("Led verde, intensidade baixa \n")
    if gA==5: print("Led verde, intensidade média \n")
    if gA>5: print("Led verde, intensidade alta \n")
    y = int(input("Pr quanto tempo você quer que esse Led fique aceso?"))
    time.sleep(y)

    sairdoExperimento3 = 0 # o nome dessa variável não significa que é o experimento 3, é apenas um nome aleatório
    while not sairdoExperimento3:
        sairdoExperimento3 = int(input("Você deseja sair do experimento? Digite 1 pra continuar: \n"))
        

    else: 

        bA = int(input("Dispositivo 1. Digite valores para B: \n"))
        listaBlue.append(bA)
    if bA<5: print("Led azul, intensidade baixa \n")
    if bA==5: print("Led azul, intensidade média \n")
    if bA>5: print("Led azul, intensidade alta \n")
    z = int(input("Pr quanto tempo você quer que esse Led fique aceso?"))
    time.sleep(z)

    print(dispositivoA(rA,gA,bA))
    
    contadorA = contadorA + 1


        
else:
    pass
    print("Pronto \n")

print(" Lista de R: \n")
print(listaRed)
print(" Lista de G: \n")
print(listaGreen)
print(" Lista de B: \n")
print(listaBlue)




# DISPOSITIVO 2

def dispositivoB(rB, gB, bB,):
    return rB, gB, bB

listaRedB = list()
listaGreenB = list()
listaBlueB = list()
    
contadorB=0
while contadorB<32:
    pass

    sairdoExperimento4 = 0 # o nome dessa variável não significa que é o experimento 4, é apenas um nome aleatório
    while not sairdoExperimento4:
        sairdoExperimento4 = int(input(" Você deseja sair do experimento? Digite 1 pra continuar \n"))
        
         
    else: 
    
        rB = int(input("Dispositivo 2. Digite valores para R: \n"))
        listaRed.append(rB)
    if rB<5: print("Led vermelho, intensidade baixa \n")
    if rB==5: print("Led vermelho, intensidade média \n")
    if rB>5: print("Led vermelho, intensidade alta \n")
    w = int(input("Pr quanto tempo você quer que esse Led fique aceso?"))
    time.sleep(w)

    sairdoExperimento5 = 0 # o nome dessa variável não significa que é o experimento 5, é apenas um nome aleatório
    while not sairdoExperimento5:
        sairdoExperimento5 = int(input("Você deseja sair do experimento? Digite 1 pra continuar\n"))
        
    else: 
        gB = int(input("Dispositivo 1. Digite valores para G: \n"))
        listaGreen.append(gB)

    if gB<5: print("Led verde, intensidade baixa \n")
    if gB==5: print("Led verde, intensidade média \n")
    if gB>5: print("Led verde, intensidade alta \n")
    t = int(input("Pr quanto tempo você quer que esse Led fique aceso?"))
    time.sleep(t)

    sairdoExperimento6 = 0 # o nome dessa variável não significa que é o experimento 6, é apenas um nome aleatório
    while not sairdoExperimento6:
        sairdoExperimento6 = int(input("Você deseja sair do experimento? Digite 1 pra continuar\n"))
        

    else: 

        bB = int(input("Dispositivo 1. Digite valores para B: \n"))
        listaBlue.append(bB)
    if bB<5: print(" Led azul, intensidade baixa \n")
    if bB==5: print(" Led azul, intensidade média \n")
    if bB>5: print(" Led azul, intensidade alta \n")
    m = int(input("Pr quanto tempo você quer que esse Led fique aceso?"))
    time.sleep(m)

    print(dispositivoB(rB,gB,bB))

    contadorB = contadorB + 1
    

else:
    pass
    print("\n Pronto \n")

print("\n Lista de R: \n")
print(listaRedB)
print("\n Lista de G: \n")
print(listaGreenB)
print("\n Lista de B: \n")
print(listaBlueB)

# PARA O DISPOSITIVO 1:

listaExperimento = list()
listatempodeinicio = list()
listatempodeexperimento = list()
listaexperimentos = list()
listadataExperimentos = list()
i = 0
numero = int(input("\n Quantidade de experimentos: \n"))
while i < numero:
    print("experimento ",i+1)
    tempodeinicio = int(input("\n Informe o tempo de início do experimento: \n"))
    listatempodeinicio.append(tempodeinicio)
    dataexperimentos = input("\n Digite a data: \n")
    listadataExperimentos.append(dataexperimentos)
    #print(listatempodeinicio)
    
    i+=1
    
else:
    print('\n ok \n')

print(listatempodeinicio)
print(listadataExperimentos)


# PARA O DISPOSITIVO 2:
        

listaExperimentoB = list()
listatempodeinicioB = list()
listatempodeexperimentoB = list()
experimentoB = list()
listadataExperimentosB = list()
n = 0
numeroB = int(input("\n Quantidade de experimentos: \n"))
while n < numeroB:
    print("experimento ",n+1)
    tempodeinicioB = int(input("Informe o tempo de início do experimento:\n"))
    listatempodeinicioB.append(tempodeinicioB)
    dataexperimentosB = input("Digite a data: \n")
    listadataExperimentosB.append(dataexperimentosB)
    #print(listatempodeinicio)
    
    n+=1
    
else:
    print('\n ok \n')

print(listatempodeinicioB)
print(listadataExperimentosB)

# COMPARAÇÃO ENTRE OS DOIS DISPOSITIVOS

if dataexperimentos == dataexperimentosB:
    
    if listatempodeinicio == listatempodeinicioB:

        print("os dispositivos estão alinhados temporalmente \n")
    else: print("os dispositivos não estão alinhados temporalmente \n")
else: print("os dispositivos não estão alinhados temporalmente \n")





# FIM DO PROGRAMA