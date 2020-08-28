print('Esse programa tem o intuito de automatizar o processo para treinamento em saguis')
print('em caixas de condicionamento. ')

habit = int(input("O animal está habituado ao experimento? (Responda 0 para não e 1 para sim)  "))
if(habit == 1):
    distAnimal = int(input('Digite a distância (em cm) do animal para o local de recompensa. '))
    distFixa = 30
    rec = 0
    distT = distFixa - distAnimal
    correto = 0
    toque = 0
    if (distT < distFixa):
        print('O animal se aproximou!')
        recT = rec + 0,5
        recT = rec
        animalToq = int(input('O animal tocou na barra? (Responda 0 para não e 1 para sim.) '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque)   
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 
        animalToq = int(input('O animal tocou na barra? '))
        if(animalToq == 1):
            toque = toque + 1
            print('Toques: ', toque) 

        if(toque == 20):
            print('O animal passou para a próxima etapa.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')
            print('O animal acertou ', correto, 'vezes.')

            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            print('O animal acertou ', correto, 'vezes.')
            som1 = int(input('O som apresentado foi o Phee? (Responda 0 para não e 1 para sim) '))
            animalToq1 = int(input('O animal tocou na barra esquerda? '))
            if(som1 == 1 and animalToq1 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

            som2 = int(input('O som apresentado foi o Trill? (Responda 0 para não e 1 para sim) '))
            animalToq2 = int(input('O animal tocou na barra direita? '))
            if(som2 == 1 and animalToq2 == 1):
                print('Recompensa liberada!')
                recT = rec + 0,5
                correto = correto + 1
            else: print('Recompensa não liberada.')

        else: print('Ainda não liberado para próxima etapa.')

    else: print('O animal não se aproximou. Tente novamente.')   



    print('Para prosseguir para a próxima etapa, o experimento necessita uma taxa de êxito >= 50 em um tempo menor que 30 minutos.')
    tempo = int(input('Indique o tempo em que foi realizado (em minutos). '))
    if(correto >= 50 and tempo <= 30):
        print('O experimento seguirá para a próxima etapa.')
    else: print('O experimento não seguirá para a próxima etapa. A taxa de êxito é: ', correto) 

else: print('Não é possível continuar com o experimento.')