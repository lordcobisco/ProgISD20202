import time, sys

Exp = input("Qual a quantidade de experimentos será realizado: ")
Temp = input("\nQual a duração da sessão (min): ")
Onda = input("\nQual o comprimento de onda a ser utilizado (nm): ")
Potencia = input("\nQual a potência a ser utilizada: ")

print("Comprimento de onda: ", Onda, "Potência: ", Potencia)

def menu():    
    print('\n0 = Sair\n1 = Intensidades \n2 = Selecionar LED\n3 = Temporizador')
    return int(input('\nEntre com a opção desejada: '))


while True:
    opcao = menu()
    
    if opcao == 0:
        print ('Tchau!')
        break;
    
    elif opcao == 1:    
        print("\n-----------------INTENSIDADE DOS LEDS----------------")
        
        red = input("Insira a intensidade do LED Vermelho: ")
        green = input("Insira a intensidade do LED Verde: ")
        blue = input("Insira a intensidade do LED Azul: ")
        print("As intensidades selecionadas foram as seguintes: ","\n Vermelho: ", red, "\n Verde: ", green, "\n Azul: ", blue)
    
    elif opcao == 2:
        print("\n-----------------SELECIONE O LED----------------")
        red2 = input("Será utilizado o LED vermelho? \n1-SIM 0-NÃO: ")
        green2 = input("Será utilizado o LED verde? \n1-SIM 0-NÃO: ")
        blue2 = input("Será utilizado o LED azul? \n1-SIM 0-NÃO: ")
        rgb = [red2, green2, blue2]
        
        if red2 == 1 and green2 == 0 and blue2 == 0:
            print("Você selecionou o led Vermelho")
        elif green2 == 1 and red2 == 0 and blue2 == 0:
            print("Você selecionou o led verde")
        elif blue2 == 1 and red2 == 0 and green2 == 0:
            print("Você selecionou o led azul")

    elif opcao == 3:
        print("\n-----------------TEMPORIZADOR----------------")
        tempo = int(input("Qual a quantidade de pulsos desejado: "))
        for i in range(0, tempo): 
            sys.stdout.write("\nAtivada {}s".format(i))
            sys.stdout.flush()
            time.sleep(1)

            print ("\nEND")

