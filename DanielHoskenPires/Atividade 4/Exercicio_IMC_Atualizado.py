#Exercício 1 - Cálculo de índice de massa corporal atualizado(IMC)

peso = float (input("Qual é o seu peso em 'Kg'? (Digite somente números)\n"))
altura = float (input("Qual é a sua altura em 'm'? (Digite somente números)\n"))
imc = peso/(altura**2)
print ("O seu IMC é de ", imc)

if (imc < 17):
    print ("Você está muito abaixo do peso, pois seu IMC é menor que 17!") 
elif (imc >= 17 and imc <= 18.5):
    print ("Você está abaixo do peso normal, pois seu IMC está entre 17 e 18.5!") 
elif (imc > 18.5 and imc <= 25):
    print ("Você está dentro do peso normal, pois seu IMC está entre 18.5 e 25!") 
elif (imc > 25 and imc <= 30):
    print ("Você está acima do peso normalpois seu IMC está entre 25 e 30!") 
elif (imc > 30):
    print ("Você está muito acima do peso, pois seu IMC está acima de 30!")
print ("Fim do programa")
