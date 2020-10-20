
#Habituação

def variaveis():
    """Essa Função agrupa todas as váriaveis""" 

habituacao = int(input('O rato está habituado? (Aperte 0 para não e 1 para sim)'))

if(habituacao):
    print('O rato está habituado')
if(not habituacao):
    print('O rato não está habituado')

#Regime de aproximações sucessivas

aproximacao = 30 
print('O rato aproximou 30 cm')

aproximacao = int(input('Quantos centimetros o rato aproximou? ( Variavél de aproximação for  que 30cm, gera recompensa)'))
if(aproximacao <30 ):
    print('Liberar 0,5ml de recompensa')
else:
    print('Não liberar recompensa')

contador = 0

toquebarra = input('O animal tocou na barra? (Responda n para não e s para sim)')
while(toquebarra == 's'):
    contador=contador +1
    print("Contador:",contador)
else:
    ( toquebarra == 'n')
    print ('Não computar no contador')


while(contador==20):
    print('O experimento passou para proxima etapa')
if (contador<20):
    print('O experimento não seguirá para próxima etapa')

som1emitido = input('O som 1 foi emitido? (Responda n para não e s para sim)')
toquebarraesquerda = input('O animal tocou na barra esquerda? (Responda n para não e s para sim)')
if(som1emitido == 's') and (toquebarraesquerda == 's'):
    print('Liberado 0,5ml de recompensa')
while(som1emitido == 'n') and (toquebarraesquerda == 's'):
    print('Sem recompensa')


experimento = int(input('O experimento foi realizado 50 vezes em 30 minutos? (Responda 0 para não e 1 para sim)'))
for realizado in experimento:
    print('O experimento seguirá para próxima fase')
else:
    print('O experimento seguirá nesta fase')






    
    




