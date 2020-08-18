#Inicio da aula Hello World 

#print("este é o meu primeiro programa") #é assim que se comenta o programa

#Fim da aula

print("Bem vindo ao sistema de cálculo de IMC")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso/(altura*altura)

IMC_Abaixo17 = False
IMC_Entre17e18.5 = False
IMC_Entre18.5e25 = False
IMC_Entre25e30 = False
IMC_Acima30 = False

print(IMC)

