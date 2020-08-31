
peso = float(input ("Digite o peso:"))
altura = float(input ("Digite a altura:"))
imc=peso/(altura*altura)
print ("O imc é de %s" %(imc))

print ("Muito abaixo do peso:", imc<17)
print ("Abaixo do peso normal:", imc>=17 and imc<=18.5)
print ("Peso dentro do normal:", imc>18.5 and imc<=25)
print ("Muito abaixo do peso:", imc>25 and imc<=30)
print ("Muito abaixo do peso:", imc>30)
