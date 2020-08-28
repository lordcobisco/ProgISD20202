
#Inicialização das variáveis com valores padrão adequados
celula = 'neurônio'
tipoLaser = 458
intensidaLaser = 0
resolucao = 40
tempoArgonioEmMinutos = 5
ligarLaser = '0'
diametroLaser = 9
salvarArquivosdeImagens = '0' 
ligarEquipamento = '0'
ligarArgonio = '0'
print('Olá, usuário! O programa a seguir objetiva receber dados e utilizá-los nas técnicas de microscopia confocal')
variavel = celula
celula = input('Qual o tipo de célula? ')
print('Houve alteração no tipo de célula? ', variavel != celula)

variavel = tipoLaser
tipoLaser = input('Qual o tipo de laser que você deseja usar? ')
print('Houve alteração no tipo de laser', variavel != tipoLaser)

variavel = intensidaLaser
intensidaLaser = input('você deseja ajustar a intensidade desse laser para quanto? ')
print('Houve alteração na intensidade do laser', variavel!=intensidaLaser)

variavel = resolucao
resolucao = input('Qual o tipo de resolucao que você deseja? ')
print('Houve alteração no tipo de resolução', variavel != resolucao)

variavel = tempoArgonioEmMinutos
tempoArgonioEmMinutos = input('Digite o tempo de argônio desejado: ')
print('Houve alteração no tempo de argônio? ', variavel != tempoArgonioEmMinutos)

variavel = ligarLaser
ligarLaser = input('Voce deseja ligar o laser? Digite 1 para ligar')
print('Houve alteração na ligação do laser? ', variavel != ligarLaser )

variavel = diametroLaser
diametroLaser = input('Qual o diametro que você deseja? ')
print('Houve alteração no diâmetro do laser? ', variavel != diametroLaser)

variavel = ligarArgonio 
ligarArgonio = input('Você deseja ligar o argônio? Digite 1 para ligar ')
print('Houve alteração na ligação do argônio? ', variavel != ligarArgonio )

variavel = ligarEquipamento
ligarEquipamento = input('Você deseja ligar o equipamento? Digite 1 para ligar ')
print( 'Houve alteração na ligação do equipamento? ', variavel != ligarEquipamento)

variavel = salvarArquivosdeImagens
salvarArquivosdeImagens = input('Você deseja salvar os arquivos? Digite 1 para salvar ')
print('O arquivo será salvo? ', variavel != salvarArquivosdeImagens)

print('Tipo de célula: ', celula)
print('Tipo de laser utilizado: ', tipoLaser)
print('Intensidade do laser: ', intensidaLaser)
print('Resolução', resolucao)
print('Tempo de argônio em minutos: ', tempoArgonioEmMinutos)
print('Ligar laser', ligarLaser)
print('Diametro o laser', diametroLaser)
print('Ligar argônio', ligarArgonio)
print('Ligar equipamento', ligarEquipamento)
print('Salvar arquivos', salvarArquivosdeImagens)

# Calibrando o equipamento 
# Calibração horizontal (O usuário deve apertar 10x a primeira letra de seu nome e 10x  última letra de seu nome)
# Haverá uma comparação entre a letra digitada e a letra do nome que o usuário informou
# Primeiro será feito pra primeira letra do nome 10x e depois será feito pra última letra do nome 10x


nomeUsuario = input('Digite seu nome: ')
print(nomeUsuario.lower())

# Primeira letra do nome
print(nomeUsuario,', você irá digitar a primeira e a última letra do seu nome 10 vezes para calibrar o equipamento horizontalmente.')

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())

horiz = input('A primeira letra do seu nome é: ') # Primeira letra do nome
print(horiz == nomeUsuario[0].lower())

horiz2 = input('A última letra do seu nome é: ') # última letra do nome
print(horiz2 == nomeUsuario[-1].lower())
    


# Calibração vertical do equipamento
# Para calibrar verticalmente o equipamento o usuário terá de digitar a segunda e a penúltima letra do nome dele 10x 

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

vert = input('A segunda letra do seu nome é: ') # segunda letra do nome
print(vert == nomeUsuario[1].lower())

vert2 = input('A penúltima letra do seu nome é: ') # penúltima letra do nome
print(vert2 == nomeUsuario[-2].lower())

print('Obrigada,',nomeUsuario,', você já pode utilizar o equipamento.')