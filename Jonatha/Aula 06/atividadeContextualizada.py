# Atividade Contextalizada 06
from os import system
system('clear')

print('Bem vindo(a) à cirurgia esterotáxica.')
print('Este programa vai automatizar o procedimento.')
print('Por favor, observe atentamente as perguntas e preencha os parâmetros conforme solicitado.')
resposta = input('Está pronto para começar [sim]?  ')

while(resposta.lower() != 'sim'):
    resposta = input(
        "\nNão entendi sua resposta. Digite 'sim' para dar inicio ao procedimento: ")

print('\nVamos iniciar!')
farmaco = dict()
animal = dict()
resposta = ''

# PROCEDIMENTO 1
while(resposta.lower() != 'sim'):
    farmaco['nome'] = input('Digite o fármaco que será utilizado: ')
    farmaco['quantidade'] = int(input('Quantidade (ml): '))
    animal['peso'] = float(input('Digite o peso do animal: '))
    resposta = input('A quantidade de ' + str(farmaco['quantidade'])+'ml de ' + str(
        farmaco['nome'])+' é adequada para um animal de '+str(animal['peso'])+'gramas? ')
    if(resposta != 'sim'):
        print('Informe os parâmetros novamente...\n')
# FIM DO PROCEDIMENTO 1

# PROCEDIMENTO 2
resposta = ''
while(True):
  resposta = input('\nO anestésico fez efeito? ')
  if(resposta.lower()=='sim'):
    break
  print('Vamos aguardar...')

print('\nPosicione o animal no esterotáxico.')
while(True):
  resposta = input('O animal está posicionado corretamente? ')
  if(resposta.lower()=='sim'):
    break
  print('Reposicione...')
# FIM DO PROCEDIMENTO 2
