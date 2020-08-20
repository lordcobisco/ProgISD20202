'''
listaNomes=['Andre', 'Felipe', 'Oliveira']

for nome in listaNomes:
    print(nome)
else:
    print('Todos os nomes foram escritos com sucesso!')
#enumerate enumera a lista
for key,value in enumerate(['p', 'y', 't', 'h', 'o', 'n']):
    print(key, value)

for i in range(9,-2,-1):
    print(i)

linguagens= ['Python', 'PHP', 'C#', 'Cobol', 'C++']
tam = len(linguagens)
indices= range(tam)
for item in indices:
    print(linguagens[item])

lista1 = ['bacon', 'fritas', 'picanha']
lista2 = ['cerveja', 'refri', 'suco']

#zip junta duas listas
#for alimento,bebida in zip(lista1,lista2):
#    print(alimento, bebida)

for alimento in lista1:
    for bebida in lista2:
        print(alimento, bebida)

cont=0
#while cont <5:
#    print(cont)
#    cont= cont + 1

while cont < 100:
    cont = int(input("Digite um numero"))
else:
    print('o numero digitado não está na faixa pedida')

#break encerra o loop na linha do break
#continue encerra o loop ao final da iteração
tocou= 0
contador=0
for contador in range(100):
    tocou= int(input('O animal tocou na barra?'))
    if(tocou):
        break
    mostrar= int(input("Deseja mostrar contador?"))
    if(not mostrar):
        continue
    print(contador)

'''
#Exercício de aula melhoria do algoritmo da caixa operante

habituado = int(input("O rato está habituado? (Digite 1 para sim, 0 para não)"))
if (habituado==1):
    print("O animal está habituado. Pode iniciar o experimento")
    dist =30
    aprox = int(input("Quantos cm o animal se aproximou?"))
    distrest= dist- aprox
    if (distrest < 30):
        print("Liberar 0.5ml de recompensa")

    ####################REGIME DE APROXIMAÇÕES SUCESSIVAS######################################
    contador = 0
    toque=int(input("Animal tocou na barra?"))
    while (contador <= 20):
        toque=int(input("Animal tocou na barra?"))
        if(toque):
            contador= contador +1
    print("O experimento passou para próxima etapa") 
    
    #################### TREINAMENTO ######################################
    while (cont <50):
        som= int(input("Qual som foi emitido(1 ou 2)?"))
        barra= int(input("Qual barra foi acionada(1, para esquerda ou 2, para direita)?"))
        if (som==1 and barra==1):
            print("Liberar 0.5ml de recompensa")
        elif(som==2 and barra==2):
            print("Liberar 0.5ml de recompensa")
        else:
            print("Não liberar recompensa!")
        cont= cont+1

    tempo= int(input("Qual o tempo de duração do experimento?"))

    if(tempo <=30):
        print("O experimento seguirá para a próxima fase")

else:
    print("O animal não está habituado. O experimento não pode ser realizado")
    