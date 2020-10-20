import csv

def eq_imc (x,y):
    x = float(x)
    y = float(y)
    calc_imc = (x)/(y**2)
    return calc_imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = eq_imc(peso, altura)

salvar = input("Como deseja salvar os dados?")

if salvar == 'csv':
    with open('IMC.csv',  'w', newline = '') as csvfile:
        wr = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting =  csv.QUOTE_MINIMAL)

        if imc <17: 
            print( "Muito abaixo do peso, ", round (imc,2) )
            wr.writerows(['Muito abaixo do peso: ']+ [str(imc)])
        elif imc >= 17 and imc <18.5:
            print("Abaixo do peso normal, " , round (imc,2))
            wr.writerows(['Abaixo do peso normal: ']+ [str(imc)])
        elif imc >= 18.5 and imc < 25.0:
            print("Peso dentro do normal, ", round (imc,2))
            wr.writerows(['Peso dentro do normal: '] + [str(imc)])
        elif imc >= 25 and imc < 30:
            print("Acima do peso normal, ", round (imc,2))
            wr.writerows(['Acima do peso normal, ']+ [str(imc)])
        else:
            print("Muito acima do peso, ", round (imc,2))
            wr.writerows(['Muito acima do peso: ']+ [str(imc)])

else:
    with open('IMC.txt',  'w', newline = '') as wr:
        

        if imc <17: 
            print( "Muito abaixo do peso, ", round (imc,2) )
            wr.writelines(['Muito abaixo do peso: ']+ [str(imc)])
        elif imc >= 17 and imc <18.5:
            print("Abaixo do peso normal, " , round (imc,2))
            wr.writelines(['Abaixo do peso normal: ']+ [str(imc)])
        elif imc >= 18.5 and imc < 25.0:
            print("Peso dentro do normal, ", round (imc,2))
            wr.writelines(['Peso dentro do normal: '] + [str(imc)])
        elif imc >= 25 and imc < 30:
            print("Acima do peso normal, ", round (imc,2))
            wr.writelines(['Acima do peso normal, ']+ [str(imc)])
        else:
            print("Muito acima do peso, ", round (imc,2))
            wr.writelines(['Muito acima do peso: ']+ [str(imc)])


