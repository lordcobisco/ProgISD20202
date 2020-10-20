#Exercício contextualizado 3 - Técnica de microscopia confocal de varredura à laser 
#Numero 2 - Letra a) e letra b)
#varString = "Nome", "Matricula", , "conversao", "ImagemComputador2D", "ImagemComputador3D", "ImagemComputadorMovimento"
TipoCelula = "Nenhuma"
Lente = 0
ResolucaoImagem = 0
FaixaIluminacao = 0
VarreduraAmostraX = 0
VarreduraAmostraY = 0
Intensidade = 0
Foco = 0
ComprimentoOnda = 0
FeixeLaiser = False
LigarMicroscopio = False
LigarArgonio = False 
LigarFluorescencia = False
Resete = False
AtualizazaoSistema = False

def alteracaovar():
    print('Houve alteração na variável inserida?')

#Letra c)
print ("Esse programa referente a 'Técnica de microscopia confocal de varredura à laser',\ntem como objetivo a interação com o pesquisador, possibilitando receber e \nretornar dados. SEJA BEM VINDA(O)!!!")
#Letra d) e e)
Nome = (input("Qual é o seu nome completo?\n"))

Matricula = (input("Qual é o seu número de matrícula?\n"))

Comparativo = LigarMicroscopio
LigarMicroscopio = bool (input("Deseja ligar o microscópio? (Aperte qualquer tecla para ligar ou enter para manter desligado) \n" ))
alteracaovar()
print(LigarMicroscopio != Comparativo)

Comparativo = ResolucaoImagem
ResolucaoImagem = int (input("Qual a resolução de imagem desejada de 1 a 5, sendo 1 a menor resolução e 5 a maior resolução?\n"))
alteracaovar()
print(ResolucaoImagem != Comparativo)

Comparativo = TipoCelula
TipoCelula =  (input("Qual é o típo de célula a ser analisada? \n"))
alteracaovar()
print(TipoCelula != Comparativo)

Comparativo = FaixaIluminacao
FaixaIluminacao = float (input("Qual a faixa de iluminação desejada de 1 a 7, sendo 1 a menor faixa e 7 a maior faixa?\n"))
alteracaovar()
print(FaixaIluminacao != Comparativo)

Comparativo = Intensidade
Intensidade = float (input("Qual a intensidade desejada de 1 a 5, sendo 1 a menor intensidade e 5 a maior intensidade?\n"))
alteracaovar()
print(Intensidade != Comparativo)

Comparativo = Foco
Foco = float (input("Qual foco desejado de 1 a 10, sendo 1 o menor foco e 10 o maior foco?\n"))

print('Houve alteração na variável inserida? ', Foco != Comparativo)

Comparativo = ComprimentoOnda
ComprimentoOnda = float (input("Qual o comprimento de onda desejado de 1 a 3, sendo 1 o menor comprimento e 10 o maior comprimento?\n"))
alteracaovar()
print(ComprimentoOnda != Comparativo)

Comparativo = False
FeixeLaiser = bool (input("Deseja ligar o feixe de laser? (Aperte qualquer tecla para ligar ou enter para manter desligado) \n" ))
alteracaovar()
print(FeixeLaiser != Comparativo)

Comparativo = False
LigarFluorecencia = bool (input("Deseja ligar a fluorescência? (Aperte qualquer tecla para ligar ou enter para manter desligado) \n" ))
alteracaovar()
print(LigarFluorecencia != Comparativo)

Comparativo = False
LigarArgonio = bool (input("Deseja ligar o Argônio? (Aperte qualquer tecla para ligar ou enter para manter desligado) \n" ))
alteracaovar()
print(LigarArgonio != Comparativo)

Comparativo = False
AtualizacaoSistema = bool (input("Deseja buscar atualização do sistema? (Aperte qualquer tecla para atualizar ou enter para manter como está) \n" ))
alteracaovar()
print(AtualizacaoSistema != Comparativo)

# Letra f)
print("\nAs informações de configuração setadas pelo usuário são: \n")
print ("O nome do usuário é: ", Nome)
print ("A matrícula do usuário é: ", Matricula)
print ("Microscópio ligado: ", LigarMicroscopio)
print ("A resolução de imagem está no nível: ", ResolucaoImagem)
print ("A célula escolhida foi: ", TipoCelula)
print ("A iluminação está no nível: ", FaixaIluminacao)
print ("A intensidade está no nível: ", Intensidade)
print ("O foco está no nível: ", Foco)
print ("O comprimento de onda está no nível: ", ComprimentoOnda)
print ("O feixe de laiser está ligado: ", FeixeLaiser)
print ("O fluorecencia está ligada: ", LigarFluorecencia)
print ("O Argônio está ligado: ", LigarArgonio)
print ("O sistema será atualizado agora: ", AtualizazaoSistema)

# Calibração horizontal do equipamento Letra g) e h)
print ("Nesse momento, vamos fazer a calibração horizontal de seu equipamento...")

CalibHorizontal1 = input("Digite a primeira letra de seu nome por 10x: \n")
print ("A tecla informada foi corretamente acionada, sendo ela: ", CalibHorizontal1)
CalibHorizontal2 = input("Digite a última letra de seu nome por 10x: \n")
print ("A tecla informada foi corretamente acionada, sendo ela: ", CalibHorizontal2)

# Calibração vertical do equipamento Letra i) e j)
print ("Nesse momento, vamos fazer a calibração vertical de seu equipamento...")

CalibVertical1 = input("Digite a segunda letra de seu nome por 10x: \n")
print ("A tecla informada foi corretamente acionada, sendo ela: ", CalibVertical1)
CalibVertical2 = input("Digite a penultima letra de seu nome por 10x: \n")
print ("A tecla informada foi corretamente acionada, sendo ela: ", CalibVertical2)

#Mensagem de calibração final Letra k)
print ("O equipamento foi devidamente calibrado!\n")