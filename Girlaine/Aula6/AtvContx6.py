
print('Programa automatizador de procedimento cirúrgico')
print('Para realização do procedimento , será necessário que o animal esteja cedado, posicionado, inserido as cordenadas tridimencionail e informações quanto a realização das etapas do procedimento a ser realizado')


Inicio = int(input(" Iniciar o procedimento cirúrgico estereotáxica? (Responda 0 para não e 1 para sim"))
if(Inicio):
    print('Sim')
else:
    print('Não')

print('O animal deve ser cedado')
Sedação = int(input(" A dosagem do cedativo esta de acordo com o peso do animal? (Responda 0 para não e 1 para sim"))
if(Sedação):
    print('Sim')
else:
    print('A dosagem deve ser ajustada ao peso do animal')


Sedação = int(input(" O animal foi cedado? (Responda 0 para não e 1 para sim"))
if(Sedação):
    print('Sim')
else:
    print('O animal deve ser sedado para iniciar o procedimento cirúgico')

print('O animal deve ser posicionadono no estereotáxico')

Posicionamento = int(input(" O animal está posicionadono no estereotáxico ? (Responda 0 para não e 1 para sim"))
if(Posicionamento):
    print('Sim')
else:
    print('O animal deve ser posicionadono no estereotáxico')

print('As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal, em resposta o animal pisca')

PosicionamentoBarra = int(input(" As barras de suportes estão posicionadas no ouvido? (Responda 0 para não e 1 para sim"))
if(PosicionamentoBarra):
    print('Sim')
else:
    print(' Posicionar as barras de suporte nos ouvidos')

ReaçãoAnimal = int(input(" O animal piscou ao ser posicionado nas barras de suporte? (Responda 0 para não e 1 para sim"))
if(ReaçãoAnimal):
    print('Sim')
else:
    print('Reveja o posicionamento das barrasa de suporte')

print('Angulação da cabeça do animal, deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana')

AngulaçãoCabeça = int(input(" Angulação bregma e o lambda  estão correspondentes ? (Responda 0 para não e 1 para sim"))
if(AngulaçãoCabeça):
    print('Sim')
else:
    print('Angulação da cabeça do animal, deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana')


print('A limpeza do campo de trabalho para inicio sa secção')

RetiradaPelagem = int(input("retirada da epiderme, derme e tecido conjuntivo ? (Responda 0 para não e 1 para sim"))
if(RetiradaPelagem):
    print('Sim')
else:
    print('Retirar a pelagem')

print('Deve-se limpar a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H 2 O 2 10 volumes')

LimparCalota = int(input("Todo o resto de pele foi retirado ? (Responda 0 para não e 1 para sim"))
if(LimparCalota):
    print('Sim')
else:
    print('Limpara a calota com utilizando H 2 O 2 10 volumes')

print('utiliza-se uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos')

Poliacrilato = int(input(" Foi colocado uma camada de poliacrilato ? (Responda 0 para não e 1 para sim"))
if(Poliacrilato):
    print('Sim')
else:
    print('utiliza-se uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos')

print('Após este procedimento deve-se escolher um ponto para a fixação de parafusos, de preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior profundidade do parafuso.')
print('Obs: Cuidar para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.')

print('Posicionar a agulha devidamente preparada para o tamanho da cânula e que servirá de suporte para a fixação das cânulas sobre o bregma. Fazer os cálculos de posicionamento AnteroPosterior (AP), LateroLateral (LL) e DorsoVentral (DV)')
print('Os valores utilizados para os cálculos: valores encontrados nas réguas a partir do posicionamento da agulha. AP: 6,42 cm, LL: 3,23 cm, DV: 4,2 cm')

print('Os valores utilizados para os cálculos: valores encontrados nas réguas a partir do posicionamento da agulha')

PosicionamentoAgulha = ['AP: 6,42 cm', 'LL: 3,23 cm', 'DV: 4,2 cm']
for nome in PosicionamentoAgulha:
    print(PosicionamentoAgulha)

print('Calcule o valor: CA1: AP - 0,42 cm LL +/- 0,30 cm DV - 0,20 cm.')
ResultadoSubtraçãoAP = 6.42-0.42
print(ResultadoSubtraçãoAP)

ResultadoSomaLL = 3.33+0.30
print(ResultadoSomaLL)

ResultadoSubtraçãoDV = 4.20-0.20
print(ResultadoSubtraçãoDV)

print('Após estes cálculos feitos é hora de localizar os pontos de inserção das cânulas-guia. Assim que estes pontos forem localizados é necessário fazer furos para a introdução das cânulas-guia')

AnteroPosterior = ResultadoSubtraçãoAP
print(ResultadoSubtraçãoAP)

LateroLateral = ResultadoSomaLL 
print(ResultadoSomaLL)

Furar = int(input(" Faça um furo com a broca até alcançar as meninges (Responda 0 para não e 1 para sim"))
if(Furar):
    print('Sim')
else:
    print('Faça um furo com a broca até alcançar as meninges')

print ('Após ter atingido este objetivo, introduza a cânula-guia previamente confeccionada até o valor DorsoVentral que foi calculado anteriormente')
 IntroduzirCandula = int(input("Introduzir canula")
if(IntroduzirCandula):
    print(ResultadoSubtraçãoDV)

print('Logo após drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo peloorifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente)

Mistura = ['acrílico polimerizante','solvente']
print(Mistura)

print("Deixe secar até ficar suficientemente rígido. O tempo de secagem varia de acordo com a temperatura e umidade da sala.")
print('O próximo passo é a fixação da outra cânula-guia')

Manuseio = int(input('levante levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não semovimente'))
print(Manuseio)

Manuseio = int(input('introduzir candula'))
if(Manuseio = ResultadoSubtraçãoDV)
print('ResultadoSubtraçãoDV')
elif (Manuseio = ResultadoSubtraçãoAP)
print( 'ResultadoSubtraçãoAP')
else:
    print('Não manusear')

print('Logo após drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo peloorifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente)

Canula = int(input('A cânula foi fixada? (responda 0 paraa não e 1 para sim'))
if(Caula)
print(Fixada)
else:
    print('A cânula deve ser fixada')

print('Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados. Assim que o animal despertar colocá-lo de volta a sua caixa-moradia.')
print('Fim do programa')