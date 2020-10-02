#Exercício da Aula 07 - Atualização da caixa comportamental v3.0

def treino():
    for i in range(50):
        som1 = str(input('Som 1 foi tocado e o animal tocou a barra da esquerda? "s" para SIM e "n" para NÃO.\n'))
        som2 = str(input('Som 2 foi tocado e o animal tocou a barra da direita? "s" para SIM e "n" para NÃO.\n'))
        if (som1 == "s" and som2 == "s"):
            print('Som 1: Liberar 0,5ml de rec.')
            print('Som 2: Liberar 0,5ml de rec.')
        elif (som1 == "n" and som2 =="s"):
            print('Som 1: Não liberar nada.')
            print('Som 2: Liberar 0,5ml de rec.')
        elif (som1 == "s" and som2 == "n"):
            print('Som 1: Liberar 0,5ml de rec.')
            print('Som 2: Não liberar nada.')
        else:
            print('Não liberar nada')
    return print("Fim do treinamento")

def habituar():
    distancia=30
    for i in range(20):
        distancia1=float(input("Qual a distância que o sagui está da barra?\n"))
        if (distancia1 < distancia):
            print("Liberar 0,5ml de rec.")
        else: 
            print("Não liberar nada")
    return print('\nFim da habituação do animal. \nVamos para a próxima fase!')

def temp():
    tempo=float(input('Por favor, digite o tempo utilizado no treinamento em minutos:\n'))
    if (tempo > 30):
        print('O experimento excedeu os 30 minutos, logo não será considerado. Por favor, realize novamente o experimento após o animal descansar no mínimo 4 horas.')
    else:
        print('O expermento foi realizado com sucesso e seguirá para a próxima fase.')
    return print('Fim do treinamento.')

def saguis():
    print('<<Programa para treinamento de saguis>>')
    print('')
    print('1ª Etapa: Habituação do animal na caixa.')
    habituado = str(input('O animal está habituado? "s" para SIM e "n" para NÃO.\n'))
    if (habituado == "s"):
        print("Vamos iniciar o treinamento!")
        print('')
    
        habituar()

        treino()

        temp()
    else:
        print('Abra novamente o programa quando o animal estiver melhor habituado.')

saguis()