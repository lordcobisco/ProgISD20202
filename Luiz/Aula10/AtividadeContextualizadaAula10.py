# Cadastro
print('=_' *20)
print('Seja Bem Vindo ao ISD, o seu Trabalho é muito Importante para Você mesmo!')
print('=_' *20)
print()
print()

print('Vamos Iniciar o Experimento de OPTGENÉTICA')
print('___' *20)
print('O animal já passou pela crirurgia de implante da Matriz com 32 canais, que estão funcionando corretamente. A Cânula e a Fibra Optica já estão implantados, em todos os animais, Teste e Controle.')
print('Animais já habituados para teste em Freezing, induzido a resposta do Medo!')
print('+++++' *20)
print('Iniciando o Experenimento: 1734/PROG_ISD_2020_02')
grupo = input('Digite a ID do Animal e qual Grupo: ')
print("Injentando em %s AAV-pEF1α-DIO-EYFP" %(grupo))
print('=-' *20)

# Escolhendo as CEPAS
srtgenetica1 = input('O animal é Knockin Fos-CreER T2? \n ')
srtnod = input('O anima é Knockout NOD1? \n ')

if(srtgenetica1 == "s" and  srtnod == "n"):
	print("Seguindo para AAV-pEF1α-DIO-EYFP\n")

if(srtgenetica1 == "n" and  srtnod == "n"):
	print("ERRO na Operação!\n")

if(srtgenetica1 == "n" and  srtnod == "s"):
	print("Você tem Certeza que quer Continuar?\n")

if(srtgenetica1 == "s" and  srtnod == "s"):
	print("Existe algo ERRADO, mas se quiser continuar é por sua conta!\n")

print('Ingetando o AAV-pEF1α-DIO-EYFP!')
print()
print('_____' *20)
print()
print('Para a próxima etapa Escolha os número para relacionar o animal ao Experimento Especifico:')
print('Animal Knowout NOD1 = 1')
print('Animal Knowout NOD2 = 2')
print('Anima knockin Fos-CreER T2  = 3')
print()
print('_____' *20)
print()

animal = int(input('Digite o número do Animal de acordo com a tabela Acima: '))
if animal < 3:
	print("Você está no Experimento ERRADO!\n")
	print("Essa Opção não Existe!!!")
else:
	print("Animal escolhido foi: ",animal)


acao = int(input("Para realizar AAV-pEF1α-DIO-EYFP, Digite 1. Se for para CaMKIIα Digite 2, eArch3 digite 3: "))
if(acao == 1):
	print("ACx e MGN em Fos-CREER irá atuar em ACx e MGN em Fos-CREE")
elif(acao==2):
	print("O CaMKIIα pode modificiar a expressão de AAV-pEF1α-DIO-EYFP ")
elif(acao==3):
	print("O eArch3 Precisa de ter sua ação limitada.")
else:
	print("Cada Ação irá ter Expressar um tipo de resultado")
print()
print('_____' *20)
print()
print('Próxima Etapa....')

# Calibrando
print('Pesquisador, o aparelho precisa ser calibrado! Escolha o tempo ideal para que o Experimento aconteça e os LEDs sejam acionados adequadamente.')
print('Irá iniciar uma contagem de 10 segundo. Aguarde!!!')
from time import sleep

def contador(i, f, p):
	print('_____' *20)
    
	print(f'Escolha três momentos o {i} até {f} de {p} em {p}')
	sleep(2.5)

	if i < f:
		cont = i
		while cont <= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont += p
		print('Gerando os Dados para Análise do Experimento')
	else:
		cont = 1
		while cont >= f:
			print(f' {cont} ', end='', flush=True)
			sleep(0.5)
			cont -= p			
		print('Gerando os Dados para Análise do Experimento')
contador(1, 10, 1)
print('=-' *20)
print('Agora o momento que a LED Azul deve acender, tendo um periodo de 2,5 segundos ligados')
ini = int(input("Início que o LED AZUL:  "))
fim = int(input("O teste deve terminar em quantos segundos: "))
pas = float(input("Qual intervalo quer irá Acender o LED AZUL: "))
contador(ini, fim, pas)

#Estimulos com LEDs

cor1 = input('LED Azul Funciona? \n ')
cor2 = input('LED Vermelho Funciona? \n ')

if(cor1 == "s" and  cor2== "n"):
   	print("Somente LED Azul Funciona.\n")

