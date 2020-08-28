Tipo_de_Lente = 1
Tipo_de_laser = 514
protecao = "aberta"
fluoroforo = "rodamina"
resolucao = "media"
filtro = 15
lapadaUv = "ligada"
ganho = 0
zoom = 10
campo = "escuro"

print("                                                   ")
print("Configuração do microscopio confocal de varredura a laser")
print("    Para proseguir insira as informações solicitadas")
print("                                                   ")
 
Tipo_de_Lente_desejada = int(input("Informe o Tipo de Lente desejada: "))
print("Houve alteração na variável inserida?: ",Tipo_de_Lente!=Tipo_de_Lente_desejada)
Tipo_de_laser_desejado = int(input("Informe o tipo de laser desejado: "))
print("Houve alteração na variável inserida?: ",Tipo_de_laser!=Tipo_de_laser_desejado)
protecao_desejado = input("Retire a tampa de proteção e informe se está aberta: ")
print("Houve alteração na variável inserida?: ",protecao!=protecao_desejado)
fluoroforo_desejado = input("Informe o fluoróforo desejado: ")
print("Houve alteração na variável inserida?: ",fluoroforo!=fluoroforo_desejado)
resolucao_desejada = input("Informe a qualidade de resolução desejada: ")
print("Houve alteração na variável inserida?: ",resolucao!=resolucao_desejada)
filtro_desejado = int(input("Informe o filtro desejado: "))
print("Houve alteração na variável inserida?: ",filtro!=filtro_desejado)
lampadaUv_desejada = input("Informe como deseja a lampada UV: ")
print("Houve alteração na variável inserida?: ",lapadaUv!=lampadaUv_desejada)
ganho_desejado = int(input("Informe a quantidade de ganho que deseja utilizar: "))
print("Houve alteração na variável inserida?: ",ganho!=ganho_desejado)
zoom_desejado = int(input("Informe a quantidade de zoom que deseja utilizar: "))
print("Houve alteração na variável inserida?: ",zoom!=zoom_desejado)
campo_desejado = input("informe qual campo deseja utilizar: ")
print("Houve alteração na variável inserida?: ",campo!=campo_desejado)

print("Configurações utilizadas pelo usuário: ")
print("Tipo de Lente: ",Tipo_de_Lente_desejada)
print("Tipo de Laser: ",Tipo_de_laser_desejado)
print("Protecao: ",protecao_desejado)
print("Fluoroforo: ",fluoroforo_desejado)
print("Resolução: ",resolucao_desejada)
print("Filtro: ",filtro_desejado)
print("LampadaUv: ",lampadaUv_desejada)
print("Ganho: ",ganho_desejado)
print("Zoom: ",zoom_desejado)
print("Campo: ",campo_desejado)

print(" ")
print("Para realizar a calibração horizontal insira os dados solicitados por um ciclo de 10x")
print(" ")

#1
LetraInicial_do_usuario = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial_do_usuario)
ultima_letra = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima_letra)
#2
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#3
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#4
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#5
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#6
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#7
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#8
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#9
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)
#10
LetraInicial = input("Para realizar a calibração horizontal digite a primeira letra do seu nome: ")
print("Caracter digitado é:",LetraInicial)
ultima = input("Para realizar a calibração horizontal digite a última letra do seu nome: ")
print("Caracter digitado é:",ultima)
print("Houve alteração? ",LetraInicial_do_usuario!=LetraInicial,ultima_letra!=ultima)

print(" ")
print(" Você realizou o ciclo de calibração Horizontal Realizada com suceesso! ")
print(" ")
print("Agora para realizar a calibração Vertical insira as informações solicitadas por um ciclo de 10x")
print(" ")
#1
segunda_letra_do_usuario = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda_letra_do_usuario)
penultima_letra= input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima_letra)
2#
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#3
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#4
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#5
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#6
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#7
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#8
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#9
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)
#10
segunda = input("Para realizar a calibração vertical digite a segunda letra do seu nome: ")
print("Caracter digitado é:",segunda)
penultima = input("Para realizar a calibração vertical digite a penúltima letra do seu nome: ")
print("Caracter digitado é:",penultima)
print("Houve alteração?: ",segunda!=segunda_letra_do_usuario,penultima!=penultima_letra)

print(" ")
print("Parabéns, a calibração foi realizada com sucesso")
print(" ")