# Exercício da aula 08 - Implementação dos arquivos de csv e txt

# Solicitar ao usuário a forma de gravação do arquivo.

import csv

def Calculoimc(altura, peso):
        """Retornar IMC"""
        imc = peso / (altura**2)
        return imc

def ResultadoIMC(imc):
    
    tipoarquivo = int(input('Qual formato você deseja salvar o seu arquivo? Digite 1 para CSV e 2 para TXT: \n'))
    if (tipoarquivo == 1):
        with open('imc08.csv','w', newline='') as csvfile:
            imcwriter = csv.writer(csvfile, delimiter=' ',
                                   quotechar='|', quoting=csv.QUOTE_MINIMAL)
            print('Índice de Massa Corpotal (IMC)')
            imcwriter.writerow('Índice de Massa Corporal (IMC)')
            print("Seu IMC é: ", imc)
            imcwriter.writerow('Seu IMC é:')
            imcwriter.writerow([imc])
            print('Você está:')
            imcwriter.writerow('Você está: ')
            if imc < 17:
                print('Muito abaixo do peso.')
                imcwriter.writerow('Muito abaixo do peso.')
            if 17 <= imc < 18.5:
                print('Abaixo do peso normal.')
                imcwriter.writerow('Abaixo do peso normal')
            if 18.5 <= imc <25:
                print('Dentro do peso normal.')
                imcwriter.writerow('Dentro do peso normal')
            if 25 <= imc < 30:
                print('Acima do peso normal.')
                imcwriter.writerow('Acima do peso normal')
            if imc>30:
                print('Muito acima do peso.')
                imcwriter.writerow('Muito acima do peso.')
            print('')
            print('Cuide da sua saúde e faça exercícios físicos.')
            imcwriter.writerow('Cuide da sua saúde e faça exercícios físicos.')
    if (tipoarquivo == 2):
        with open('imcAula08.txt', 'w') as arquivo:
            print('Índice de Massa Corpotal (IMC)')
            arquivo.write('Índice de Massa Corporal (IMC)\n')
            print("Seu IMC é: ", imc)
            arquivo.write('Seu IMC é:\n')
            arquivo.write(str(imc))
            print('Você está:')
            arquivo.write('Você está: \n')
            if imc < 17:
                print('Muito abaixo do peso.')
                arquivo.write('Muito abaixo do peso.\n')
            if 17 <= imc < 18.5:
                print('Abaixo do peso normal.')
                arquivo.write('Abaixo do peso normal\n')
            if 18.5 <= imc <25:
                print('Dentro do peso normal.')
                arquivo.write('Dentro do peso normal\n')
            if 25 <= imc < 30:
                print('Acima do peso normal.')
                arquivo.write('Acima do peso normal\n')
            if imc>30:
                print('Muito acima do peso.')
                arquivo.write('Muito acima do peso.\n')
            print('')
            print('Cuide da sua saúde e faça exercícios físicos.')
            arquivo.write('Cuide da sua saúde e faça exercícios físicos.\n')

altura = float(input('Por favor, digite a sua altura:'))
peso = float(input('Por favor, digite o seu peso:'))

imc = Calculoimc(altura, peso)
ResultadoIMC(imc)