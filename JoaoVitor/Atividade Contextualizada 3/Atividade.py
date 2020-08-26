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

print("\nCALIBRAÇÃO HORIZONTAL\n PRESSIONE j 10 VEZES SEGUIDAS, DEPOIS o 10 VEZES SEGUIDAS")
print("\n===\nBOTAO j 10x\n")

calib_h_J0 = input("Digite j (1 de 10):")
b_calib_h_J0 = bool(calib_h_J0 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J0, "Caractere pressionado: ", calib_h_J0)

calib_h_J1 = input("Digite j (2 de 10):")
b_calib_h_J1 = bool(calib_h_J1 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J1, "Caractere pressionado: ", calib_h_J1)

calib_h_J2 = input("Digite j (3 de 10):")
b_calib_h_J2 = bool(calib_h_J2 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J2, "Caractere pressionado: ", calib_h_J2)

calib_h_J3 = input("Digite j (4 de 10):")
b_calib_h_J3 = bool(calib_h_J3 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J3, "Caractere pressionado: ", calib_h_J3)

calib_h_J4 = input("Digite j (5 de 10):")
b_calib_h_J4 = bool(calib_h_J4 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J4, "Caractere pressionado: ", calib_h_J4)

calib_h_J5 = input("Digite j (6 de 10):")
b_calib_h_J5 = bool(calib_h_J5 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J5, "Caractere pressionado: ", calib_h_J5)

calib_h_J6 = input("Digite j (7 de 10):")
b_calib_h_J6 = bool(calib_h_J6 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J6, "Caractere pressionado: ", calib_h_J6)

calib_h_J7 = input("Digite j (8 de 10):")
b_calib_h_J7 = bool(calib_h_J7 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J7, "Caractere pressionado: ", calib_h_J7)

calib_h_J8 = input("Digite j (9 de 10):")
b_calib_h_J8 = bool(calib_h_J8 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J8, "Caractere pressionado: ", calib_h_J8)

calib_h_J9 = input("Digite j (10 de 10):")
b_calib_h_J9 = bool(calib_h_J9 == "j")
print("O botão j foi pressionado corretamente?", b_calib_h_J9, "Caractere pressionado: ", calib_h_J9)

#################################################################################

print("\n===\nBOTAO o 10x\n")
calib_h_O0 = input("Digite o (1 de 10):")
b_calib_h_O0 = bool(calib_h_O0 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O0, "Caractere pressionado: ", calib_h_O0)

calib_h_O1 = input("Digite o (2 de 10):")
b_calib_h_O1 = bool(calib_h_O1 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O1, "Caractere pressionado: ", calib_h_O1)

calib_h_O2 = input("Digite o (3 de 10):")
b_calib_h_O2 = bool(calib_h_O2 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O2, "Caractere pressionado: ", calib_h_O2)

calib_h_O3 = input("Digite o (4 de 10):")
b_calib_h_O3 = bool(calib_h_O3 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O3, "Caractere pressionado: ", calib_h_O3)

calib_h_O4 = input("Digite o (5 de 10):")
b_calib_h_O4 = bool(calib_h_O4 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O4, "Caractere pressionado: ", calib_h_O4)

calib_h_O5 = input("Digite o (6 de 10):")
b_calib_h_O5 = bool(calib_h_O5 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O5, "Caractere pressionado: ", calib_h_O5)

calib_h_O6 = input("Digite o (7 de 10):")
b_calib_h_O6 = bool(calib_h_O6 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O6, "Caractere pressionado: ", calib_h_O6)

calib_h_O7 = input("Digite o (8 de 10):")
b_calib_h_O7 = bool(calib_h_O7 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O7, "Caractere pressionado: ", calib_h_O7)

calib_h_O8 = input("Digite o (9 de 10):")
b_calib_h_O8 = bool(calib_h_O8 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O8, "Caractere pressionado: ", calib_h_O8)

calib_h_O9 = input("Digite o (10 de 10):")
b_calib_h_O9 = bool(calib_h_O9 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O9, "Caractere pressionado: ", calib_h_O9)

falha_horizontal = bool(b_calib_h_J0 and b_calib_h_J1 and b_calib_h_J2 and b_calib_h_J3 and b_calib_h_J4 and b_calib_h_J5 and b_calib_h_J6 and b_calib_h_J7 and b_calib_h_J8 and b_calib_h_J9 and b_calib_h_O0 and b_calib_h_O1 and b_calib_h_O2 and b_calib_h_O3 and b_calib_h_O4 and b_calib_h_O5 and b_calib_h_O6 and b_calib_h_O7 and b_calib_h_O8 and b_calib_h_O9)

#######################################################################


