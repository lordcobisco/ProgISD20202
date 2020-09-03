# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:13:35 2020

@author: seidi
"""
import time 

# I. Procedimento de anestesia: Pode-se utilizar uma diversidade de fármacos para
#anestesia os animais, dentre eles Ketamina e xilazina utilizados em conjunto, halotano
#(gasoso). Verificar a dosagem correta de acordo com o peso dos animais.
print('_'*80)
print('Etapa I: Dosagem e aplicação de anestésico')

time.sleep(.5)
peso_animal = float(input('Qual o peso do animal em g? '))
while(peso_animal <= 50 or peso_animal > 5000):
  print('Você digitou um valor inválido, tente novamente')
  peso_animal = float(input('Qual o peso do animal em g? '))

# aqui entraria uma função que recebe o peso e retorna o valor da dosagem de anestesico
print('  Calculando dosagem para animal com',peso_animal,'g...' )
time.sleep(1)
print('\n  Aplique x mg de anestesico A e y mg de anestesico B')
time.sleep(.5)
print('  Aguarde ~10 minutos para que a anestesia tenha efeito')
time.sleep(.5)

input("\nTecle Enter para continuar...")
print('')

# II. Depois do anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico. As
#barras que suportam o peso do animal devem ser posicionadas no ouvido externo do
#animal. Normalmente o animal dá uma pequena piscada, devido ao estímulo da
#musculatura responsável por este movimento. Em seguida verificar a angulação da
#cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o
#lambda, para ter uma superfície de cirurgia plana.
print('_'*80)
print('Etapa II - Posicionamento do animal no estereotáxico')

time.sleep(.5)
print('\n  a.  Posicione as barras laterais nos ouvidos externos do animal')
time.sleep(.5)
print('  b.  Verifique a angulação da cabeça do animal. O ângulo que a linha entre o\
\n\tBregma e o Lambda fazem com a horizontal deve ser o mínimo possível')
time.sleep(.5)

input("\nTecle Enter para continuar...")
print('')

# III. Limpeza do campo de trabalho: Este procedimento requer o cumprimento de algumas
#etapas: Retirada da pelagem que recobre a parte superior da calota craniana, Retirada
#dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da
#caixa craniana. Por último e não menos importante deve-se limpar a calota craniana de
#qualquer resto de “pele” que esteja sobrando utilizando H2O 2 10 volumes.
print('_'*80)
print('Etapa III - Limpeza do campo de trabalho')
time.sleep(.5)
print('\n  a.  Retire a pelagem que recobre a parte superior da calota craniana')
time.sleep(.5)
print('  b.  Retire os tecidos moles até alcançar a parte óssea da caixa craniana')
time.sleep(.5)
print('  c.  Limpe a calota craniana com H2O2 volume, para retirar qualquer resto\
      \n\tde pele')

time.sleep(.5)
input("\nTecle Enter para continuar...")
print('')

# IV. Com o animal em posição e com o campo cirúrgico devidamente limpo, utiliza-se uma
#pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.
print('_'*80)
print('Etapa IV - Aplicação de poliacrilato')
print('\n  Aplique uma pequena camada de poliacrilato em todo o perímetro\
\nexterno para evitar sangramentos')
time.sleep(.5)


input("\nTecle Enter para continuar...")
print('')

# V. Após este procedimento deve-se escolher um ponto para a fixação de parafusos, de
#preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa
#e suporta uma maior profundidade do parafuso.

print('_'*80)
print('Etapa V - localização do ponto para fixação de parafusos')

# dicionário com posição das estruturas
# obs.: os valores podem não estar corretos, estou apenas testando a funcionalidade
#do código
dict_nucleus = {}
dict_nucleus['CA1']  = (-0.42,0.3,-0.2)
dict_nucleus['LH']   = (-1.0,-1.25,4.75)
dict_nucleus['mPFC'] = (1.7,0.25,-1.75)
dict_nucleus['OFC']  = (2.7,1.75,1.7)
list_keys = list(dict_nucleus.keys())
count = 1

print('\n  Posicione a agulha sobre o Bregma')
# recebe leitura do esterotáxico
AP = float(input('  Qual a medida AnteroPosterior em cm?: '))
LL = float(input('  Qual a medida LateroLateral em cm?: '))
DV = float(input('  Qual a medida DorsoVentral em cm?: '))

print('\n  Selecione a estrutura alvo:')
for key in list_keys:
  print('  ',count,'-',key)
  count += 1

ind_estrutura = int(input('  Digite a estrutura a ser acessada (índice): ')) - 1
while(ind_estrutura < 0 or ind_estrutura > len(list_keys)):
  print('  Você digitou um valor errado')
  ind_estrutura = int(input('  Digite a estrutura a ser acessada (índice): ')) - 1

estrutura = list_keys[ind_estrutura]
print('\n  Estrutura',estrutura,'escolhida')

# hipocampo
dAP = dict_nucleus[estrutura][0]
dLL = dict_nucleus[estrutura][1] # bilateral, somar e subtrair
dDV = dict_nucleus[estrutura][2]

dict_positions = {}
dict_positions['AP']   = AP + dAP
dict_positions['LL_E'] = LL + dLL # hemisfério esquerdo
dict_positions['LL_D'] = LL - dLL # hemisfério direito
dict_positions['DV']   = DV + dDV

str_show = "\n  Os pontos encontrados foram: \n\t{:.3f} cm AnteroPosterior\
\n\t{:.3f} cm LateroLateral - Hemisfério Esquerdo\
\n\t{:.3f} cm LateroLateral - Hemisfério Direito\
\n\t{:.3f} cm DorsoVentral".format(dict_positions['AP'] ,dict_positions['LL_E'] ,
dict_positions['LL_D'], dict_positions['DV'])
time.sleep(.5)
print(str_show)

time.sleep(.5)
input("\nTecle Enter para continuar...")
print('')

# VI. Após estes cálculos feitos é hora de localizar os pontos de inserção das cânulas-guia.
#Assim que estes pontos forem localizados é necessário fazer furos para a introdução
#das cânulas-guia. A localização destes pontos deve ser definida pelos valores
#encontrados nos cálculos AnteroPosterior (6,00) e LateroLateral (3,63 e 3,03). Deve-se
#escolher qual dos hemisférios vai ser colocada a primeira cânula, daí os dois valores
#para as medidas LL.
print('_'*80)
print('Etapa VI - localização do primeiro ponto de inserção das cânulas-guias')
time.sleep(.5)
print('\n  Posição do ponto de inserção no hemisfério esquerdo:')
print('  AnteroPosterior:',dict_positions['AP'],'cm')
print('  LateroLateral:  ',dict_positions['LL_E'],'cm')
input("\nTecle Enter para continuar...")
print('')

# VII. Depois de posicionar a agulha, fazer um furo com a broca até alcançar as meninges. A
#não perfuração das meninges é o procedimento ideal, e para conseguir isso apoie a
#mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +-
#45 0 de angulação.

print('_'*80)
print('Etapa VII - Perfuração com broca')
time.sleep(.5)
print('\n  Posicionando broca a 45º...')
time.sleep(1)
print('  Perfurando')
time.sleep(1)
input("\nTecle Enter para continuar...")
print('')


# VIII. Após ter atingido este objetivo, introduza a cânula-guia previamente confeccionada
#até o valor DorsoVentral (4,00) que foi calculado anteriormente.
print('_'*80)
print('Etapa VII - Introdução da Cânula DorsoVentral')
time.sleep(.5)
print('\n  Introduzindo a cânula até o valor de ',dict_positions['DV'], 'cm na direção dorso-ventral...')
time.sleep(.5)

input("\nTecle Enter para continuar...")
print('')

# IX. Logo após drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo
#orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.
print('_'*80)
print('Etapa IX - Drenagem de sangue ou líquido cefalorraquidiano')
time.sleep(.5)
print('\n  Utilize pequenos rolos de papel absorvente para retirar líquidos que\
\nestejam saindo pelo orifício criado no crânio')
time.sleep(.5)

input("\nTecle Enter para continuar...")
print('')

# X. Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura
#espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejada
#sem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o
#crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. O
#tempo de secagem varia de acordo com a temperatura e umidade da sala.
print('_'*80)
print('Etapa X - Capacete de acrílico polimerizante')
time.sleep(.5)
print('\n  a. Faça uma mistura do acrílico polimerizante com o solvente até ficar com \
\ntextura espessa porém maleável')
time.sleep(.5)
print('  b. Aplique a mistura sobre o crânio, cânula-guia e parafuso')
time.sleep(.5)
print('  c. Deixe secar até ficar suficientemente rígido')

input("\nTecle Enter para continuar...")
print('')

# XI. O próximo passo é a fixação da outra cânula-guia. Deve-se levantar levemente o braço
#do estereotáxico cuidando para que a cânula-guia previamente fixada não se
#movimente. Logo após, posicionar a agulha sobre o outro ponto de inserção da cânula-
#guia. Introduzir a cânula-guia até o valor DV (4,00) calculado previamente.
print('_'*80)
print('Etapa XI - Fixação da outra cânula-guia')
time.sleep(.5)
print('\n  Posição do ponto de inserção no hemisfério direito:')
print('  AnteroPosterior:',dict_positions['AP'],'cm')
print('  LateroLateral:  ',dict_positions['LL_D'],'cm')
input("\nTecle Enter para continuar...")

time.sleep(.5)
print('\n  Posicionando broca a 45º...')
time.sleep(1)
print('  Perfurando')
time.sleep(1)
input("\nTecle Enter para continuar...")

time.sleep(.5)
print('\n  Introduzindo a cânula até o valor de ',dict_positions['DV'], 'cm na direção dorso-ventral...')
time.sleep(.5)

print('')

# XII. Seguir novamente a descrição do item 9 e após fixar a cânula conforme item 10. De
#preferência espalhar o cimento sobre a maior área do crânio, sempre deixando um
#espaço entre o capacete e o início da área tecidual. Este cuidado previne de um futuro
#descolamento do capacete devido a entrada de sangue ou outro líquido entre o
#capacete e o crânio.
print('_'*80)
print('Etapa XII - Drenagem de sangue ou líquido cefalorraquidiano')
time.sleep(.5)
print('\n  Utilize pequenos rolos de papel absorvente para retirar líquidos que\
\nestejam saindo pelo orifício criado no crânio')
time.sleep(.5)
input("\nTecle Enter para continuar...")

time.sleep(.5)
print('\n  a. Faça uma mistura do acrílico polimerizante com o solvente até ficar com \
\ntextura espessa porém maleável')
time.sleep(.5)
print('  b. Aplique a mistura sobre o crânio, cânula-guia e parafuso')
time.sleep(.5)
print('  c. Deixe secar até ficar suficientemente rígido')
input("\nTecle Enter para continuar...")
print('')


# XIII. Levantar bem devagar seguindo as instruções do item contida no item 11. Acomodar o
#animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados.
#Assim que o animal despertar colocá-lo de volta a sua caixa-moradia.
print('_'*80)
time.sleep(.5)
print('\n  a. Levante o braço do estereotáxico e retire o animal com cautela')
print('  b. Acomode o animal em uma caixa aquecida por uma lâmpada e sem outros\
\n animais acordados')
input("\nTecle Enter para continuar...")
print('')

print('\nProcedimento Concluído!')