if(cor1 == "n" and  cor2 == "s"):
   	print("Somente LED Vermelho Funciona.\n")

if(cor1 == "s" and  cor2 == "s"):
    print("LEDs Azul e Vermelhor Funcionando. \n")

if(cor1 == "n" and  cor2 == "n"):
    print("Nenhum LED Está Funcionando, Recomendamos não prosseguir!\n")

from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('_____' *20)
print()
print('LED Azul Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *20)
print()
print('LED Azul Desligado')
from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('_____' *20)
print()
print('LED Vermelho Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *20)
print()
print('LED Vermelho Desligado')

from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('______' *20)
print()
print('LED Azul Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *20)
print()
print('LED Azul Desligado')
from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('______' *20)
print()
print('LED Vermelho Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *20)
print()
print('LED Vermelho Desligado')

from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('_____' *20)
print()
print('LED Azul Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *20)
print()
print('LED Azul Desligado')
from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('______' *20)
print()
print('LED Vermelho Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *20)
print()
print('LED Vermelho Desligado')
print()
print('_____' *20)
print()
print('Estabilizando o Animal')
from time import sleep
for cont in range(10, -1, -1):
	print(cont)
	sleep(0.5)
print('|||' *20)
print('Etapa Concluida!')

animal = dict()
animal['ID do Animal'] = str(input('ID do Animal: '))
animal['Pontuação do Experimento'] = float(input(f'Os freezings de {animal["ID do Animal"]} foram:'))
if animal['Pontuação do Experimento'] <= 3:
    animal['Score'] =  'Teste do Medo OK'
elif 3.1 <= animal ['Pontuação do Experimento'] >= 5:
    animal['Score'] = 'Inconclusivo'
else:
    animal['Score'] = 'Resultado Insignificante'
print('----' *20)
for k, v in animal.items():
	print(f'{k} é igual a: {v}') 

print('Processando todos os dados.... Dados Salvos!')
print('Para novo Experimento Reinicie todos os processo. Caso Contrário Desligue os Aparelhos, faça Acepsia e Vá trabalhar analisando os dados! ')
print('O ISD Agradece a Sua Publicação!')

print('RELATÓRIO DE CAPTAÇÃO DE ESTIMULO DOS SINAIS EMITIDO:')
import random
print('1°')
print('Relatório do Primeiro Estimulo:')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print('Sinais Captados nos Eletrodos   LED Azul: ')
n = random.sample(HD, 12)
n1 = random.sample(NacC, 4) 
n2 = random.sample(NacS, 4)
n3 = random.sample(HV, 3)
print ("Dados gerado HD:",n )
print("Dados Gerado NacC:", n1)
print("Dados Gerado NacS:" , n2)
print("Dados Gerado HV:" ,n3)
with open('Dados 1 do LED Azul.xls', 'w') as arquivo:
	for valor in n:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in n1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in n2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in n3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print()
print('Sinais Captados nos Eletrodos com  LED Vermelho: ')
nv = random.sample(HD, 12)
nv1 = random.sample(NacC, 4) 
nv2 = random.sample(NacS, 4)
nv3 = random.sample(HV, 3)
print ("Dados gerado HD:",nv )
print("Dados Gerado NacC:", nv1)
print("Dados Gerado NacS:" , nv2)
print("Dados Gerado HV:" ,nv3)
print()
with open('Dados 1 do LED Vermelho.xls', 'w') as arquivo:
	for valor in nv:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in nv1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')
#Parte 2

print('2°')
print('Relatório do Primeiro Estimulo:')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print('Sinais Captados nos Eletrodos   LED Azul: ')
n = random.sample(HD, 12)
n1 = random.sample(NacC, 4) 
n2 = random.sample(NacS, 4)
n3 = random.sample(HV, 3)
print ("Dados gerado HD:",n )
print("Dados Gerado NacC:", n1)
print("Dados Gerado NacS:" , n2)
print("Dados Gerado HV:" ,n3)
with open('Dados 2 do LED Azul.xls', 'w') as arquivo:
	for valor in n:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in n1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in n2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in n3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print()
print('Sinais Captados nos Eletrodos com  LED Vermelho: ')
nv = random.sample(HD, 12)
nv1 = random.sample(NacC, 4) 
nv2 = random.sample(NacS, 4)
nv3 = random.sample(HV, 3)
print ("Dados gerado HD:",nv )
print("Dados Gerado NacC:", nv1)
print("Dados Gerado NacS:" , nv2)
print("Dados Gerado HV:" ,nv3)
print()
with open('Dados 2 do LED Vermelho.xls', 'w') as arquivo:
	for valor in nv:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in nv1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')


# Parte 3
print('3°')
print('Relatório do Primeiro Estimulo:')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print('Sinais Captados nos Eletrodos   LED Azul: ')
n = random.sample(HD, 12)
n1 = random.sample(NacC, 4) 
n2 = random.sample(NacS, 4)
n3 = random.sample(HV, 3)
print ("Dados gerado HD:",n )
print("Dados Gerado NacC:", n1)
print("Dados Gerado NacS:" , n2)
print("Dados Gerado HV:" ,n3)
with open('Dados 3 do LED Azul.xls', 'w') as arquivo:
	for valor in n:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in n1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in n2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in n3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print()
print('Sinais Captados nos Eletrodos com  LED Vermelho: ')
nv = random.sample(HD, 12)
nv1 = random.sample(NacC, 4) 
nv2 = random.sample(NacS, 4)
nv3 = random.sample(HV, 3)
print ("Dados gerado HD:",nv )
print("Dados Gerado NacC:", nv1)
print("Dados Gerado NacS:" , nv2)
print("Dados Gerado HV:" ,nv3)
print()
with open('Dados 3 do LED Vermelho.xls', 'w') as arquivo:
	for valor in nv:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in nv1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')

# Parte 4
print('4°')
print('Relatório do Primeiro Estimulo:')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print('Sinais Captados nos Eletrodos   LED Azul: ')
n = random.sample(HD, 12)
n1 = random.sample(NacC, 4) 
n2 = random.sample(NacS, 4)
n3 = random.sample(HV, 3)
print ("Dados gerado HD:",n )
print("Dados Gerado NacC:", n1)
print("Dados Gerado NacS:" , n2)
print("Dados Gerado HV:" ,n3)
with open('Dados 4 do LED Azul.xls', 'w') as arquivo:
	for valor in n:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in n1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in n2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in n3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print()
print('Sinais Captados nos Eletrodos com  LED Vermelho: ')
nv = random.sample(HD, 12)
nv1 = random.sample(NacC, 4) 
nv2 = random.sample(NacS, 4)
nv3 = random.sample(HV, 3)
print ("Dados gerado HD:",nv )
print("Dados Gerado NacC:", nv1)
print("Dados Gerado NacS:" , nv2)
print("Dados Gerado HV:" ,nv3)
print()
with open('Dados 4 do LED Vermelho.xls', 'w') as arquivo:
	for valor in nv:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in nv1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')

# Parte 5 Final
print('5°')
print('Relatório do Primeiro Estimulo:')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print('Sinais Captados nos Eletrodos   LED Azul: ')
n = random.sample(HD, 12)
n1 = random.sample(NacC, 4) 
n2 = random.sample(NacS, 4)
n3 = random.sample(HV, 3)
print ("Dados gerado HD:",n )
print("Dados Gerado NacC:", n1)
print("Dados Gerado NacS:" , n2)
print("Dados Gerado HV:" ,n3)
with open('Dados 5 do LED Azul.xls', 'w') as arquivo:
	for valor in n:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in n1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in n2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in n3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')
HD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
NacC = [ 17, 18, 19, 20, 21, 21] 
NacS= [ 22, 23, 24, 25, 26, 27]
HV = [28, 29, 30, 31, 32,]
print()
print('Sinais Captados nos Eletrodos com  LED Vermelho: ')
nv = random.sample(HD, 12)
nv1 = random.sample(NacC, 4) 
nv2 = random.sample(NacS, 4)
nv3 = random.sample(HV, 3)
print ("Dados gerado HD:",nv )
print("Dados Gerado NacC:", nv1)
print("Dados Gerado NacS:" , nv2)
print("Dados Gerado HV:" ,nv3)
print()
with open('Dados 5 do LED Vermelho.xls', 'w') as arquivo:
	for valor in nv:
	  arquivo.write('HD: ')
	  arquivo.write(str(valor)+'\n')
	for valor in nv1:
		arquivo.write('NacC: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv2:
		arquivo.write('NacS: ')
		arquivo.write(str(valor)+'\n')
	for valor in nv3:
		arquivo.write('HV: ')
		arquivo.write(str(valor)+'\n')

print()
print('[HD = Hipocampo Dorsal, NacC = Nucléo Accumbens Core, NacS = Núcleo Accumbens Shell, HV = Hipocampo Ventral]')


