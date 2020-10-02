'''
Com base na lista de requisitos apresentada, elabore um programa em python que simule o comportamento desse sistema. O programa deve conter:
a)	Entrada e Saída de dados
b)	Estrutura de decisão
c)	Estrutura de repetição
d)	Funções
e)	Classes
f)	Pelo menos um dos 3 Lista, Tupla ou Dicionário
g)	Temporização (Esse item deve ser pesquisado, ou seja, buscar uma solução na rede)
'''
print('=_' *50)
print('Seja Bem Vindo ao ISD, o seu Trabalho é muito Importante para Você mesmo!')
print('=_' *50)
print()
print()

print('Vamos Iniciar o Experimento de OPTGENÉTICA')
print('___' *50)
print('O animal já passou pela crirurgia de implante da Matriz com 32 canais, que estão funcionando corretamente. A Cânula e a Fibra Optica já estão implantados, em todos os animais, Teste e Controle.')
print('Animais já habituados para teste em Freezing, induzido a resposta do Medo!')
print('+++++' *50)
print('Iniciando o Experenimento: 1734/PROG_ISD_2020_02')
grupo = input('Digite a ID do Animal e qual Grupo: ')
print("Injentando em %s AAV-pEF1α-DIO-EYFP" %(grupo))
print('=-' *50)

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
print('_____' *50)
print()
print('Para a próxima etapa Escolha os número para relacionar o animal ao Experimento Especifico:')
print('Animal Knowout NOD1 = 1')
print('Animal Knowout NOD2 = 2')
print('Anima knockin Fos-CreER T2  = 3')
print()
print('_____' *50)
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
print('_____' *50)
print()
print('Próxima Etapa....')

# Calibrando
print('Pesquisador, o aparelho precisa ser calibrado! Escolha o tempo ideal para que o Experimento aconteça e os LEDs sejam acionados adequadamente.')
print('Irá iniciar uma contagem de 10 segundo. Aguarde!!!')
from time import sleep

def contador(i, f, p):
	print('_____' *50)
    
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

#Estimolos com LEDs

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
print('_____' *50)
print()
print('LED Azul Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *50)
print()
print('LED Azul Desligado')
from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('_____' *50)
print()
print('LED Vermelho Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *50)
print()
print('LED Vermelho Desligado')

from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('______' *50)
print()
print('LED Azul Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *50)
print()
print('LED Azul Desligado')
from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('______' *50)
print()
print('LED Vermelho Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *50)
print()
print('LED Vermelho Desligado')

from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('_____' *50)
print()
print('LED Azul Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *50)
print()
print('LED Azul Desligado')
from time import sleep
for cont in range(5, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('______' *50)
print()
print('LED Vermelho Acesso')
from time import sleep
for cont in range(2, -1, -1):
     print(cont)
     sleep(0.5)
print()
print('=-=-=-' *50)
print()
print('LED Vermelho Desligado')
print()
print('_____' *50)
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
print('----' *30)
for k, v in animal.items():
	print(f'{k} é igual a: {v}') 

print('Processando todos os dados.... Dados Salvos!')
print('Para novo Experimento Reinicie todos os processo. Caso Contrário Desligue os Aparelhos, faça Acepsia e Vá trabalhar analisando os dados! ')
print('O ISD Agradece a Sua Publicação!')

