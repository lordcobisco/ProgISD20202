#Atividade 3 IMC



def imc(altura, peso):
	'''
	Para Calcular o IMC
  	'''
	return peso / altura**2


peso = float(input('Digite seu Peso (Kg): '))
altura = float(input('Digite sua Altura (m): '))

'''
  Peso: é uma variável, que precisa ser digitada pelo usuário, por isso usei input que também está convertida em decimal através da função float.
Consequentemente, usei a mesma regra para Altura, que também é outra variável.
'''

indice = imc(altura, peso)

'''
Como já defini as função de Peso e Altura, dentro do sistema criei uma função que  realize o calculo, sendo outra variável, no qual denominei IMC que receberá as informações de Peso e Altura do usuário. 
Dentro da função, atribuo para ela o nome de IMC, que coloco a formula do calculo.
Como retorno da função é informado o Índice de Massa do Corpo do usuário
'''

print('Seu IMC é: {:.2f}'.format(indice))

print('Muito abaixo do peso', indice < 17)
print('Abaixo do peso', 17 <= indice < 18.5)
print('Peso Normal', 18.5 <= indice < 25)
print('Acima do peso', 25 <= indice < 30)
print('Muito Acima do Peso', indice > 30)
print()

