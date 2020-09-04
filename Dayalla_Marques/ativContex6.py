# Atividade 6: procedimento cirúrgica
#PROCEDIMENTO DE ANESTESIA


value = input('digite o fármaco usando 0 ou 1:')
print(value)

if(value == '0'): print("xilazina")
if(value == '1'): print("ketamina")

print("Verifique a dose correta do medicamento de acordo com o peso do animal: ")

dosagemCorreta = input("A dosagem está correta (aperte 0 pra sim ou 1 pra nao)?")
if(dosagemCorreta == '0'): print("dosagem correta\n")
if(dosagemCorreta == '1'): print("dosagem incorreta\n")

########################################
# POSICIONAMENTO DO ANIMAL NO APARELHO
#########################################

print('Verifique a angulação da cebeça do animal: \n')
angulacaoCabeca = input('A angulacao da cabeça do animal está correta? Tecle 0 para sim e 1 para não: ')
if(angulacaoCabeca == '0'): print("Angulação correta")
if(angulacaoCabeca == '1'): print("Angulacao incorreta")

#######################################
#LIMPEZA DO CAMPO DE TRABALHO
######################################

print("Limpeza do campo de trabalho: \n")

print("Limpe o campo de trabalho: \n")
retiradadaPelagem = input('Digite 0 para retirada da pelagem: \n')
if(retiradadaPelagem == '0'): print("Retirada da pelagem feita com sucesso!")

print("Retirada dos tecidos moles: \n")
retiradadosTecidosmoles= input('Digite 0 para retirada dos tecidos moles: \n')
if(retiradadosTecidosmoles == '0'): print("Retirada feita com sucesso!")

print("Limpeza da calota craniana: \n")
calotaCraniana = input('Digite 0 para limpeza de calota craniana: \n')
if(calotaCraniana == '0'): print("Limpeza da calota realizada com sucesso!\n")

#######################################
# Com o animal em posição e com o campo cirúrgico devidamente limpo, utiliza-se uma
# pequena camada de poliacrilato
######################################

print("Camada de poliacrilato: \n")
poliacrilato = input('Tecle 0 para poliacrilato: ' )
if(poliacrilato == '0'): print("poliacrilato feito com sucesso em todo o perímetro externo!")

######################################
# Fixação de parafusos
#######################################

print("Fixação de parafusos: \n")

ap = float(input('Digite um valor para AP: \n'))
print(ap)

ll = float(input('Digite um valor para LL: \n'))
print(ll)

dv = float(input('Digite um valor para DV: \n'))
print(dv)

x = float(input('Digite o primeiro valor de estrutura\n'))
print(x)
y = float(input('Digite o segundo valor de estrutura\n'))
print(y)
z = float(input('Digite o terceiro valor de estrutura\n'))
print(z)

print("Calculando os valores:\n")

# ATENÇÃO: x, y, e z são os valores encontrados nas réguas. Subtrai AP, LL E DV e obtive 3 valores

primeiroValor = ap-x
segundoValor = ll-y
terceiroValor = dv-z

print("Os valores são: \n")
print(primeiroValor, segundoValor, terceiroValor)
    
lista123 = [primeiroValor, segundoValor, terceiroValor]

#lista123 = random.rand(3)
for terceiroValor in lista123:
    print("o novo valor de DV é: ")
    print(terceiroValor)

# A variavel terceiroValor é o valor de DV

    
    
    

########################
# Imprimindo lista e tupla de valores
########################

listaValoresExper = [primeiroValor, segundoValor, terceiroValor]
tuplaValoresExper = (primeiroValor, segundoValor, terceiroValor)

print(listaValoresExper)
print(tuplaValoresExper)

############################
# Dicionário 
############################

dicionario1Exper = {'primeiro valor': [primeiroValor]}
dicionario2Exper = {'segundo valor': [segundoValor]}
dicionario3Exper = {'terceiro valor': [terceiroValor]}

print(dicionario1Exper)
print(dicionario2Exper)
print(dicionario3Exper)

#################################
# Inserção das cânulas - guia
#################################


    
valor1hemisferio = input("valor hemisfério 1: \n")
valo2hemisferio  = input("valor hemisfério 2: \n")

print('escolher qual dos hemisférios vai ser colocada a primeira cânula\n')
    
t = bool(input("Digite 0 ou 1 para escolher o hemisfério 1 ou 2, respectivamente: \n"))
if  True: print("hemisferio 1 foi escolhido")
if  False: print("Hemisferio 2 foi escolhido")

print("ATENÇÃO! Começou o processo: \n")
if dv < 4 :
    print("O valor de DV precisa ser igual a 4 e ainda nao é\n")
elif dv == 4:
    print("tudo pronto!\n")
else:
    print("NÃO CONTINUE O PROCESSO")
    

#####################################
# Perfurando o crânio, angulo de 45 graus
######################################

angulocorreto = 0
while not angulocorreto:
    animaisacordados = int(input('digite o angulo correto: '))
    
else:
    print('o ângulo está correto e é 45 graus.')
    

##########################################        
# Drenando o sangue
################################

print("Drene o sangue usando papel absorvente\n")

###############################
# mistura de acrilico polimerizante
##############################

passo1 = ('Faça uma mistura do acrílico polimerizante', 'Com essa mistura faça um capacete abrangendo o crânio')
print(passo1)

passo2 = ('deixe secar até ficar rígido', 'o tempo da saa varia com a temperatura e umidade da sala')
print(passo2)

#################################
# Inserção das cânulas - guia 2
#################################
# Segunda cânula - guia

    
valor1hemisferio = input("valor hemisfério 1: \n")
valo2hemisferio  = input("valor hemisfério 2: \n")

print('escolher qual dos hemisférios vai ser colocada a primeira cânula\n')
    
t = bool(input("Digite 0 ou 1 para escolher o hemisfério 1 ou 2, respectivamente: \n"))
if  True: print("hemisferio 1 foi escolhido")
if  False: print("Hemisferio 2 foi escolhido")

print("cuidado pra nao tocar na primeira cânula - guia!!!\n")

print("ATENÇÃO! Começou o processo: \n")

if dv < 4 :
    print("O valor de DV precisa ser igual a 4 e ainda nao é\n")
elif dv == 4:
    print("tudo pronto!\n")
else:
    print("ATENÇÃO! Não continue esse processo\n")

#########################################
# Seguir novamente a descrição do item 9 
#########################################

print("Drene o sangue usando papel absorvente\n")

####################################################
# Aqui to seguindo os passos do item 10 e adicionando mais informações
####################################################
print("Siga as orientações a seguir: \n")
passo3 = ('De preferência espalhar o cimento sobre a maior área do crânio crânio, sempre deixando um espaço entre o capacete e o início da área tecidual. Este cuidado previne de um futuro descolamento do capacete devido a entrada de sangue u outro líquido entre o capacete e o crânio')
print(passo3)

####################################################
# seguindo o item 11 e adicionando mais informações#
####################################################

passo4 = ('Levantar bem devagar seguindo as instruções do item contida no item 11.', 'Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados', 'Assim que o animal despertar colocá-lo de volta a sua caixa-moradia')
print(passo4)




animaisacordados = 0
while not animaisacordados:
    animaisacordados = int(input('digite 1 quando os animais estiverem dormindo: '))
    
else:
    print('Os animais estão dormindo')
    print("Acomodar animal")


 