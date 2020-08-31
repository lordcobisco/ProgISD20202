# Habituação

animalHabituado = '0'
Distancia = 30
Som1BarraEsquerda = '1'
TocounaBarra = '1'
x = 0
TempoMinutos = False


# PARA SABER SE O ANIMAL ESTÁ HABITUADO OU NÃO, DIGITAR 0 OU 1

print('Digite 0 para afirmativo e 1 para negativo')
variavel = input('O animal está habituado? ')

if(variavel == animalHabituado): 
    print('Sim. O animal está habituado!') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
     
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 19 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 18 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 17 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################

# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 16 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 15 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 14 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 13 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 12 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 11 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 10 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 9 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 8 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 7 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 6 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 5 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 
    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 4 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 3 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 2 VEZES PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.')   

    ############################################################################################
    # A PARTIR DESSA LINHA, OS PASSOS ANTERIORES SE REPETIRÃO 1 VEZ PARA QUE A VARIÁVEL x ATUALIZE SEU VALOR     
    ############################################################################################
# SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. 

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): 
            print('É HORA DE PASSAR PARA A PRÓXIMA FASE')
            
        else: 
            print('NÃO É HORA DE PASSAR PARA A PRÓXIMA FASE')    
            
    else: print('O animal não tocou na barra')

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    # SE A DISTÂNCIA FOR MENOR QUE A DISTÂNCIA INICIAL, O ANIMAL APROXIMOU E RECEBE RECOMPENSA

    dist = int(input('A distancia é: '))
    if (dist<Distancia): 
        print('O animal aproximou. Libere 0.5 ml de rec.')
    else: print ('A distância nao foi menor.')

    # CONTABILIZA QUANTAS VEZES O ANIMAL TOCOU NA BARRA. SE ELE TOCAR 20 VEZES, O EXPERIMENTO PASSA PARA A PRÓXIMA FASE

    TocounaBarra = input('Digite 0 para verdadeiro e 1 para falso. O animal tocou na barra? ')
    if (TocounaBarra == '0'): 
    
        x = x + 1
        print(x)
        if (x==20): print('O animal tocou na barra um total de 20 vezes. Próxima fase')
        else: print('O experimento continua')
    else: print('O animal não tocou na barra')

    # SE O SOM1 FOR EMITIDO E O ANIMAL TOCAR NA BARRA ESQUERDA, ELE SERÁ RECOMPENSADO

    
    Som1BarraEsquerda = input('O som 1 foi emitido e o animal tocou na barra esquerda? ')
    if(Som1BarraEsquerda == '0'): 
        print('Liberar 0.5 ml de rec.')
    else:   print('Não liberar nada.')

    # SE O SOM2 FOR EMITIDO E O ANIMAL TOCAR NA BARRA DIREITA, EE SERÁ RECOMPENSADO    

    Som2BarraDireita = input('O som 2 foi emitido e o animal tocou na barra direita? ')
    if(Som2BarraDireita == '0'):
        print('Liberar 0.5 ml de rec.')
    else:  print('Não liberar nada.') 

    TempoMinutos = input('A experiência foi feita 50 vezes em 30 minutos? ')
    if(TempoMinutos == True): 
        print('Passar para próxima fase do experimento')

    
    

else:  print('Fim do programa')
    


















