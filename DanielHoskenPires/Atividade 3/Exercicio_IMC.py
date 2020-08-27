#Exercício 1 - Cálculo de índice de massa corporal (IMC)

peso = float (input("Qual é o seu peso em 'Kg'? (Digite somente números)\n"))
altura = float (input("Qual é a sua altura em 'm'? (Digite somente números)\n"))
imc = peso/(altura**2)
print ("O seu IMC é de ", imc)

print ("Você está muito abaixo do peso:",(imc < 17)) 
print ("Você está abaixo do peso normal:",(imc >= 17 and imc <= 18.5)) 
print ("Você está dentro do peso normal:",(imc > 18.5 and imc <= 25)) 
print ("Você está acima do peso normal:",(imc > 25 and imc <= 30)) 
print ("Você está muito acima do peso:",(imc > 30))