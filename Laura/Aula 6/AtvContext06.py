#Atividade Contextualizada 6

print('Protocolo para cirurgia estereotáxica em ratos wistar \n')

#Etapa I
print('Inicialmente, vamos escolher o tipo de fármaco a ser utilizado como anestésico na cirurgia.')

anestesicos = ['Ketamina e Xilazina','80ml-90mg/Kg e 2% - 10 a 13mg/Kg','Pentobarbital','30 a 40mg/Kg','Fentanil-Droperidol','2ml/Kg']
print('As opções de anestésicos são: ', anestesicos,'\n')
numeroAnestesico = int(input('Digite o número correspondente ao anestésico a ser utilizado (1- Ketamina e Xilazina, 2- Pentobarbital ou 3- Fentanil-Droperidol): '))
if(numeroAnestesico==1):
    print('O anestesico será:', anestesicos[0], '\n' 'E a dose será:', anestesicos[1],'\n')
elif (numeroAnestesico==2):
    print('O anestesico será:', anestesicos[2], '\n' 'E a dose será:', anestesicos[3],'\n')
else:
    print('O anestesico será:', anestesicos[4], '\n' 'E a dose será:', anestesicos[5],'\n')

#Etapa II
print('Após o anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico.')
print('Primeiramente, as barras que suportam o peso do animal deverão ser posicionadas no ouvido externo do animal. Em seguida, a angulação entre o bregma e o lambda não deverão ter diferença.')
anguloBregma = float(input('Para verificar a angulação da cabeça do animal, digite o ângulo do bregma: '))
anguloLambda = float(input('Para verificar a angulação da cabeça do animal, digite o ângulo do lambda: '))
while anguloBregma != anguloLambda:
    anguloBregma = float(input('Digite a nova angulação do bregma após reajuste: '))
    anguloLambda = float(input('Digite a nova angulação do lamda após reajuste: '))
print('Como não há diferença entre as angulações, o animal está posicionado no estereotáxico.\n')

#Etapa III
print('Agora, vamos realizar a limpeza do campo de trabalho.')
print('Inicialmente, retire a pelagem que recobre a parte superior da calota craniana do animal. Após isso, seguir para a retirada dos tecidos moles (epiderme, derme e tecido conjuntivo).')
retiradaTM = int(input('Na retirada dos tecidos moles, já se alcançou a parte óssea da caixa craniana? (Digite 1 para sim e 0 para não) '))
while retiradaTM != 1:
    retiradaTM = int(input('Após continuar com a retirada dos tecidos moles, já se alcançou a parte óssea da caixa craniana? (Digite 1 para sim e 0 para não) '))
print('Como já atingiu a parte óssea, limpar a calota craniada utilizando peróxido de hidrogênio de 10 volumes.\n')

#Etapa IV
print('Com o animal em posição e com o campo cirúrgico devidamente limpo, coloque uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos. \n')

#Etapas V e VI
print('Agora, vamos escolher um ponto para fixação dos parafusos, de preferência na parte posterior da calota craniana.')

agulha = ('AnteroPosterior','LateroLateral','DorsoVentral')
print('Quais regiões precisam ser dimensionadas para o posicionamento da agulha?', agulha)
#Atribuindo valores
posicionamento = [6.42, 3.23, 4.2]
AP = posicionamento[0] - 0.42
LL = posicionamento[1] - 0.30
DV = posicionamento[2] - 0.20
posicionamentoAgulha= {'AnteroPosterior (AP)': AP, 'LateroLateral (LL)': LL, 'DorsoVentral (DV)': DV}
print("O posicionamento da agulha será:", posicionamentoAgulha, '\n')

#Etapa VII
print('Após o posicionamento da agulha, fazer um furo com a broca até alcancar as meninges.')
print('Com o objetivo de não perfurar as meninges, deve-se perfurar o crânio a uma angulação de +-45°. \n')

#Etapa VIII
print('Neste momento, deverá ser introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00).')
for c in range(4):
    print('Introduzindo a cânula-guia.')
print('Cânula-guia introduzida até o valor DorsoVentral (4,00) \n')     

#Etapas IX e X
drenar = int(input('Está saindo sangue ou líquido cefalorraquidiano pelo orifício criado no crânio? '))
if (drenar==1):
    print('Utilize rolos de papel absorvente para drenar o líquido.')
else:
    print('Passe para a próxima etapa. \n')

print('Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa, porém maleável. Com essa mistura, faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido.\n')

#Etapa XI
print('O próximo passo é a fixação de outra cânula-guia.')
for c in range(4):
    print('Introduzindo a segunda cânula-guia.')
print('Segunda cânula-guia introduzida até o valor DorsoVentral (4,00) \n')     

#Etapa XII 
drenar = int(input('Está saindo sangue ou líquido cefalorraquidiano pelo orifício criado no crânio? '))
if drenar==1:
    print('Utilize rolos de papel absorvente para drenar o líquido.')
else:
    print('Passe para a próxima etapa. \n')

print('Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa, porém maleável. Com essa mistura, faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. De preferência, espalhar o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete e o início da área tecidual. Deixe secar até ficar suficientemente rígido.\n')

#Etapa XIII
print('Com o término de todos os procedimentos, vamos acomodar o animal.')
print('Levantar o animal bem devagar e acomodá-lo em uma caixa aquecida por uma lâmpada e sem outros animais acordados.')
animalDespertar = int(input('O animal despertou? '))
if(animalDespertar == 1):
    print('Coloque o animal em sua caixa moradia.')
else:
    print('Aguarde o animal despertar para colocá-lo em sua caixa-moradia.')
