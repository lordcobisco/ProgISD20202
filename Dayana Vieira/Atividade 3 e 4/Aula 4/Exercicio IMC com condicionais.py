#Este programa informa se o IMC esta entra as codições informadas abaixo. 
#As afirmações são classificadas com True e False 
peso = float(input ("Digite o peso:"))
altura = float(input ("Digite a altura:"))
imc=peso/(altura*altura)

if imc<=17:
    print ("Muito abaixo do peso, imc:", imc)
if imc>=17 and imc<=18.5:
    print ("Abaixo do peso normal, imc", imc)
if imc>18.5 and imc<=25:
    print ("Peso dentro do normal, imc:", imc)
if imc>25 and imc<=30: 
    print ("Muito abaixo do peso, imc:", imc)
if imc>30:
    print ("Muito abaixo do peso, imc:", imc)


 
print("Fim do programa!")