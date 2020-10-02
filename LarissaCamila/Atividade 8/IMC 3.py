import csv

filecsv= open('imc.csv', 'w')
def menu():    
    print('0 = Sair\n1 = Calcular IMC\n2 = Classificação IMC')
    return int(input('Entre com a opção desejada:'))

while True:
    opcao = menu()

    if opcao == 0:
        print('Tchau!')
        break;

    elif opcao == 1:    
        altura = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))
        imc = (peso/altura**2)
        print('Seu índice de massa corporal é: ', imc) 

    elif opcao == 2:    

        if imc < 17.0:
            filecsv.write("Muito abaixo do peso!")
        elif imc >= 17.0 and imc < 18.5:
            filecsv.write("Abaixo do peso normal!")
        elif imc >= 18.5 and imc < 25.0:
            filecsv.write("Peso dentro do normal!")
        elif imc >= 25.0 and imc < 30.0:
            filecsv.write("Acima do peso normal!")
        elif imc > 30:
            filecsv.write("Muito acima do peso!")
filecsv.close()