#Atividade 08 - Atualização da caixa comportamental para realizar a saída de arquivos csv e txt

def armazenar(arquivo, tipo, texto):
    if(tipo == 'txt'):
        arquivo.write(texto)
    elif(tipo == 'csv'):
        arquivowriter = csv.writer(arquivo, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        arquivowriter.writerow(texto)
'''
arquivo = open('arquivo.txt', 'w')
saida=''
'''
while(True):
    tipo = input('Qual o tipo do arquivo que você deseja salvar o experimento? txt ou csv?\n')
    if(tipo=='txt'):
        arquivo = open('arquivo.txt', 'w')
        break
    elif(tipo=='csv'):
        import csv
        arquivo = open('arquivo.csv','w')
        break

saida = '<<Programa para treinamento de saguis>>\n\n1ª Etapa: Habituação do animal na caixa.'
print(saida)
armazenar(arquivo, tipo, saida)

habituado = str(input('O animal está habituado? "s" para SIM e "n" para NÃO.\n'))
if (habituado == "s"):
    saida = '\nVamos iniciar o treinamento!'
    print(saida)
    armazenar(arquivo, tipo, saida)
    print('')
    distancia=30
    for i in range(20):
        distancia1=float(input("Qual a distância que o sagui está da barra?\n"))
        if (distancia1 < distancia):
            saida = '\nLiberar 0,5ml de rec.'
            print(saida)
            armazenar(arquivo, tipo, saida)
        else:
            saida = '\nNão liberar nada' 
            print(saida)
            armazenar(arquivo, tipo, saida)
    
    saida = '\nVamos para a próxima fase.'
    print(saida)
    armazenar(arquivo, tipo, saida)
    for i in range(50):
        som1 = str(input('Som 1 foi tocado e o animal tocou a barra da esquerda? "s" para SIM e "n" para NÃO.\n'))
        som2 = str(input('Som 2 foi tocado e o animal tocou a barra da direita? "s" para SIM e "n" para NÃO.\n'))
        if (som1 == "s" and som2 == "s"):
            saida= '\nSom 1: Liberar 0,5ml de rec.\nSom 2: Liberar 0,5ml de rec.\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
        elif (som1 == "n" and som2 =="s"):
            saida = '\nSom 1: Não liberar nada.\nSom 2: Liberar 0,5ml de rec.\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
        elif (som1 == "s" and som2 == "n"):
            saida = '\nSom 1: Liberar 0,5ml de rec.\nSom 2: Não liberar nada.\n'
            print(saida)
            armazenar(arquivo, tipo, saida)
        else:
            saida = '\nNão liberar nada\n'
            print(saida)
            armazenar(arquivo, tipo, saida)

    tempo=float(input('Por favor, digite o tempo utilizado no treinamento em minutos:\n'))
    if (tempo > 30):
        saida = '\nO experimento excedeu os 30 minutos, logo não será considerado. Por favor, realize novamente o experimento após o animal descansar no mínimo 4 horas.\n'
        print(saida)
        armazenar(arquivo, tipo, saida)
    else:
        saida = '\nO expermento foi realizado com sucesso e seguirá para a próxima fase.\n'
        print(saida)
        armazenar(arquivo, tipo, saida)

    saida = '\nFim do treinamento\n'
    print(saida)
    armazenar(arquivo, tipo, saida)

else:
    saida='\nAbra novamente o programa quando o animal estiver melhor habituado.\n'
    print(saida)
    armazenar(arquivo, tipo, saida)
    
arquivo.close()