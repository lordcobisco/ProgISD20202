# Cáculo do IMC
peso = float(input("Qual o seu peso em Kg?"))
altura = float(input("Qual a sua altura em metros?"))

IMC = peso / (altura)**2

print ("Seu IMC é: ", IMC)
print ("\n## CLASSIFICAÇÃO COM BASE NO IMC ##")

# Classificação com base no IMC
if IMC<17:
    print ("Muito abaixo do peso")
elif IMC >= 17 and IMC < 18.5: 
    print ("Abaixo do peso normal")
elif IMC >= 18.5 and IMC <25: 
    print ("Peso dentro do normal")
elif IMC >= 25 and IMC < 30: 
    print ("Acima do peso normal")
else: #Poderia usar Elif IMC >= 30 também
    print ("Muito acima do peso")
