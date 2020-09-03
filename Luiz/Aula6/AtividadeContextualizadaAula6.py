#Iniciando os procedimentos das Anestesia -------
print('Esse procedimento deve ser realizado na sala de Preparo!')
print('É Proibido Realizar esse procedimento no Centro Cirurgico! Qualquer dúvida, pare e Chame a Veterinária Resposponsavel')
peso = float(input('Peso do Animal em Kg: '))
media1 = peso / 75
print(' A doser de de Ketamina será de:{}'.format(media1))
media2 = peso / 20
print(' A doser de de Xetamina será de:{}'.format(media2))
print() 
print('A partir desse momento o Animal deve ser mantido Isoflurano entre 1,5 a 5,0, a dosagem de Anestesico é do Tipo SEDAÇÃO LEVE')
print('Siga para o Centro Cirúrgico!')
print('_-'*50)
#------------ Bregma & Lambda ------------
valor = []
while True:
	valor.append(float(input('Digite sua Coordenada ML Estereotaxia: ')))
	resp = str(input('Desejar Continuar Digite sua Coordenada ML? [S/N] '))
	if resp in 'Nn':
            break
print(valor)
print('_#_' *50)	
valores = []	
while True:
	valores.append(float(input('Digite sua Coordenada do AP Estereotaxia: ')))
	resp = str(input('Desejar Continuar Digite sua Coordenada AP? [S/N] '))
	if resp in 'Nn':
            break
print(valores)
print('-_-' *50)
print(f'Essas são suas Coordenada ML e AP Estereotaxia: {valor} e {valores} são referentes as regiões para serem analisasdas.')
valores.sort
if 0 <=0.100 in valores:
	print('Angule o crânio na mesa Estereotaxia!')
else:
	print('Os valores Estão entre as Marcações de Bregma e Lambda')
print()
print(' \@*@/           \@*@/         \@*@/        '*5)
print('Lubrifique os Olhos do Animal com Solução Salina 0,09%')
print()

# Procedimento Cirúrgico

print('Como Protocolo Institucional Responda o questionário')
nome = input('Digite seu nome: ')
print("Olá %s, Aqui será também seu CheckList Cirúrgico" %(nome))


angulo = input("Qual o tipo de Animal: ")
print(" %s, estabilize o crânio" %(angulo))
print('Depdendendo do animal a Aste Auricular tem que ser posicionada em local diferente. Abaixo informe a localização do exata da Aste.')
core = input('Acomple bocal e astes das barras auriculares: ')
print("As Astes Auriculares estão posicionadas em  %s. Para a angulação em AP tenha 45°." %(core))

ligado2 = input("Introduza o aferidor cardiaco no esfíncter da ampola retal: ")
print(" %s, monitoramento da frequência Cardíaca está OK" %(angulo))
    
temp = '33° de temperatura'
cardio = '290 btm'
cama = '37° Placa'
print('Os Sinais vitais do animal: {0}, {1} e {2} Animal pronto'.format(temp, cardio, cama))

aviso1 = input('Ajustou a Ventilação ao Animal ')
print('Pronto para Iniciar a Cirurgia!')


informe = input('Será utiizado Canula? ' )
print('%s, Aguarde...' %(nome))

print('%s será utilizado canula' %(informe))

nome2 = input('Será utilizado matriz de eletro: ')
print(" %s Será utilizado" %(nome2))

print('Inicie os procedimentos para abertura das janelas para o implate da matriz de eletrodo do  %s' %(nome))
lam = 'H2O2'
print("Adcionando  %s, para melhorar a visualização da calota craniana" %(lam))

lam2 = input('Digite a numeração da broca: ')
print(" Iniciaremos os furos com broca %s" %(lam2))

print('Iniciaremos os proceimentos para implatar a matriz')
print('A Cirurgia só termina quando o Capacete estiver no Crânio...')
#Lembrete IMPORTANTE de Sinais Vitais
print()
print(' \@*@/           \@*@/         \@*@/        '*5)
print('Lubrifique os Olhos do Animal com Solução Salina 0,09%')
print()
print('Os Sinais vitais do animal: {0}, {1} e {2} Animal pronto'.format(angulo, cardio, cama))
print()
print()
print('Estamos finalizando a Cirurgia...')
print()
print()
print('Cirurgia Encerrada!')
print()
print()
print('Organize o Centro Cirúrgico!!!')
print()
print()
print('Agora Lave todo o Instrumental, seque-os e gruarde-os')
print()
print()
print('Bora Trabalhar...')