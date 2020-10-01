import math
#variaveis

laser_unit = 405 # laser em nm
laser_sec = 445 # laser secundário em nm
diascopic_detector = 400 # unidade em nm
pinhole = 6 # size
Image_bit_depth = 12 # bits
scanner = "galvonometro"
resolution = "64x64" # pixels
num_campo = 18 # numero de campo
resolucao_wave = 2 # resolução do comprimento de onda
bandwidth = 100 # largura de banda do comprimento de onda em nm

# mensagem inicial
print("Esse programa tem como objetivo receber dados para a configuração do microscopio confocal \n")

# variaveis setadas - comparação 
laser_unit2= input("Digite a unidade de laser a ser utilizada: ")
print("Houve alteração na variável inserida?", str(laser_unit)!= laser_unit2)

laser_sec2= input("Digite o tamanho do laser secundário: ")
print("Houve alteração na variável inserida?", str(laser_sec)!= laser_sec2)

diascopic_detector2= input("Informe a configuração do detector diascópico: ")
print("Houve alteração na variável inserida?", str(diascopic_detector) != diascopic_detector2)

pinhole2= input("Digite o diâmtro do pinhole: ")
print("Houve alteração na variável inserida?", str(pinhole)!= pinhole2)

Image_bit_depth2= input("Digite a profundidade de bits da imagem: ")
print("Houve alteração na variável inserida?", str(Image_bit_depth) != Image_bit_depth2)

scanner2= input("Digite o tipo do scanner a ser utilizado: ")
print("Houve alteração na variável inserida?", str(scanner) != scanner2)

resolution2= input("Informe a resolução da imagem: ")
print("Houve alteração na variável inserida?", str(resolution)!= resolution2)

num_campo2= input("Digite o número de campo: ")
print("Houve alteração na variável inserida?", str(num_campo)!= num_campo2)

resolucao_wave2= input("Insira a resolução do comprimento de onda: ")
print("Houve alteração na variável inserida?", str(resolucao_wave)!= resolucao_wave2)

bandwidth2= input("Insira a largura do comprimento de onda em nm: ")
print("Houve alteração na variável inserida?", str(bandwidth)!= bandwidth2)

# informações setadas - mostrar na tela

print("\n As informações de configurações setadas pelo usuário são:")
print("Unidade de laser: ",laser_unit2)
print("Tamanho do laser secundário: ", laser_sec2)
print("Detector diascópico utilizado:", diascopic_detector2)
print("Diâmetro do pinhole:", pinhole2)
print("Profundidade de bits da imagem:",Image_bit_depth2)
print("Scanner: ",scanner2)
print("Resolução da imagem:",resolution2)
print("Número de campo:",num_campo2)
print("Resolução do comprimento de onda",resolucao_wave2)
print("Largura do comprimento de onda:",bandwidth2)

#calibração horizontal 
primeiraletra = "cccccccccc"
ultimaletra = "aaaaaaaaaa"

print("\n Para a calibração na horizontal, informe a primeira (10x) e a ultima letra (10x) do seu nome.")

primeiraletra2= input("Insira a primeira letra do seu nome 10 vezes:")
print(str(primeiraletra)== primeiraletra2)
ultimaletra2= input("Insira a ultima letra do seu nome 10 vezes:")
print(str(ultimaletra)== ultimaletra2)

#calibração vertical

print("\n Para a calibração na vertical, informe a segunda e a penultima letra do seu nome 10x")

segundaletra = "aaaaaaaaaa"
penultimaletra = "nnnnnnnnnn"

segundaletra2= input("Insira a segunda letra do seu nome 10 vezes:")
print(str(segundaletra)== segundaletra2)

penultimaletra2= input("Insira a penultima letra do seu nome 10 vezes:")
print(str(penultimaletra)== penultimaletra2)

print("\n A calibração do microscópio foi finalizada com sucesso!")