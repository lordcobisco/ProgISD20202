import csv
def contador(n):
    n = int(n)
    n += 1
    return n

print('Seja bem vindo ao treinamento de sagui')
salvar = input("Como deseja salvar os dados?")

if salvar == 'csv':
    with open('Opto.csv',  'w', newline = '') as csvfile:
        wr = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting =  csv.QUOTE_MINIMAL)

        #Animal habituado
        var1 = (input('O animal está habituado? Responda "s" para sim ou "n" para não \n' ))
        if var1 == "s":
            resposta1 = var1  

            distancia = 30
            x = 0
            contador1=0

            dist_usuario = float(input('Qual a distância do animal? \n'))

            if dist_usuario < distancia:
                print ("Liberar 0.5ml de recompensa") 
                wr.writerows(["Liberar 0.5ml de recompensa"])

            while (x <20):
                tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
                if tocar_barra == "s":
                    x = contador(x)
                    

            print ( "O experimento passou de etapa")
            wr.writerows(["O experimento passou de etapa"])
                

            barra_esquerda = input("O animal tocou a barra esquerda? (Responda n para não e s para sim) \n ")
            barra_direita = input("O animal tocou a barra direita? (Responda n para não e s para sim) \n ")
            som1 = input("O som1 foi tocado quando tocou a barra esquerda? (Responda n para não e s para sim) \n ")
            som2 = input("O som2 foi tocado quando tocou a barra direita? (Responda n para não e s para sim) \n ")


            if som1 == "s" and barra_esquerda == "s":
                print ("Liberar 0.5ml de recompensa") 
                wr.writerows(["Liberar 0.5ml de recompensa"])
            else:
                print ("Não liberar recompensa")
                wr.writerows(["Não liberar recompensa"])

            if som2 == "s" and barra_direita == "s":
                print ("Liberar 0.5ml de recompensa") 
                wr.writerows(["Liberar 0.5ml de recompensa"])
            else:
                print ("Não liberar recompensa")
                wr.writerows(["Não liberar recompensa"])

            #até o momento será considerado que o experimento foirealizado 20 vezes, visto que passou para a proxima fase

            while x <50:
                quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") #contador começa no 20
                if quantidade == "s":
                    print ("O experimento segue para a mesma fase") 
                    x = contador(x)
                    print(x)
            condicao = input("O experimento que foi realizado, 50x, foi em 30minutos?")

            if condicao == "s":
                print( "O experimento seguirá para a próxima fase")
                wr.writerows(["O experimento seguirá para a próxima fase"])
else:
    with open('Opto.txt',  'w', newline = '') as wr:
        

        #Animal habituado
        var1 = (input('O animal está habituado? Responda "s" para sim ou "n" para não \n' ))
        if var1 == "s":
            resposta1 = var1  

            distancia = 30
            x = 0
            contador1=0

            dist_usuario = float(input('Qual a distância do animal? \n'))

            if dist_usuario < distancia:
                print ("Liberar 0.5ml de recompensa") 
                wr.writelines(["Liberar 0.5ml de recompensa"])

            while (x <20):
                tocar_barra = input('O animal tocou a barra?? Responda "s" para sim ou "n" para não  \n')
                if tocar_barra == "s":
                    x = contador(x)
                    

            print ( "O experimento passou de etapa")
            wr.writelines(["O experimento passou de etapa"])
                

            barra_esquerda = input("O animal tocou a barra esquerda? (Responda n para não e s para sim) \n ")
            barra_direita = input("O animal tocou a barra direita? (Responda n para não e s para sim) \n ")
            som1 = input("O som1 foi tocado quando tocou a barra esquerda? (Responda n para não e s para sim) \n ")
            som2 = input("O som2 foi tocado quando tocou a barra direita? (Responda n para não e s para sim) \n ")


            if som1 == "s" and barra_esquerda == "s":
                print ("Liberar 0.5ml de recompensa") 
                wr.writelines(["Liberar 0.5ml de recompensa"])
            else:
                print ("Não liberar recompensa")
                wr.writelines(["Não liberar recompensa"])

            if som2 == "s" and barra_direita == "s":
                print ("Liberar 0.5ml de recompensa") 
                wr.writelines(["Liberar 0.5ml de recompensa"])
            else:
                print ("Não liberar recompensa")
                wr.writelines(["Não liberar recompensa"])

            #até o momento será considerado que o experimento foirealizado 20 vezes, visto que passou para a proxima fase

            while x <50:
                quantidade = input("O experimento foi realizado novamente? (Responda n para não e s para sim) \n ") #contador começa no 20
                if quantidade == "s":
                    print ("O experimento segue para a mesma fase") 
                    x = contador(x)
                    print(x)
            condicao = input("O experimento que foi realizado, 50x, foi em 30minutos?")

            if condicao == "s":
                print( "O experimento seguirá para a próxima fase")
                wr.writelines(["O experimento seguirá para a próxima fase"])




