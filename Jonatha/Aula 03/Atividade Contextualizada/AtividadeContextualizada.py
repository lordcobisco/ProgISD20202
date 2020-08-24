# Devo inicializar a variável com valores defalut
resolucao = 100
tipoCelula = 'eucarionte'

print('Esse programa tem como objetivo receber dados para automatizar o uso do miscroscópio confocal.')

print('CONFIGURAÇÃO DO EQUIPAMENTO')
# Deve ter 10 inputs
temp = resolucao
resolucao = input('Informe a resolução da imagem desejada: ')
print('Houve alteração na variável inserida? ', resolucao != temp)

temp = tipoCelula
tipoCelula = input('Tipo de celula a ser escaneada : ')
print('Houve alteração na variável inserida? ', tipoCelula != temp)

print('As informações de configurações setadas pelo usuário são: ')
print('Resolução: ',resolucao)
print('Tipo de Celula: ', tipoCelula)
print('Area de Pesquisa: ', areaPesquisa)
print('Resolução: ',resolucao)
print('Resolução: ',resolucao)
print('Resolução: ',resolucao)
print('Resolução: ',resolucao)
print('Resolução: ', resolucao)
print('Resolução: ', resolucao)
print('Resolução: ', resolucao)


'''

a. Crie as variáveis necessárias para que o programa funcione corretamente.
b. Inicialize as variáveis com valores padrão adequados.
c. Crie uma pequena mensagem de apresentação do programa para realizar uma interface
com o usuário. Ex.: “Esse programa tem como objetivo receber dados para ...”
d. Solicite algumas informações necessárias para a configuração de um microscópio dessa
natureza. Buscar pelo menos 10 itens para essas informações de entrada. Ex.: resolução
da imagem desejada, tipo de célula a ser escaneada, faixa de iluminação necessária.
e - Ok. Para cada informação digitada, apresente na tela a seguinte mensagem: “Houve
alteração na variável inserida? ”. Após a mensagem, apresentar verdadeiro ou falso com
base no que foi digitado pelo usuário e o que estava armazenado na variável. Obs.: Não
deve ser utilizado if aqui.
f. Retorne ao usuário de forma organizada as informações que foram digitadas. Ex.: “As
informações de configurações setadas pelo usuário são: ...”
g. Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a
calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla
correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.
h. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
foi corretamente digitada e mostrar o caractere pressionado.
i. Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento
no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do
seu nome 10x e à penúltima letra do seu nome 10x.
j. Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação
foi corretamente digitada e mostrar o caractere pressionado.
k. Finalmente, o programa deverá apresentar na tela que houve o término da calibração do
sistema.
l. Para verificar que o programa está funcionando corretamente, execute-o colocando um
breakpoint na linha 15. Tire um print da tela mostrando a linha parada e as informações
armazenadas nas variáveis até então.
'''
