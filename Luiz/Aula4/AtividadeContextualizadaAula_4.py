# Método de discriminação de estímulos auditivos para primatas através do condicionamento operante.
'''
Requisito 1: Habituação
    Se o animal está habituado, registrar em uma variável
Requisito 2: Regime de aproximações sucessivas
    Iniciar a variável com 30cm
    Se a variável de aproximação diminuiu (animal aproximou), liberar 0,5ml de recompensa
Requisito 3: Regime de aproximações sucessivas
    Se animal tocou na barra 20x, retornar que o experimento passou para a próxima etapa
Requisitos 4: Se o som1 foi emitido e o animal tocou na barra esquerda, liberar 0,5ml de recompensa
    Caso contrário não liberar nada
Requisitos 5: 
    Se o som2 foi emitido e o animal tocou na barra direita, liberar 0,5ml de recompensa
Caso contrário não liberar nada
Requisitos 6: Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.
'''
# REQUESITO 1
 
print('Vamos iniciar o Treinamento do seu Animal, Já está tudo pronto?')
nome = input('Digite o tipo de Animal que será testado: ')
print("Coloque o %s na Caixa de Habituação" %(nome))

logicValue = int(input('Feche a Caixa. Podemos Iniciar? (Responda 0 para Sim e 1 para Não)'))

if(logicValue) :
    print('Reinicie o processo, porque há algum erro!')



grupo = input('Iniciaremos a Habituação, INFORME o grupo de Animal: ')
print("Esse animal pertence ao Grupo %s," %(grupo))
tarefa = input('Digite o experimento que animal deve realizar: ')
print("O animal irá realizar a tarefa  %s. " %(tarefa))
ligado2 = input("Aperte ENTER para Iniciar.")
print(" Aguarde... a Habituação do %s, já vai iniciar" %(nome))
    

informe = input('Digite a Recompena que será entregue ao %s' %(nome))
print('%s, Aguarde...' %(informe))

print('Tudo Ok para inicar-mos')

botao1Apertado = int(input("O Animal apertou o batão 1?\n"))
botao2Apertado = int(input("O Animal apertou o batão 2?\n"))

if (botao1Apertado and not botao2Apertado):
	print("Foram adicionados 0,5ml de água")
elif (not botao1Apertado and botao2Apertado):
	print("Ruido Aleatório")
elif (botao1Apertado and botao2Apertado):
	print("Choque!")
else: 
	print("Nada foi Acionado! Verifique se o Animal está bem!")

print("Fim da 1ª Habituação. O Animal realizou 20 Tentativas")


botao1Apertado = int(input("o rato apertou o botão 1? (Responda 1 para não e 2 para sim)"))
botao2Apertado = int(input("o rato apertou o botão 2? (Responda 1 para não e 2 para sim)"))

if (botao1Apertado):
	print('O botão 1 foi apertado. A luz ligou. O animal Recebeu recompensa!')
elif (not botao1Apertado):
	print('O botão 1 não foi apertado. O Animal receberar uma carga de 0,5mA por 3 segundos.')
elif (botao2Apertado):
	print('O botão 2 Não foi apertado. A luz ligou. O animal Recebeu recompensa!')
elif (not botao2Apertado):
	print('O botão 2  foi apertado. O Animal receberar uma carga de 0,5mA por 3 segundos.') 

else:
	print('Nenhum Botão foi apertado. Animal não condicionado. Verifique se o Anima está bem!')
print('Analizando... Próxima Etapa>>>')


strLazy = input("O animal tocou na barra Direita?\1")
strInteligent = input("O animal tocou na barra Esquerda?!\1")


if(strLazy == "2" and strInteligent =="1"):
	print('A barra Direita foi apertado. A luz ligou. O animal Recebeu recompensa!')
if(strLazy == "1" and strInteligent == "1"):
	print('A barra Direita  não foi apertado. O Animal receberar uma carga de 0,4mA por 2 segundos.')
if(strLazy == "2" and strInteligent =="2"):
	print('A barra Esquerda Não foi apertado. A luz ligou. O animal Recebeu recompensa!')
if(strLazy == "1" and strInteligent =="2"):
	print('A barra Esquerda  foi apertado.O Animal receberar uma carga de 0,4mA por 2 segundos.') 
print("Analizando...")


print('Passaremos para outra fase do Experimento')

print('NESTA ETAPA O ANIMAL DEVE TOCAR NA BARRA DA ESQUERDA')


strLazy = input("O animal tocou na barra Esquerda?\1")
strInteligent = input("O animal tocou na barra Direita?!\1")


if(strLazy == "2" and strInteligent =="1"):
	print('A barra Esquerda foi apertado.  Ruido e o animal Recebeu recompensa!')
if(strLazy == "1" and strInteligent == "1"):
	print('A barra Esquerda  não foi apertado. Nada Aconteceu')
if(strLazy == "2" and strInteligent =="2"):
	print('A barra Direita Não foi apertado. Ruido. O animal Recebeu recompensa!')
if(strLazy == "1" and strInteligent =="2"):
	print('A barra Direita  foi apertado.Nada Aconteceu') 
else:
	print('O animal não realizou todas as tarefas, mais o tempo de 30 minutos foi excedido. Fim do Teste!')
print("2ª parte do Teste Concluido!")

logicValue = int(input('O animal explorou a caixa comportamental? (Responda 0 para Sim e 1 para Não)'))
if(logicValue) :
    print('O animal teve 30 minutos para realizar a tarefa. Por hoje é só')

botao1Apertado = int(input("O Animal apertou o batão 1?\n"))
botao2Apertado = int(input("O Animal se aproximou da Recompensa 2?\n"))

if (botao1Apertado and not botao2Apertado) :
	print("Foram adicionadosliberar 0,5ml de recompensa")
elif (not botao1Apertado and botao2Apertado) :
	print("Foi acionado o Ruido e o Choque")
elif (not botao1Apertado and botao2Apertado) :
	print("Foi acionado o Ruido e o Choque")
elif (botao1Apertado and  botao2Apertado) :
	print("Nada aconteceu")
elif (not botao1Apertado and  not botao2Apertado) :
	print("Nada aconteceu. Veja se o animal está bem!")

print("Fim do Experimento")