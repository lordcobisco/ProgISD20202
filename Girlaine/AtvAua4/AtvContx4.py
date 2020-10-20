#Habituação

logicValue = int(input("Se o sagui retirou o marshmallow das barras (responda 0 para não e 1 para sim)"))

if(logicValue):
    print('O Sagui seguirá para a primeira etapa do treinamento')

#Treinamento

Barra1Apertada = int(input("O Sagui apertou a barra 1? (responda 0 para não e 1 para sim)"))
Barra2Apertada = int(input("O Sagui apertou a barra 2?(responda 0 para não e 1 para sim)"))

if(not Barra1Apertada or Barra2Apertada):
    print(' A Barra 1 não foi apertada ou a barra 2 foi apertada, entregar reconpensa')
elif(Barra1Apertada or not Barra2Apertada):
    print(' A Barra 1 foi apertada ou a barra 2 não foi apertada, entregar recompensa')
else:
    print('as duas Barras não foram apertadas, não entregar a recompensa')

# Regime de apriximaxão sucessiva 

BarraApertada = int(input("O Sagui manteve uma distância de 30 cm da barra? (responda 0 pra não e 1 para sim)"))

if(BarraApertada==1):
    print('Não entregar a recompensa')

else:
    print('O Sagui não se aproximou das barras')

BarraApertada = int(input("O Sagui manteve uma distância menor de 30 cm da barra? (responda 0 pra não e 1 para sim)"))

if(BarraApertada==1):
    print('Liberar 0,5ml de recompensa')
else:
    print('O Sagui não se aproximou das barras')

BarraApertada = int(input("O sagui tocou na barra 20 vezes? (responda 0 pra não e 1 para sim)"))
if(BarraApertada == '1'):
    print('proxima fase de teste')

Barra1Apertada = int(input("A barra foi tocada ao som1 ? (responda 0 para não e 1 para sim)"))
Barra2Apertada = int(input("A barra foi tocada ao som1 ? (responda 0 pra não e  para sim)"))

if(Barra1Apertada and not Barra2Apertada):
    print('liberar recompensa de 0,5ml')
elif(Barra2Apertada and not Barra1Apertada):
    print('Não liberar recompensa')
else:
    print('Não liberar recompensa')

Barra1Apertada = int(input("A barra foi tocada ao som2 ? (responda 0 para não e 1 para sim)"))
Barra2Apertada = int(input("A barra foi tocada ao som2 ? (responda 0 pra não e  para sim)"))

if(Barra1Apertada and not Barra2Apertada):
    print('Não liberar recompensa')
elif(Barra2Apertada and not Barra1Apertada):
    print('liberar recompensa de 0,5ml')
else:
    print('Não liberar recompensa')

BarraApertada = int(input("O sagui tocou na barra 50 vezes em 30 minutos? (responda 0 pra não e 1 para sim)"))
if(BarraApertada == '1'):
    print('proxima fase de teste')