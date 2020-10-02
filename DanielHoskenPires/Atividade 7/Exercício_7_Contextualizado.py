
def lerEletrodos(Vmax, qtd=96):
    import random
    saida = list()
    for i in range(qtd):
        saida.append(round(random.randint(0,255)))
    return saida


print ('Olá, seja bem vinda(o) ao procedimento de optogenética!')
Start = input ("Podemos começar? (Digite 'sim' para começarmos)\n")
if (Start == 'sim'):
    print ("Iniciando procedimento...")


#PROCEDIMENTO 1 - Parâmetros iniciais de segurança
while Start == "sim":   
    equipe = input ("A equipe está preparada para começar? (Digite 'sim' ou 'nao')\n")
    equipamentos = input ("Os equipamentos e ferramentas estão no local correto? (Digite 'sim' ou 'nao')\n")
    seguranca = input ("Foram checados todos os itens de segurança? (Digite 'sim' ou 'nao')\n")
    animal = input ("O animal está devidamente posicionado? (Digite 'sim' ou 'nao')\n")
    break

if (equipe == 'sim' and equipamentos == 'sim' and seguranca == 'sim' and animal =='sim'):
     print ("Parâmetros iniciais ajustados! Vamos para a próxima etapa...")
elif (equipe != 'sim' and equipamentos == 'sim' and seguranca == 'sim' and animal =='sim'):
    print ("Assegure-se de que a equipe está toda preparada para darmos sequência ao procedimento!")
elif (equipe == 'sim' and equipamentos != 'sim' and seguranca == 'sim' and animal =='sim'):
    print ("Assegure-se de que os equipamentos e ferramenta estejam no local corrreto para darmos sequência ao procedimento!")
elif (equipe == 'sim' and equipamentos == 'sim' and seguranca != 'sim' and animal =='sim'):
    print ("Assegure-se que os itens de segurança estejam de acordo!")
elif (equipe == 'sim' and equipamentos == 'sim' and seguranca == 'sim' and animal !='sim'):
    print ("Posicione o animal corretamente!")
else:
    print ("Alguns parâmetros impedem de dar sequência ao procedimento de optogenética. Reinicie o procedimento!")

emergencia = input("Digite 'stop' em caso de emergência, ou qualquer tecla para continuramos: ")
if emergencia == "stop":
    print ("Equipamento desligado por questões de segurança")
else:
    print ("Como não houve nenhuma emergência, vamos para a próxima etapa...")

#Infectar animal com vírus

print ("Nessa etapa, vamos injetar o vírus no animal!")
while (True):
    print ('1 - Limpe o local onde será aplicado o vírus;')
    print ('2 - Posicione a agulha sobre o local;')
    print ('3 - Introduza o vírus até a quantidade previamente especificada;')
    Verificacao1 = input("O vírus foi injetado corretamente? (Digite 'sim' ou 'nao')\n")
    if (Verificacao1 == 'sim'):
        print ('Etapa concluída com sucesso!')
        break
    else:
        print('Continue introduzindo o vírus...')

emergencia = input("Digite 'stop' em caso de emergência, ou qualquer tecla para continuramos: ")
if emergencia == "stop":
    print ("Equipamento desligado por questões de segurança")
else:
    print ("Como não houve nenhuma emergência, vamos para a próxima etapa...")

#Inserir fibra óptica no animal
print ("Nessa etapa, vamos inserir a fibra óptica no animal!")
ProfundidadeFibra = input("Informe qual é a profundidade (em mm) que irá inserir a fibra óptica: ")
while(True):
    print ("Insira a fibra óptica no animal até a profundidade de", ProfundidadeFibra, "mm")
    Verificacao2 = input("A fibra óptica foi inserida corretamente? (Digite 'sim' ou 'nao')\n")
    if (Verificacao2 == 'sim'):
        print ('Etapa concluída com sucesso!')
        break
    else:
        print('Continue introduzindo a fibra...')

emergencia = input("Digite 'stop' em caso de emergência, ou qualquer tecla para continuramos: ")
if emergencia == "stop":
    print ("Equipamento desligado por questões de segurança")
else:
    print ("Como não houve nenhuma emergência, vamos para a próxima etapa...")

# Leitura dos eletrodos
print ("Nessa etapa, vamos fazer a leitura dos eletrodos!")
eletrodos = list()
eletrodos = lerEletrodos(255)

emergencia = input("Digite 'stop' em caso de emergência, ou qualquer tecla para continuramos: ")
if emergencia == "stop":
    print ("Equipamento desligado por questões de segurança")
else:
    print ("Como não houve nenhuma emergência, vamos para a próxima etapa...")

