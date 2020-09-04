#Aluno João Vitor da Silva Neto

animal_habituado = False

print("O sagui está habituado? ", animal_habituado)
while(not animal_habituado):
    animal_habituado = bool(input("\nQuando o animal estiver habituado, entre com algum caractere.\n"))
    
    if (animal_habituado):
        print('Passar para o proximo experimento.')
    else:
        print('Aguarde o animal se habituar.')


distancia = 30
print('Experimento 1 (Aproximação):') 
while (distancia > 0):

    print('O sagui se encontra a ', distancia, 'cm da barra. Caso ele se aproxime, será liberado 0,5ml de recompensa.')
    distancia = int(input("O sagui se moveu quantos cm? Caso tenha se afastado, insira um número positivo, caso tenha se aproximado, insira um número negativo.\n")) + distancia
    if (distancia == 0):
        print("Sucesso! Liberado 0.5ml de recompensa. E o experimento passou para a proxima fase.\n")
    else:
        print("Não foi liberada recompensa\n")

toques = 0
print("Experimento 2 (Toque simples na barra): O sagui deve tocar na barra 20x.\n")
sensor_barra = False

while (toques < 20):
    sensor_barra = bool(input("Repeticao " + str(toques) +" de 20. Se o sagui tocou na barra, insira qualquer caractere. Caso contrário, apenas pressione enter.\n"))
    if (sensor_barra):
        toques = toques+1
        print("Sucesso! Liberado 0.5ml de recompensa.\n")
        sensor_barra = False
    else:
        print("O sagui não tocou na barra dessa vez")

    if (toques == 20):
        print('O animal repetiu a logica 20x, e o experimento passou para a proxima fase.\n')

toques = 0
som = 'n'
barra = 'n'
tempo = False

while ((tempo == False) and (toques < 50)):
    print("Repetição "+ str(toques) + " de 50\n")
    tempo = bool(input("Insira qualquer caractere para informar o fim dos 30 minutos, ou não insira nenhum caractere caso o tempo não tenha expirado.\n"))

    if (tempo == True):
        print('O tempo se esgotou.')
        break

    else:
        som = str(input("Qual som foi tocado? Digite 1 para som1 e 2 para som2.\n"))
        barra = str(input("Qual barra foi tocada? Digite e para esquerda, e d para direita.\n"))

        if ((som == '1' and barra == 'e') or (som == '2' and barra == 'd')):
            print("Sucesso! Liberado 0.5ml de recompensa.\n")
            toques = toques+1

        else:
            print("O sagui não seguiu a lógica dessa vez")

print('\nFim do experimento.')