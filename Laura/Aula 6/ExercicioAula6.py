#Método de discriminação de estímulos auditivos para primatas através do condicionamento operante (atualização)

#Habituação
habituado = int(input("O animal está habituado? (Responda 0 para não e 1 para sim) "))
if(habituado):
    print("O animal está habituado, pode iniciar o experimento.\n")
else: 
    print("O animal não está habituado. Ele precisará acertar 70% do total de tentativas para a atividade. Continue até atingir esta marca para que o animal esteja habituado e então inicie o experimento.\n")

#Regime de aproximações sucessivas
aproximacaosus=30
aproximacao = float(input("O animal andou quantos cm? "))
if(0 != aproximacao < 30):
    print("O animal aproximou, logo, liberar 0,5ml de recompensa.\n")
else:
    print("Não liberar recompensa, pois o animal não aproximou.\n")

#Tocar na barra
print("Abaixo, verificaremos se o experimento poderá passar para a próxima fase.")
contador = 0
tocarBarra = int(input("O animal tocou na barra? (Responda 0 para não e 1 para sim) "))
while (contador <=20):
    tocarBarra = int(input("O animal tocou na barra? (Responda 0 para não e 1 para sim) "))
    if(tocarBarra):
        contador = contador+1
    print("Como o animal tocou na barra 20 vezes, o experimento passou para a próxima etapa.\n")

#Tocar na barra esquerda ou direita conforme o som emitido
print("Para esta etapa será acionado 50 vezes o som, do tipo 1 ou 2, esperando-se que o animal toque na barra correta.")

contador2=0
while (contador2 <= 50):
    som = int(input("Qual o som foi emitido? (Digite 1 para som1 e 2 para som2) "))
    barra = int(input("Qual a barra que foi tocada pelo animal? (Digite 1 se tocou na barra esquerda e 2 se tocou na direita)  "))
    if(som==1 and barra==1):
        print("Liberar 0,5ml de recompensa")
    elif(som==2 and barra==2):
        print("Liberar 0,5ml de recompensa")
    else:
        print("Como o animal não executou a tarefa esperada, não liberar a recompensa")

contador2 = contador2+1

#Verificar se o experimento foi realizado 50x em 30min
tempo=30
qntdExperimento=50

experimento=int(input("Quantas vezes o experimento foi realizado? "))
tempo2=int(input("Em quanto tempo, em minutos, o experimento foi realizado? "))

if(experimento==qntdExperimento and tempo2<=tempo):
    print("Seguir para a próxima fase.")
else:
    print("O experimento não poderá seguir para a próxima fase, pois não foi executado 50 vezes em até 30 minutos.")

