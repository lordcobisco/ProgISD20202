#Este programa informa se o IMC esta entra as codições informadas abaixo. 
#As afirmações são classificadas com True e False 
peso = float(54)
altura = float(1.65)
imc = peso/(altura**2)

print ("Muito abaixo do peso:", imc<17)
print ("Abaixo do peso normal:", imc>=17 and imc<=18.5)
print ("Peso dentro do normal:", imc>18.5 and imc<=25)
print ("Muito abaixo do peso:", imc>25 and imc<=30)
print ("Muito abaixo do peso:", imc>30)
