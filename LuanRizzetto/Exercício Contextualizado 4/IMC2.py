alt = float(input('Entre com sua altura: '))
peso = float(input('Entre com o seu peso: '))

imc = peso/(alt*alt)

if(imc <= 17):
    print('Seu IMC é:', imc)
    print('Muito abaixo do peso normal. (>17)')
elif(17 < imc <= 18.5):
    print('Seu IMC é:', imc)
    print('Abaixo do peso normal. (17 ~ 18.5)')
elif(18.5 < imc <= 25):
    print('Seu IMC é:', imc)
    print('Peso normal. (18.5 ~ 25)')
elif(25 < imc <= 30):
    print('Seu IMC é:', imc)    
    print('Acima do peso normal. (25 ~ 30)')
elif(imc > 30):
    print('Seu IMC é:', imc)
    print('Muito acima do peso normal. (<30)')