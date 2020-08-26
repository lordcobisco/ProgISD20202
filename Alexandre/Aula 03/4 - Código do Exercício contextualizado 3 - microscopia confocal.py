# Definindo as variáveis para funcionamento do microscópio confocal 
light_path = "campo claro"
intensidade_luz = 20
pixel_imagem = "512x512"
Velocidade_escaneamento = 10
media_imagem = 1
tons_cinza = 12 
area_scaneada = 160
slices = 20
intervalo = 0,91
zoom = 2

#Abertura do programa
print ("## Esse programa tem como objetivo receber parâmetros para configuração de um microscópio confocal ##")

#Comparação entre configurações iniciais das variáveis e configurações do usuário
light_path_usuario = input("\nDigite o light path (campo claro ou DAPI): ")
print ("Houve alteração na variável inserida?", light_path != light_path_usuario)
intensidade_luz_usuario = float(input("Digite um valor da intensidade da luz do aparelho: "))
print ("Houve alteração na variável inserida?", intensidade_luz != intensidade_luz_usuario)
pixel_imagem_usuario = str (input("Digite o valor dos pixels da imagem: "))
print ("Houve alteração na variável inserida?", pixel_imagem != pixel_imagem_usuario)
Velocidade_escaneamento_usuario = float(input("Digite o valor da velocidade de escaneamento em FPS: "))
print ("Houve alteração na variável inserida?", Velocidade_escaneamento != Velocidade_escaneamento_usuario)
media_imagem_usuario = int(input("Digite a média de imagens"))
print ("Houve alteração na variável inserida?", media_imagem != media_imagem_usuario)
tons_cinza_usuario = int(input("Digite os tons de cinzas em bits: "))
print ("Houve alteração na variável inserida?", tons_cinza != tons_cinza_usuario)
area_scaneada_usuario = float(input("Digite a área a ser escaneada em micro metros quadrados: "))
print ("Houve alteração na variável inserida?", area_scaneada != area_scaneada_usuario)
slices_usuario = int(input("Digite o valor do número de imagens que serão capturadas (Slice): "))
print ("Houve alteração na variável inserida?", slices != slices_usuario)
intervalo_usuario = float(input("Digite o valor do intervalo entre cada imagem em micro metro: "))
print ("Houve alteração na variável inserida?", intervalo != intervalo_usuario)
zoom_usuario = float(input("Digite o valor do zoom: "))
print ("Houve alteração na variável inserida?", zoom != zoom_usuario)

# Retorno ao usuário das informações que foram colocadas 
print ("\n## As informações de configuração inseridas pelo usuário foram: ##")
print ("\nA light path selecionada foi: ", light_path_usuario)
print ("Intensidade da luz: ", intensidade_luz_usuario)
print ("pixels da imagem: ",pixel_imagem_usuario)
print ("Velocidade de escaneamento: ", Velocidade_escaneamento_usuario)
print ("Média de imagens: ", media_imagem_usuario)
print ("Tons de cinza: ", tons_cinza_usuario)
print ("área a ser escaneada: ",area_scaneada_usuario)
print ("Slice: ", slices_usuario)
print ("Intervalo entre cada imagem: ", intervalo_usuario)
print ("Zoom: ", zoom_usuario)

# CALIBRAÇÃO HORIZONTAL DO EQUIPAMENTO
print ("\n## Para calibração horizontal do equipamento, será solicitado abaixo que digite a 1° e última letra do seu nome, o passo irá se repetir 10 vezes ##")

#1° rodada 
primeira_letra = input("Digite a 1° letra do seu nome: ")
ultima_letra = input ("Digite a última letra do seu nome: ")
print ("A primeira letra do seu nome é:",primeira_letra)
print ("A última letra do seu nome é:",ultima_letra)

#2° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#3° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#4° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#5° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#6° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#7° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#8° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#9° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

#10° rodada
primeira_letra_calicabrao = input ("Digite a 1° letra do seu nome: ")
print ("A informação foi digitada corretamente", primeira_letra == primeira_letra_calicabrao,".","O caractere pressionado foi:",primeira_letra_calicabrao)
ultima_letra_calibracao = input ("Digite a última letra do seu nome: ")
print ("A informação foi digitada corretamente", ultima_letra == ultima_letra_calibracao,".","O caractere pressionado foi:",ultima_letra_calibracao)

# CALIBRAÇÃO VERTICAL DO EQUIPAMENTO
print ("\n## Para calibração vertical do equipamento, será solicitado abaixo que digite a 2° e penúltima letra do seu nome, o passo irá se repetir 10 vezes ##")

#1° rodada 
segunda_letra = input("Digite a 2° letra do seu nome: ")
penultima_letra = input ("Digite a penúltima letra do seu nome: ")
print ("A segunda letra do seu nome é:",segunda_letra)
print ("A penúltima letra do seu nome é:",penultima_letra)

#2° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#3° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#4° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#5° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#6° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#7° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#8° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#9° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#10° rodada
segunda_letra_calicabrao = input ("Digite a 2° letra do seu nome: ")
print ("A informação foi digitada corretamente", segunda_letra == segunda_letra_calicabrao,".","O caractere pressionado foi:",segunda_letra_calicabrao)
penultima_letra_calibracao = input ("Digite a penúltima letra do seu nome: ")
print ("A informação foi digitada corretamente", penultima_letra == penultima_letra_calibracao,".","O caractere pressionado foi:",penultima_letra_calibracao)

#FINALIZAÇÃO DA CALIBRAÇÃO
print ("\n## FIM DA CALIBRAÇÃO DO EQUIPAMENTO ##")