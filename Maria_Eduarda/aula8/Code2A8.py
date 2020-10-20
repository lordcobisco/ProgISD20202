import math 
import csv
#Importando a biblioteca math para uso de operações como pow
#Função que calcula o IMC

def FuncImc():
    condicao=1
    resultado=[]
    while(condicao):
        peso=float(input('Insira seus peso '))
        altura=float(input('Insira seus altura '))
        imc= round(peso/math.pow(altura,2),2)
        resultado.append(imc)
        if (imc<17.0):
            print ("Imc:",imc,"Muito abaixo do peso")
        elif (imc>=17.0 and imc<18.5):
            print ("Imc:",imc,"Abaixo do peso")
        elif (imc>=18.5 and imc<25.0):
            print ("Imc:",imc,"Peso dentro do normal")
        elif (imc>=25 and imc<30):
            print ("Imc:",imc,"Acima do peso normal")
        elif (imc>=30):
            print ("Imc:",imc,"Muito acima do peso normal")
        condicao=int(input("Gostaria de fazer outra leitura, 1 para sim e 0 para não?"))
        if(not condicao):
            salvar=int(input("Gostaria de salvar os resultados dos seus pacientes:1 para sim e 0 para não"))
            if (salvar):
                opc=int(input("Qual formato, 1 para csv, 2 para txt e 3 para os dois tipos:"))
                Save(opc,resultado)
            else:
                print("Encerrando o sistema")

#Função salvar
def Save (opc,contador):
    if (opc==1):
        with open('dados2.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter= ' ',
                        quotechar= '|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Dados'] )
            spamwriter.writerow(['IMC: \n'] + [contador])
    elif (opc==2):
        with open('dados2.txt','w') as FileObject:
            FileObject.write("***Dados***\n#IMC:\n")
            FileObject.writelines(str(contador))
    elif (opc==3):
        with open('dados2.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter= ' ',
                        quotechar= '|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Dados'])
            spamwriter.writerow(['IMC: \n'] + [contador])
        with open('dados2.txt','w') as FileObject:
            FileObject.write("***Dados***\n#IMC:\n")
            FileObject.writelines(str(contador))

#Chamando a função

FuncImc()

