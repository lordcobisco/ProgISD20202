#Exercício IMC - Aula 4
#Apresentar na tela apenas o IMC e a faixa na qual o operador se encaixa

peso = float(input ("Qual o seu peso em quilogramas? "))
altura = float(input ("Qual a sua altura em metros? "))
imc = peso / (altura**2)
print("Como o seu peso é: %skg e a sua altura é: %sm, logo, o seu IMC será: %s\n" %(peso, altura, imc))

if(imc<17):
    print("Você está muito abaixo do peso.")
elif(17 <= imc < 18.5):
    print("Você está abaixo do peso normal.")
elif(18.5 <= imc < 25):
    print("O seu peso está dentro do normal.")
elif(25 <= imc < 30):
    print("Você está acima do peso normal.")
else:
    print("Você está muito acima do peso.")