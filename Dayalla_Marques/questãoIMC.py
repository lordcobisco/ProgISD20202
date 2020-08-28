#EXERCÍCIO 01 - AULA 03
# Esse programa calcula o Índice de massa corporal de um indivíduo

print('Olá, usuário. Esse programa calcula o seu IMC.')
alturaIndividuo = float(input('Informe a sua altura: '))
pesoIndividuo = float(input('Infurme o seu peso: '))

indice = pesoIndividuo/(alturaIndividuo ** 2)

print('Seu imc é: ', indice)

print('Muito baixo do peso', indice < 17)
print('Abaixo do peso normal', 17 <= indice < 18.5)
print('Dentro do peso normal', 18.5 <= indice < 25)
print('Acima do peso normal', 25 <= indice < 30)
print('Muito acima do peso', indice > 30)


