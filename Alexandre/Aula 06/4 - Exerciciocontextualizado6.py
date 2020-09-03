
## ANESTESIA
    
#Montar LISTA com o nome do fármaco e as informações desse fármaco (por ordem de posição: dose, via de administração e tempo de ação). Algumas informações estão com tupla, já que a ordem não pode ser modificada nesses casos. 
cetamina_lista = [("dose",100,"mg/kg"),"Intraperitoneal (IP)",("ação durante",20,"min")]
isoflurano_lista = [("dose",3,"%"),"Inalatória","variável"]
acepromazina_lista = [("dose",3,"mg/Kg"),"Intraperitoneal (IP)","ação durante",30,"min"]
midazolam_lista = [("dose",5,"mg/Kg"),"Intraperitoneal (IP)",("ação durante",20,"min")]
diazepam_lista = [("dose",5,"mg/Kg"),"Intraperitoneal (IP)",("ação durante",20,"min")]

# Dicionário com o nome do fármaco  que será utilizado para busca das informaçõs do fármaco
dicionario_farmacos = {"cetamina":cetamina_lista,"isoflurano":isoflurano_lista,"acepromazina":acepromazina_lista,"midazolam":midazolam_lista,"diazepam":diazepam_lista}

#Montar DICIONÁRIO de informações dos fármacos (criação de DICIONÁRIO e USO de ESTRUTURA DE REPETIÇÃO)
anestesico_informacoes = "sim"
while anestesico_informacoes != "nao":
    anestesico_informacoes = input("O primeiro passo para o procedimento é realizar a anestesia adequada. Os anestésicos possiveis são cetamina,isoflurano,acepromazina,midazolam,diazepam.\n Para receber informações sobre esses anestésicos digite o nome (exatamente igual), caso não deseje informaões, digite nao")
    if anestesico_informacoes == "nao":
        print ("\nOk, agora iremos solicitar escolher o anestésico e calcular a dose com base no peso dado")
    else:
        print(dicionario_farmacos[anestesico_informacoes])

#Calcular a dose com base no fármaco escolhido
anestesico_escolhido = input("Escreva o nome do anestésico que irá utilizar")
peso_animal = int(input("Digite o peso do animal"))

anestesico_escolhido_lista = dicionario_farmacos[anestesico_escolhido]
dose_anestesico_escolhido = anestesico_escolhido_lista[0]
valor_anestesico_escolhido = dose_anestesico_escolhido[1]

dose_anestesico = valor_anestesico_escolhido/peso_animal

if anestesico_escolhido!= "isoflurano": #Apagar
    print ("Faça um dose de", dose_anestesico, "mL")
   
anestesico_aplicado = "não"

while anestesico_aplicado != "sim": 
    anestesico_aplicado = input("O anestésico foi feito? (Digite 'sim' ou 'não', exatamente igua e sem as aspas)")
    if anestesico_aplicado == "sim":
         print ("\n## Agora iremos para a fase de posicionar o animal no estereotáxico ##")
    else:
         print("\nAplique o anestésico na dosagem indicadada anteriormente")

## POSICIONAMENTO ESTEREOTÁXICO
print ("Posicione o animal no estereotáxico de modo que as barras se posicionem no ouvido externo e não tenha movimento horizontal da cabeça")
posicionamento_correto = "não"

while posicionamento_correto != "sim": 
    posicionamento_correto = input("O animal teve o estereotáxico posicionado de modo que as barras se posicionem no ouvido externo e não tenha movimento horizontal da cabeça  (Digite 'sim' ou 'não', exatamente igua e sem as aspas)")
    if posicionamento_correto == "sim":
        print ("\nAgora verifique a a angulação da cabeça do animal, a qual deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana")
        angulacao_cabeca = "não"
        while angulacao_cabeca != "sim": 
            angulacao_cabeca = input("A angulação da cabeça do animal fo medida de modo que não existia diferença de angulação entre o bregma e o lamba? (Digite 'sim' ou 'não', exatamente igua e sem as aspas)")
            if angulacao_cabeca == "sim":
                print ("\n## Agora iremos para a fase de Limpeza do campo de trabalho ##")
            else:
                print("\nVerifique novamente a posição ajustando as angulações")
    else:
         print("\nPosicione novamente o estereotáxico")

    
##LIMPEZA DO CAMPO DE TRABALHO E APLICAÇÃO DE POLIACRILATO 
print ("Para cumprir essa etapa realize a retirada da pelagem que recobre a parte superior da calota craniana, retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana e limpar a calota craniana com peroxido de hidrogênio 10 volumes")

limpeza_campo = "não"

while limpeza_campo != "sim": 
    limpeza_campo = input("A limpeza foi realizada seguindo os passos descritos anteriormente? (Digite 'sim' ou 'não', exatamente igua e sem as aspas)")
    if limpeza_campo == "sim":
         print ("\nAplique uma fina camada de poliacrilato em todo o perímetro externo para evitar sangramento.") 
         print("\n## Agora iremos para a fase de escolher o ponto de fixação do parafuso ##")
    else:
         print("\nRealize a limpeza de campo conformo os passos descritos anteriormente")


