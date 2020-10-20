##### PROGRAMA REFERENTE A ATIVIDADE CONTEXTUALIZADA 9 #####
##### ALUNA: CAROLINA KARLA DE SOUZA EVANGELISTA ###########

import numpy as np

# função para abrir e ler os arquivos
def abrir():
    with open('C:\\Users\\carol\\Desktop\\programacao20202\\isdprog2020\\Aula 9\\coletaFlexJoelho.csv', 'r') as fileobj:
        sensor1=[] #separei os sensores criando duas listas
        sensor2=[]
        for line in fileobj:
            dadosEsp=line.split('],""[')
            esp2=dadosEsp[1].split(']""')[0]
            esp1=dadosEsp[0].split("[")[1]
            for dadosEsp1 in esp1.split(","):
                sensor1.append(float(dadosEsp1))
            for dadosEsp2 in esp2.split(","):
                sensor2.append(float(dadosEsp2))
    return sensor1, sensor2

# calculos 
# modifiquei algumas coisas pois na atvd 8 não tinha visto as formulas de dadoa e dadow antes 

def dadoa (vet): #função pra calcular o dadoa
    return np.arctan(vet[0]/(np.sqrt(vet[1]**2 + vet[2]**2))) * 180/np.pi

def dadow (vet): #função pra calcular o dadow
    return np.arctan(vet[3]/(np.sqrt(vet[4]**2 + vet[5]**2))) * 180/np.pi

def ang(ang0,vet): #calculo pro angulo
    dt = 0.05 
    M = 0.98
    return M * (ang0 + dadow(vet) * dt) + (1 - M) * dadoa(vet)

def analise(ang): 
    print('Somatório:', np.sum(ang))
    print('Média dos ângulos:', np.mean(ang))
    print('Menor ângulo:', np.min(ang))
    print('Maior ângulo:', np.max(ang))
    print('Ângulos arredondados:', np.round(ang))

    dm = [] # diferença da média e cada valor do vetor ao quadrado dividida pelo tamanho do vetor
    for a in ang:
        dm.append((np.mean(ang)-a)**2/len(ang))
    print('Diferença da média:', dm)

    va = [] # variação angular (ângulo na posição i+1 – ângulo na posição i)
    for i in range(1,len(ang)):
        va.append(ang[i]-ang[i-1])
    print('Variação Angular:', va)

def calculo(sensor):
    angs = [0]
    for linha in sensor:
        angs.append(ang(angs[-1],linha))
    angs = np.array(angs)
    return angs


sensor1, sensor2 = np.array(abrir()) 
sensor1 = np.reshape(sensor1,(int(len(sensor1)/6),6))
sensor2 = np.reshape(sensor2,(int(len(sensor2)/6),6))

ang1 = calculo(sensor1)
ang2 = calculo(sensor2)
analise(ang1)

print('\nacabou programação\npode vir processamento de sinais !')
print('\n~~agradecimentos~~\n\nprof. andré\nduda franklin\njoão paulo (irmãos tem que se ajudar)\nwell (o melhor físico que eu conheço --o único)\n')
