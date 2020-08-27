#Variáveis
laser = 630
abertura_circular = 75
quantidade_lentes = 8
aumento_lente = 50
resolucao = "alta"
quantidade_celulas_area = 600
coloracao = "ausente"
tamanho_lamina=10
tipo_tecido = "cerebro"
scanner = "galvanometro"

print ("Este programa tem o objetivo de calibrar o microscópio confocal")

#comparações
laser_usuario = input("Digite o comprimento de onda do laser que será utilizado: ")
print("Houve alteração na variável inserida?", str(laser) != laser_usuario)

abertura_circular_usuario = input("Digite o tamanho da abertura circular que deseja utilizar: ")
print("Houve alteração na variável inserida?", str(abertura_circular) != abertura_circular_usuario)

quantidade_lentes_usuario = input("Digite a quantidade de lentes que serão utilizadas: ")
print("Houve alteração na variável inserida?", str(quantidade_lentes) != quantidade_lentes_usuario)

aumento_lente_usuario = input("Digite o aumento que deseja utilizar: ")
print("Houve alteração na variável inserida?", str(aumento_lente) != aumento_lente_usuario)

resolucao_usuario = input("Digite qualitativamente a resolução que deseja utilizar: ")
print("Houve alteração na variável inserida?", str(resolucao) != resolucao_usuario)

quantidade_celulas_area_usuario = input("Digite quantidade de células por área que deseja obter: ")
print("Houve alteração na variável inserida?", str(quantidade_celulas_area) != quantidade_celulas_area_usuario)

coloracao_usuario = input("Digite a coloração que deseja utilizar: ")
print("Houve alteração na variável inserida?", str(coloracao) != coloracao_usuario)

tamanho_lamina_usuario = input("Digite o tamanho da lâmina que utilizará: ")
print("Houve alteração na variável inserida?", str(tamanho_lamina) != tamanho_lamina_usuario)

tipo_tecido_usuario = input("Digite o tipo de tecido que deseja utilizar: ")
print("Houve alteração na variável inserida?", str(tipo_tecido) != tipo_tecido_usuario)

scanner_usuario = input("Digite o tipo de scanner que utilizará: ")
print("Houve alteração na variável inserida?", str(scanner) != scanner_usuario)

#exibição das esolhas do usuário

print("As suas escolhas foram")
print("Laser: " + laser_usuario)
print("Abertura cirular: " + abertura_circular_usuario)
print("Quantidade de lentes " + quantidade_lentes_usuario)
print("Aumento das lentes " + aumento_lente_usuario)
print("Resolução da imagem " + resolucao_usuario)
print("Quantidade de céluas por área "+ quantidade_celulas_area_usuario)
print("Coloração " + coloracao_usuario)
print("Lâmina a ser utilizada " + tamanho_lamina_usuario)
print("Tipo de tecido " + tipo_tecido_usuario)
print("Tipo de scanner "+ scanner_usuario)

#calibração
print("Para calibrar o microscópio, precisaremos de algumas informações")

primeira_letra = str(input("Qual a primeira letra do seu nome? "))
ultima_letra = str(input("Qual a ultima letra do seu nome? "))

print("Digite 10x a primeira letra do seu nome e também a última letra do seu nome ")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 9 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 8 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 7 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 6 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 5 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 4 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 3 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 2 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou"  + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Agora só faltam 1 vezes")

primeira = input("Primeira letra do nome ")
ultima = input("Ultima letra do nome ")
print("Digitação correta? " + str(primeira_letra == primeira) + " Você digitou " + str(primeira))
print("Digitação correta? " + str(ultima_letra == ultima) + " Você digitou " + str(ultima))
print("Pronto. Plano horizontal calibrado")

print("Agora para calibrar a vertical, precisamores que digite a segunda letra do seu nome, bem como a penúltima")

segunda_letra = str(input("Qual a segunda letra do seu nome? "))
penultima_letra = str(input("Qual a penúltima letra do seu nome? "))

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 9 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 8 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 7 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 6 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 5 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 4 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 3 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 2 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Agora só faltam 1 vezes")

segunda = str(input("Segunda letra do nome "))
penultima = str(input("Penúltima letra do nome "))
print("Digitação correta? " + str(segunda_letra == segunda) + "Você digitou " + str(segunda))
print("Digitação correta? " + str(penultima_letra == penultima) + "Você digitou " + str(penultima))
print("Vertical calibrado com sucesso")

print("O microscópio foi calibrado com sucesso")