print("\nCALIBRAÇÃO VERTICAL\n PRESSIONE o 10 VEZES SEGUIDAS, DEPOIS t 10 VEZES SEGUIDAS")
print("\n===\nBOTAO o 10x\n")

calib_h_O0 = input("Digite o (1 de 10):")
b_calib_h_O0 = bool(calib_h_O0 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O0, "Caractere pressionado: ", calib_h_O0)

calib_h_O1 = input("Digite o (2 de 10):")
b_calib_h_O1 = bool(calib_h_O1 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O1, "Caractere pressionado: ", calib_h_O1)

calib_h_O2 = input("Digite o (3 de 10):")
b_calib_h_O2 = bool(calib_h_O2 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O2, "Caractere pressionado: ", calib_h_O2)

calib_h_O3 = input("Digite o (4 de 10):")
b_calib_h_O3 = bool(calib_h_O3 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O3, "Caractere pressionado: ", calib_h_O3)

calib_h_O4 = input("Digite o (5 de 10):")
b_calib_h_O4 = bool(calib_h_O4 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O4, "Caractere pressionado: ", calib_h_O4)

calib_h_O5 = input("Digite o (6 de 10):")
b_calib_h_O5 = bool(calib_h_O5 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O5, "Caractere pressionado: ", calib_h_O5)

calib_h_O6 = input("Digite o (7 de 10):")
b_calib_h_O6 = bool(calib_h_O6 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O6, "Caractere pressionado: ", calib_h_O6)

calib_h_O7 = input("Digite o (8 de 10):")
b_calib_h_O7 = bool(calib_h_O7 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O7, "Caractere pressionado: ", calib_h_O7)

calib_h_O8 = input("Digite o (9 de 10):")
b_calib_h_O8 = bool(calib_h_O8 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O8, "Caractere pressionado: ", calib_h_O8)

calib_h_O9 = input("Digite o (10 de 10):")
b_calib_h_O9 = bool(calib_h_O9 == "o")
print("O botão o foi pressionado corretamente?", b_calib_h_O9, "Caractere pressionado: ", calib_h_O9)

#################################################################################

print("\n===\nBOTAO t 10x\n")
calib_h_T0 = input("Digite t (1 de 10):")
b_calib_h_T0 = bool(calib_h_T0 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T0, "Caractere pressionado: ", calib_h_T0)

calib_h_T1 = input("Digite t (2 de 10):")
b_calib_h_T1 = bool(calib_h_T1 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T1, "Caractere pressionado: ", calib_h_T1)

calib_h_T2 = input("Digite t (3 de 10):")
b_calib_h_T2 = bool(calib_h_T2 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T2, "Caractere pressionado: ", calib_h_T2)

calib_h_T3 = input("Digite t (4 de 10):")
b_calib_h_T3 = bool(calib_h_T3 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T3, "Caractere pressionado: ", calib_h_T3)

calib_h_T4 = input("Digite t (5 de 10):")
b_calib_h_T4 = bool(calib_h_T4 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T4, "Caractere pressionado: ", calib_h_T4)

calib_h_T5 = input("Digite t (6 de 10):")
b_calib_h_T5 = bool(calib_h_T5 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T5, "Caractere pressionado: ", calib_h_T5)

calib_h_T6 = input("Digite t (7 de 10):")
b_calib_h_T6 = bool(calib_h_T6 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T6, "Caractere pressionado: ", calib_h_T6)

calib_h_T7 = input("Digite t (8 de 10):")
b_calib_h_T7 = bool(calib_h_T7 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T7, "Caractere pressionado: ", calib_h_T7)

calib_h_T8 = input("Digite t (9 de 10):")
b_calib_h_T8 = bool(calib_h_T8 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T8, "Caractere pressionado: ", calib_h_T8)

calib_h_T9 = input("Digite t (10 de 10):")
b_calib_h_T9 = bool(calib_h_T9 == "t")
print("O botão t foi pressionado corretamente?", b_calib_h_T9, "Caractere pressionado: ", calib_h_J9)

falha_vertical = bool(b_calib_h_O0 and b_calib_h_O1 and b_calib_h_O2 and b_calib_h_O3 and b_calib_h_O4 and b_calib_h_O5 and b_calib_h_O6 and b_calib_h_O7 and b_calib_h_O8 and b_calib_h_O9 and b_calib_h_T0 and b_calib_h_T1 and b_calib_h_T2 and b_calib_h_T3 and b_calib_h_T4 and b_calib_h_T5 and b_calib_h_T6 and b_calib_h_T7 and b_calib_h_T8 and b_calib_h_T9)

print("\nCalibração horizontal realizada com sucesso?", falha_horizontal)
print("Calibração vertical realizada com sucesso?", falha_vertical)

print("Calibração do sistema finalizada.")
