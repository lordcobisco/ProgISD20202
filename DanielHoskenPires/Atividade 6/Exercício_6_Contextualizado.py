#Exercício contextualizado 6 - Cirurgia esterotáxica 

Posicionamento = list()
limpeza = list()
Animal = dict ()
Farmaco = dict ()
Anestesia = dict ()
Parafuso = 0
PosicaoParafuso = list()
PosicaoAgulha = ('AP', 'LL', 'DV')
CalculoAgulha = {'AP': 6.42, 'LL': 3.23, 'DV': 4.2}
CA1 = [-0.42, 0.3, -0.2]


print ("Bem vinda(o) ao equipamento de cirurgia esterotáxica!")
Start = input ("Podemos começar? (Digite 'sim' para começarmos)\n")

print ("Iniciando procedimento...")
print('Por favor, preencha os parâmetros conforme solicitado.')

#Procedimento I
'''
while (Start == 'sim'):
    Farmaco['Nome'] = input ('Informe qual o nome do farmaco que será utilizado: ')
    Farmaco['dosagem'] = input ('Informe qual a dosagem que será utilizada (ml): ')
    Animal['Peso'] = input ('Informe o peso do animal (Kg): ')
    Verificacao = input ("Confirme se a dosagem está correta de acordo com o peso do animal: " + (Farmaco['dosagem']) + "ml de " + (Farmaco['Nome']) + ", para um animal de " + (Animal['Peso']) + "Kg. (sim ou não)")
    if (Verificacao != 'sim'):
        print ('Você deverá informar novamente os parâmetros!')
    else:
        print ('Primeira etapa concluída com sucesso!')
        break


#Procedimento II
print ("Posicione o animal no equipamento de cirurgia esterotáxica! ")
while (True):   
    Verificacao3 = input("As barras estão posicionadas corretamente no ouvido externo do animal? (sim ou não)\n")
    if (Verificacao3 =='sim'):
        Posicionamento.append (True)
        print ('Ótimo, vamos para a próxima etapa!')
        break
    else:
        print ('Posicione as barras corretamente no ouvido externo do animal!')
        break
while (True):   
    Verificacao4 = input("Possui diferença entre a angulação da cabeça do animal e angulação de bregma e lambda? (sim ou não)\n")
    if (Verificacao4 =='não'):
        Posicionamento.append (True)
        print ('Ótimo, vamos para a próxima etapa!')
        break
    else:
        print ('Reposicione o animal!')
        break

#Procedimento III
print ("Nessa etapa, vamos realizar a limpeza do campo de trabalho!")

while (True):   
    Verificacao5 = input ('Foi realizado a retirada da pelagem que recobre a parte superior da calota craniana? (sim ou não)\n')
    if (Verificacao5 == 'sim'):
        limpeza.append(True)
        print ('Ótimo, vamos para a próxima etapa!')
        break
    else:
        limpeza.append(False)
        print ('Realize a retirada da pelagem da parte superior da calota craniana!')
        break
while (True):   
    Verificacao5 = input ('Foi realizado a retirada dos tecidos moles até alcançar a parte óssea da caixa craniana? (sim ou não)\n')
    if (Verificacao5 == 'sim'):
        limpeza.append(True)
        print ('Ótimo, vamos para a próxima etapa!')
        break
    else:
        limpeza.append(False)
        print ('Realize a retirada dos tecidos moles até alcançar a parte óssea da caixa craniana!')
        break    
while (True):   
    Verificacao5 = input ('Foi realizado a limpeza a calota craniana de qualquer resto de pele que esteja sobrando, utilizando H2O2 10 volumes? (sim ou não)\n')
    if (Verificacao5 == 'sim'):
        limpeza.append(True)
        print ('Ótimo, vamos para a próxima etapa!')
        break
    else:
        limpeza.append(False)
        print ('Realize a limpeza a calota craniana de qualquer resto de “pele” que esteja sobrando, utilizando H2O2 10 volumes!')
        break 

#Procedimento IV
print ("Utilize uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos\n")
Verificacao6 = (input("Foi aplicada a camada de poliacrilato?\n"))
if (Verificacao6 == 'sim'):
    print ('Ótimo, vamos para a próxima etapa!')
        
else:
    print ('Você deve aplicar a camada de poliacrilato!')
       
#Procedimento V
while(True):
    Parafuso = 0
    while(not Parafuso):
        Parafuso = int(input('\nDigite a quantidade de parafusos a serem fixados: '))

    for i in range(Parafuso):
        resposta = input('Informe onde o parafuso '+str(i+1) +' de '+str(Parafuso)+' será posicionado: ')
        PosicaoParafuso.append(resposta)
        print (PosicaoParafuso)
    break
print ("OBSERVAÇÃO: Cuidado para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.")

#Procedimento VII
print('Nessa etapa, vamos realizar o furo com a broca até alcançar as meninges.')
while(True):
    print('Apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 450 de angulação')
    Verificacao7 = input('Chegou até as meninges? \n')
    if(Verificacao7 == 'sim'):
        print('Furadeira parada.')
        break
    else: 
        print('Continuar furando')
        break

#Procedimento VIII
print ('Nessa etapa, vamos introduzir a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00) que foi calculado anteriormente')

#Procedimento IX

print('Drene qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.')
while(True):
    Verificacao8 = input('A drenagem foi realizada? \n')
    if(Verificacao8 == 'sim'):
        print('Ótimo, vamos para a próxima etapa!')
        break
    else: 
        print('Iniciar ou continuar drenagem!')
        break

#Procedimento X
print('Faça uma mistrura de crílico com solvente até ficar com textura espessa porém maleável . ')
while(True):
    Verificacao9 = input('A mistura está pronta? ')
    if(Verificacao9 == 'sim'):
        print('Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso')
        break
    else:
        print('Continue mexendo a mistura...')

print('Por fim, agaurde a mistura secar.')
while(True):
    Verificacao10 = input('Amistura está seca e suficientemente rígida? ')
    if (Verificacao10 == 'sim'):
        print ('Etapa concluída com sucesso')
        break
    else:
        print('Aguarde mais alguns minutos!')
        break

#Procedimento XI
print('Nessa etapa, vamos fixar a outra cânunla-guia.')
while(True):
    print('1 - Levante levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não se movimente;')
    print ('2 - Posicione a agulha sobre o outro ponto de inserção da cânula-guia;')
    print ('3 - Introduza a cânula-guia até o valor DV (4,00) calculado previamente.')
    Verificacao11 = input('A cánula-guia foi introduzida até o DorsoLateral corretamente?\n')
    if (Verificacao11 == 'sim'):
        print ('Etapa concluída com sucesso!')
        break
    else:
        print('Você deve introduzir a cânula-guia novamente...')
        break

#Procedimento XII

print('Drene novamente qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.')
print('Obs: De preferência espalhar o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete e o início da área tecidual ')
while(True):
    Verificacao12 = input('A drenagem foi realizada? \n')
    if(Verificacao12 == 'sim'):
        print('Ótimo, vamos para a próxima etapa!')
        break
    else: 
        print('Iniciar ou continuar drenagem!')
        break

#Procedimento XIII
print('1 - Levante bem devagar, tomando cuidado para que a cânulas-guia fixadas não se movimentem.')
print('2 - Acomode o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados.')
print ('3 - Por fim, assim que o animal despertar, você deve colocá-lo de volta a sua caixa-moradia.')
while(True):
    Verificacao13 = input('O procedimento foi todo realizado corretamente? ')
    if(Verificacao13 == 'sim'):
        print ('A cirurgia foi finalizada por completo e com sucesso!!!')
        break
    else:
        print('Quando o animal despertar coloque-o de volta a sua caixa-moradia!')
        break
'''
print('Posicionamento inicial da agulha:')
for i in range(len(PosicaoAgulha)):
    print(PosicaoAgulha[i], ': ', CalculoAgulha[PosicaoAgulha[i]])

print('Efetuando ajustes da agulha...')
for i in range(len(PosicaoAgulha)):
    CalculoAgulha[PosicaoAgulha[i]] += CA1[i]

print('Posicionamento da agulha após ajustes:')
for i in range(len(PosicaoAgulha)):
    print(PosicaoAgulha[i], ': ', CalculoAgulha[PosicaoAgulha[i]])

print('Agulhas devidamente posicionadas.')

"FIM DO PROGRAMA"
