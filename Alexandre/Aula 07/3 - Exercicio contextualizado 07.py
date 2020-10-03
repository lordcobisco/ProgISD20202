import time 
import sys 



class RGB: 
    def __init__(self,lista_geral):
        self.lista_geral = lista_geral
    def execucao_programa(self):
        print("\n## Ok, agora que temos os dados, vamos iniciar os experimentos.Caso queira interromper o programa em qualquer momento escreva 'parar'##")

        i = 1
        while i<= len(lista_geral):
            print("\n## Ok, Experimento ",i,"iniciando##")
            lista_desse_experimento = lista_geral[(i-1)]
            lista_caracteristicas_dispositivos = lista_desse_experimento[2]
            d = 1
            while d <= len(lista_caracteristicas_dispositivos):
                lista_dispositivo_atual = lista_caracteristicas_dispositivos[(d-1)]

                lista_tempo_acionar_dispositivos =[]
                lista_tempo_acionar_dispositivos.append (lista_dispositivo_atual[2])
                
                lista_intensidade_dispositivo = []
                lista_intensidade_dispositivo.append(lista_dispositivo_atual[1])

                lista_cor_dispositivo = []
                lista_cor_dispositivo.append(lista_dispositivo_atual[0])


                d = d + 1
                c = 1
                while c<= len(lista_tempo_acionar_dispositivos):
                    tempo_acionar_dispositivo = lista_tempo_acionar_dispositivos[c-1]
                    intensidade_dispositivo_atual = lista_intensidade_dispositivo[c-1]
                    cor_dispositivo_atual = lista_cor_dispositivo[c-1]
                    
                    time.sleep(tempo_acionar_dispositivo)
                    print("O dispositivo",d-1,"foi ligado na intensidade",intensidade_dispositivo_atual,"com a cor",cor_dispositivo_atual)
                    c = c+1

            #Finalizar experimento
            tempo_desse_experimento = lista_desse_experimento[(0)]
            i = i + 1

            time.sleep(tempo_desse_experimento)
            print("Esse experimento acabou")
        



 
def parar():
    parar = sys.exit()
    return parar 

print ("### Olá, seja bem vindo ao nosso programa. Responda as perguntas a seguir para utilizar da maneira correta ###")

numero_experimentos = int(input("Quantos experimentos serão realizados?"))
i = 1
lista_geral = []
for item in range (0,numero_experimentos):
    lista_geral.append([])

while i <= numero_experimentos:
    print ("\nExperimento",i,)
    tempo_experimento = int(input("Qual será o tempo do experimento?"))
    lista_geral[(i-1)].append(tempo_experimento)

    numero_dispositivo = int(input("Quantos dispositivos serão necessários no experimento?"))
    lista_geral[(i-1)].append(numero_dispositivo)

    c = 1
    lista_cor_e_intensidade_por_dispositivo_tempo = []
    for item in range (0,numero_dispositivo):
         lista_cor_e_intensidade_por_dispositivo_tempo.append([])

    while c <= numero_dispositivo:
        print ("\n dispositivo",c)
        cor_dispositivo = input("Qual será a cor do Led utilizado nesse dispositivo?")
        lista_cor_e_intensidade_por_dispositivo_tempo[(c-1)].append(cor_dispositivo)
        intensidade_dispositivo = int(input("Qual será a intensidade da cor do lED utilizado?"))
        lista_cor_e_intensidade_por_dispositivo_tempo[(c-1)].append(intensidade_dispositivo)

        tempo_acionar_LED = tempo_experimento + 1
        while tempo_acionar_LED > tempo_experimento:
            tempo_acionar_LED = int(input("Em quantos segundos esse dispositivo deve acionar?"))
            if tempo_acionar_LED > tempo_experimento :
                print("O tempo está inadequado, insira novo valor")
            else:
                lista_cor_e_intensidade_por_dispositivo_tempo[(c-1)].append(tempo_acionar_LED)

        c = c + 1
    lista_geral[(i-1)].append(lista_cor_e_intensidade_por_dispositivo_tempo)

    i = i + 1

print(lista_geral)

#Execução invocando a classe e função 
h = RGB(lista_geral)
print(h.execucao_programa())  
 
    
    
#
    