#Dados dos eletrodos
Verificacao3 = input ("Você gostaria de saber os valores de tensão dos eletrodos? (Digite 'sim' ou 'nao')\n")
if (Verificacao3 == 'sim'):
    print ("A saída do eletrodo 1 é de R:", eletrodos[0], ", G:", eletrodos[1], "e B:", eletrodos[2], ".")
    print ("A saída do eletrodo 2 é de R:", eletrodos[3], ", G:", eletrodos[4], "e B:", eletrodos[5], ".")
    print ("A saída do eletrodo 3 é de R:", eletrodos[6], ", G:", eletrodos[7], "e B:", eletrodos[8], ".")
    print ("A saída do eletrodo 4 é de R:", eletrodos[9], ", G:", eletrodos[10], "e B:", eletrodos[11], ".")
    print ("A saída do eletrodo 5 é de R:", eletrodos[12], ", G:", eletrodos[13], "e B:", eletrodos[12], ".")
    print ("A saída do eletrodo 6 é de R:", eletrodos[15], ", G:", eletrodos[16], "e B:", eletrodos[13], ".")
    print ("A saída do eletrodo 7 é de R:", eletrodos[18], ", G:", eletrodos[19], "e B:", eletrodos[20], ".")
    print ("A saída do eletrodo 8 é de R:", eletrodos[21], ", G:", eletrodos[22], "e B:", eletrodos[23], ".")
    print ("A saída do eletrodo 9 é de R:", eletrodos[24], ", G:", eletrodos[25], "e B:", eletrodos[26], ".")
    print ("A saída do eletrodo 10 é de R:", eletrodos[27], ", G:", eletrodos[28], "e B:", eletrodos[29], ".")
    print ("A saída do eletrodo 11 é de R:", eletrodos[30], ", G:", eletrodos[31], "e B:", eletrodos[32], ".")
    print ("A saída do eletrodo 12 é de R:", eletrodos[33], ", G:", eletrodos[34], "e B:", eletrodos[35], ".")
    print ("A saída do eletrodo 13 é de R:", eletrodos[36], ", G:", eletrodos[37], "e B:", eletrodos[38], ".")
    print ("A saída do eletrodo 14 é de R:", eletrodos[39], ", G:", eletrodos[40], "e B:", eletrodos[41], ".")
    print ("A saída do eletrodo 15 é de R:", eletrodos[42], ", G:", eletrodos[43], "e B:", eletrodos[44], ".")
    print ("A saída do eletrodo 16 é de R:", eletrodos[45], ", G:", eletrodos[46], "e B:", eletrodos[47], ".")
    print ("A saída do eletrodo 17 é de R:", eletrodos[48], ", G:", eletrodos[49], "e B:", eletrodos[50], ".")
    print ("A saída do eletrodo 18 é de R:", eletrodos[51], ", G:", eletrodos[52], "e B:", eletrodos[53], ".")
    print ("A saída do eletrodo 19 é de R:", eletrodos[54], ", G:", eletrodos[55], "e B:", eletrodos[56], ".")
    print ("A saída do eletrodo 20 é de R:", eletrodos[57], ", G:", eletrodos[58], "e B:", eletrodos[59], ".")
    print ("A saída do eletrodo 21 é de R:", eletrodos[60], ", G:", eletrodos[61], "e B:", eletrodos[62], ".")
    print ("A saída do eletrodo 22 é de R:", eletrodos[63], ", G:", eletrodos[64], "e B:", eletrodos[65], ".")
    print ("A saída do eletrodo 23 é de R:", eletrodos[66], ", G:", eletrodos[67], "e B:", eletrodos[68], ".")
    print ("A saída do eletrodo 24 é de R:", eletrodos[69], ", G:", eletrodos[70], "e B:", eletrodos[71], ".")
    print ("A saída do eletrodo 25 é de R:", eletrodos[72], ", G:", eletrodos[73], "e B:", eletrodos[74], ".")
    print ("A saída do eletrodo 26 é de R:", eletrodos[75], ", G:", eletrodos[76], "e B:", eletrodos[77], ".")
    print ("A saída do eletrodo 27 é de R:", eletrodos[78], ", G:", eletrodos[79], "e B:", eletrodos[80], ".")
    print ("A saída do eletrodo 28 é de R:", eletrodos[81], ", G:", eletrodos[82], "e B:", eletrodos[83], ".")
    print ("A saída do eletrodo 29 é de R:", eletrodos[84], ", G:", eletrodos[85], "e B:", eletrodos[86], ".")
    print ("A saída do eletrodo 30 é de R:", eletrodos[87], ", G:", eletrodos[88], "e B:", eletrodos[89], ".")
    print ("A saída do eletrodo 31 é de R:", eletrodos[90], ", G:", eletrodos[91], "e B:", eletrodos[92], ".")
    print ("A saída do eletrodo 32 é de R:", eletrodos[93], ", G:", eletrodos[94], "e B:", eletrodos[95], ".")
else:
    print ("Etapa concluída... Vamos para a próxima etapa!")

emergencia = input("Digite 'stop' em caso de emergência, ou qualquer tecla para continuramos: ")
if emergencia == "stop":
    print ("Equipamento desligado por questões de segurança")
else:
    print ("Como não houve nenhuma emergência, vamos para a próxima etapa...")

#Dados dos eletrodos com uma outra abstração (contendo classe e função)
class dispositivo:
    def __init__(self, rgb, eletrodos):
        self.eletrodos = rgb
        self.rgb = eletrodos
    
    def lerEletrodos(self):
        return self.eletrodos

    def determinarcorled(lista):
        print('Aqui sairá a cor do RGB')
        
eletrodos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
rgb = [1, 2, 3]

a = dispositivo(eletrodos, rgb)
print(a.lerEletrodos())
print(a.determinarcorled())

b = dispositivo(eletrodos, rgb)
print(a.lerEletrodos())
print(a.determinarcorled())

c = dispositivo(eletrodos, rgb)
print(a.lerEletrodos())
print(a.determinarcorled())

#Fim do experimento

print("O experimento foi finalizado com sucesso!")
