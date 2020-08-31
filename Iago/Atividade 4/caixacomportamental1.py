'''
Descrição
Requisito 1: Habituação
Se o animal está habituado, registrar em uma variável
Requisito 2: Regime de aproximações sucessivas
Iniciar a variável com 30cm
Se a variável de aproximação diminuiu (animal aproximou), liberar 0,5ml de rec
Se animal tocou na barra 20x, retornar que o experimento passou para a próxima etapa
Se o som1 foi emitido e o animal tocou na barra esquerda, liberar 0,5ml de rec
Caso contrário não liberar nada
Se o som2 foi emitido e o animal tocou na barra direita, liberar 0,5ml de rec
Caso contrário não liberar nada
Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.
'''

print("Primeira Fase: Habituação")
print("Realize a habituação do animal")

habituado = input("Animal está habituado? s/n: ")
if habituado == "s":
    print("Regime de aproximações sucessivas")
    distancia = input("Distância iniciada em 30cm, se distância reduzir digite valor: ")
    if distancia < '30':
        print("Recompensa liberada 0,5ml")
        tocou20x = input("Animal tocou na barra 20x? s/n: ")
        if tocou20x == "s":
            print("som 1 será emitido quando animal tocar na barra da esquerda ")
            som1 = input("Ouviu som 1 ser emitido? s/n: ")
            if som1 == "s":
                    print("som 1 foi emitido e a recompensa de 0,5ml foi liberada")
                    print("som 2 será emitido quando animal tocar na barra da direita")
                    som2 = input("Ouviu o som 2 ser emitido? s/n: ")
                    if som2 == "s":
                            print("Se o experimento foi realizado por 50x em 30 minutos você estará altorizado a ir para a próxima fase")
                        
                    if som2 == "n":   
                            print("Aguarde, ou realize novamente o experimento, recompensa não liberada")            
            if som1 == "n":
                     print("Aguarde, ou realize novamente o experimento, recompensa não liberada")
        if tocou20x == "n":
            print("conte as aproximações e tente novamente")    
    if distancia == "n":
        print("Retorne para regime de aproximações sucessivas e conte")
if habituado == "n":
    print("Retorne habituação do Animal")