##FIXAÇÃO DO PARAFUSO

#Valores regua 
print ("Para fixar o parafuso posicione a agulha sobre o bregma. Na sequência digite os valores solicitados da regua ")
valor_regua_AP = float(input("Digite o valor Anteroposterior (AP) encontrado na regua a partir do posicionamento da agulha" ))
valor_regua_LL = float(input("Digite o valor latero-lateral (LL) encontrado na regua a partir do posicionamento da agulha" ))
valor_regua_DV = float(input("Digite o valor Dorsoventral (DV) encontrado na regua a partir do posicionamento da agulha" ))

valor_regua_lista = [valor_regua_AP,valor_regua_LL,valor_regua_DV]

#Valores parafuso
print("\nAgora insira os valores do núcleo ou estrutura desejado")
valor_estrutura_AP = float(input("Digite o valor Anteroposterior (AP) do núcleo ou estruturada desejada"))
valor_estrutura_LL = float(input("Digite o valor latero-lateral (LL)  do núcleo ou estruturada desejada"))
valor_estrutura_DV = float(input("Digite o valor Dorsoventral (DV) do núcleo ou estruturada desejada"))

#Valores do posicionamento
valores_posicionamento = [valor_regua_AP - valor_estrutura_AP,valor_regua_LL - valor_estrutura_LL,valor_regua_LL+valor_estrutura_LL,valor_regua_DV - valor_estrutura_DV]
print ("Os valores de posicionamento são: ",valores_posicionamento)

#Furo para inserção da cânula guia nos valores de posicionamento encontrados anteriormente
print("\n## Agora vamos realizar o furo para inserir a cânula guia. Para isso, Será solicitado para dizer qual lado (1 = direita , 2 = esquerda) irá ser inserida a cânula. Na sequencia irá sair os dados do posicionamento") 
lado_canula = int(input("Qual lado será inserida a cânula?"))
print ("O valor AP é:",valores_posicionamento[0],"O valor LL é: ",valores_posicionamento[lado_canula])

print("\n## Agora realize a perfuração nos pontos indicados até chegar as meninges. O ideal é não pefurar as meninges e para conseguir isso apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 45 graus de angulação##")

#Furo profundidade e introduzir canula até o valor DV
perfuracao_profundidade = "nao"
while perfuracao_profundidade != "sim":
    perfuracao_profundidade = input("A perfuração alcançou a meninge? (Responda 'nao' ou 'sim', exatamente igual")
    if perfuracao_profundidade == "nao":
        print ("\nOk, Continue perfurando até alcançar a meninge")
    else:
        print("\n## Logo após, introduza a cânula-guia previamente confeccionada até o valor DorsoVentral: ", valores_posicionamento[3])
        print("\n## Após introduzir, drene qualquer sangue ou líquido cefaloraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente ")

# Item X - Secagem mistura 
print("\n## Agora faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejada sem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. O tempo de secagem varia de acordo com a temperatura e umidade da sala")

tempo_secagem = "não"

while tempo_secagem != "sim": 
    tempo_secagem = input("A mistura secou? (Digite 'sim' ou 'nao' exatamente igual sem aspas)")
    if tempo_secagem == "sim":
         print ("\n## Agora Agora iremos fixar a cânula guia##")
    else:
         print("\nAguarde a mistura secar")

# Fixação da cânula
print("Agora Deve-se levantar levemente o braço do estereotáxico cuidando para que a cânula-guia previamente fixada não se movimente")
print("Logo após, posicionar a agulha sobre o outro ponto de inserção da cânula-guia. Introduzir a cânula-guia até o valor DV:",valores_posicionamento[3])

introducao_canula = "não"

while introducao_canula != "sim": 
    introducao_canula = input("\nA cânula foi introduzida até o valor de DV? (Digite 'sim' ou 'nao' exatamente igual sem aspas)")
    if introducao_canula == "sim":
         print ("\n## Agora repita o passo de drenagem do sangue e líquido cefalo raquidiano e na sequência repetir a mistura do acrilitico") 
    else:
         print("Introduza a cânula até o valor de DV")

#Finalização (USO DO IF,ELIF e ELSE)
print("\n## Agora, levante levemente o braço do estereotáxico, tendo cuidado para a cânula guia previamente fixada não se movimentar. Na sequência acomodar em caixa aquecida por uma lâmpada e sem outros animais acordados")
caixa_animal = 4
while caixa_animal != 3:
    caixa_animal = int(input("O animal está fora da caixa(1), dentro da caixa mas não desperto(2) ou dentro da caixa e desperto(3)? (Responda 1,2 ou 3, conforme o que tem nos parênteses) "))
    if caixa_animal == 1:
        print("\ncoloque o animal na caixa aquecida e aguarde ele despertar para colocar de volta a sua moradia")
    elif caixa_animal == 2:
        print ("\nAguarde o animal despertar para colocar de volta a sua moradia")
    else:
        print("\n ## Coloque de volta a sua moradia e fim do procedimento ## ")
        
    










