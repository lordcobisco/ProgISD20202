laser = 351 #largura padrao em nm, default 351
argonio_dose = 0 #dose de argonio, default 0
lamina_pos = False #lamina posicionada, default false
lente_obj = 10 #lente objetiva, padrao 10x
foco = 50
anticorpos = ' ' #tipo dos anticorpos secundarios, default string vazia
luz_vizivel = True #luz visível, bool
potencia_lasers = 7 #recomendado entre 7 a 10, default 7
pinhole = 0.5 #entre 0.5 a 5, default 0.5
ganho = 1
digital_offset = 0 #assume valores negativos
digital_gain = 1 #valores positivos
resolucao = "1024x768" #default
velocidade_amostragem = 2 #default 2

print("Assistente de seleção de parâmetros para operação em microscópio confocal. Siga as instruções de entrada contida nas mensagens:\n")

laser_buff = int(input("Selecione o comprimento de onda do laser utilizado em nm (351, 364, 458, 477, 488, 514, 543 e 633). Padrão em 351nm \n"))
print("Houve alteração na variável inserida?", laser != laser_buff)
laser = laser_buff

argonio_onoff = bool(laser == 458 or laser == 488 or laser == 514) #interruptor de argonio, true se o laser for 458mm, 488mm e 514mm

print("Entrada de argônio habilitada? (Positivo para laser em 458, 488 ou 514nm): ", argonio_onoff)

argonio_dose_buff = int(input("Caso o interruptor de argônio esteja habilitado, selecione a abertura do dosador em uma porcentagem entre 1 e 100. Caso esteja desabilitado, digite 0. (valores acima de 100 serão considerados 100):"))
print("Houve alteração na variável inserida?", argonio_dose != argonio_dose_buff)

lamina_pos_buff = bool(input("A lamina para analise esta posicionada corretamente? Digite 'sim' para sim, ou não insira nenhum dado e pressione enter caso não: "))
print("Houve alteração na variável inserida?", lamina_pos != lamina_pos_buff)

lente_obj_buff = int(input ("Digite o valor de zoom da lente objetiva desejado (padrão: 10): "))
print("Houve alteração na variável inserida?", lente_obj != lente_obj_buff)

foco_buff = int(input ("Digite o valor de foco desejado (padrão 50): "))
print("Houve alteração na variável inserida?", foco != foco_buff)

anticorpos_buff = input("Digite quais anticorpos secundários deseja (por padrão, desabilitado): ")
print("Houve alteração na variável inserida?", anticorpos != anticorpos_buff)

luz_vizivel_buff = bool(input("Deseja iluminar com luz visível? Digite 'sim' para sim, ou não insira nenhum dado e pressione enter caso não (padrão True): "))
print("Houve alteração na variável inserida?", luz_vizivel != luz_vizivel_buff)

potencia_lasers_buff = int(input("Digite a potência do laser desejada (padrão 7): "))
print("Houve alteração na variável inserida?", potencia_lasers != potencia_lasers_buff)

pinhole_buff = float(input("Digite a abertura do pintfloat desejada (padrão 0.5): "))
print("Houve alteração na variável inserida?", pinhole != pinhole_buff)

ganho_buff = int(input("Digite o ganho desejado no amplificador de entrada (padrão 1): "))
print("Houve alteração na variável inserida?", ganho != ganho_buff)

digital_offset_buff = int(input("Digite o offset digital desejado (padrão 0): "))
print("Houve alteração na variável inserida?", digital_offset != digital_offset_buff)

digital_gain_buff = int(input("Digite o valor de ganho digital desejado (padrão 1): "))
print("Houve alteração na variável inserida?", digital_gain != digital_gain_buff)

resolucao_buff = input("Digite a resolução desejada no formato LARGURAxALTURA (padrão 1024x768): ")
print("Houve alteração na variável inserida?", resolucao != resolucao_buff)

velocidade_amostragem_buff = int(input("Digite a velocidade de amostragem desejada (padrão 2)"))
print("Houve alteração na variável inserida?", velocidade_amostragem != velocidade_amostragem_buff)

print("\nSumário das configurações do sistema: \n")
print("Comprimento de onda do laser: ", laser, "nm")
print("Entrada de argônio habilidada ", argonio_onoff, ", com a seguinte dosagem: ", argonio_dose_buff, "%")
print("A lâmina encontra-se posicionada? ", lamina_pos_buff)
print("Lente objetiva selecionada: ", lente_obj_buff, "x")
print("Foco selecionado: ", foco_buff)
print("Anticorpos secundários selecionados: ", anticorpos_buff)
print("O material está iluminado por luz visível? ", luz_vizivel_buff)
print("Potência dos lasers em: ", potencia_lasers_buff)
print("Abertura do pinhole: ", pinhole_buff, "AU")
print("Ganho do amplificador de entrada: ", ganho_buff, "x")
print("Offset digital em: ", digital_offset_buff)
print("Ganho digital em: ", digital_gain_buff, "x")
print("Resolução de captura: ", resolucao_buff, " pixels")
print("Velocidade de amostragem em: ", velocidade_amostragem_buff, " um^2/s")