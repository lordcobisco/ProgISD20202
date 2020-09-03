#Método de discriminação de estímulos auditivos para primatas através do condicionamento operante

print("colocar animal no ambiente\n")

animalAmbientado = 0
while not animalAmbientado:
    animalAmbientado = int(input("O animal esta ambientado?"))
else:
    print("Tudo pronto.")

animalSom = 0
while not animalSom:
    animalSom = int(input("O animal ouviu o som?"))

else:
    print("animal respondeu ao estímulo.")
    print("Dê uma recompensa.")
