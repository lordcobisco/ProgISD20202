alt = float(input('Entre com sua altura: '))
peso = float(input('Entre com o seu peso: '))

imc = peso/(alt*alt)

varBool1 = imc <= 17
varBool2 = 17 < imc <= 18,5
varBool3 = 18.5 < imc <= 25
varBool4 = 25 < imc <= 30
varBool5 = imc > 30

print('Seu IMC é:', imc)
print('Muito abaixo do peso normal. (>17)', str(varBool1))
print('Abaixo do peso normal. (17 ~ 18.5)', str(varBool2))
print('Peso normal. (18.5 ~ 25)', str(varBool3))
print('Acima do peso normal. (25 ~ 30)', str(varBool4))
print('Muito acima do peso normal. (<30)', str(varBool5))