# Calcaulando IMC
peso = 70 
altura = 1.8

IMC = peso / (altura)**2

print ("Seu IMC é: ", IMC)
print ("\n## CLASSIFICAÇÃO COM BASE NO IMC ##")

# Classificação com base no IMC
print ("\nMuito abaixo do peso", IMC<17)
print ("Abaixo do peso normal", IMC >= 17 and IMC < 18.5)
print ("Peso dentro do normal", IMC >= 18.5 and IMC <25)
print ("Acima do peso normal", IMC >= 25 and IMC < 30)
print ("Muito acima do peso", IMC >= 30)
