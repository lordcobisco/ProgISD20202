
print('Este programa tem como objetivo facilitar o processo de diagnostico de bexiga neurogênica e intestino neurogênico diante do contexto do COVID-19, afim de selecioar pacientes para participar de uma pesquisa sobre o tratamento da BN e IN com o uso da neuromodulação parasacral')

nun = input("Digite a data de hoje")
print(nun)

nome = str(input("Digite o seu nome "))
print(nome)

Sexo = int(input("sexo? (responda 0 para Feminino e 1 para Masculino"))
if(Sexo):
    print('Feminino')
else:
    print('Masculino')

NivelDaLesão = str(input("Digite o nível da sua lesão "))
print(NivelDaLesão) 

TipoDaLesão = int(input("A lesão é completa ou incompleta? (responda 0 para completa e 1 para incmpleta)" ))
if(TipoDaLesão):
    print('completa')
else:
    print('incompleta')

Sonda = int(input(" Faz uso de sonda ? (responda 0 para não e 1 para sim) " ))
if(Sonda):
    print('Sim')
else:
    print('Não')


print('As questões devem ser respondidas de acordo com os sinais e sintomas urináirio e da evacuação fecal diário, para que o diagnóstico seja fidedigno ')

print('Parte 1')
print('Questões relacionadas aos sinais e sintomas urinário')

print('Muitas pessoas sofrem eventualmente de sintomas urinários. Estamos tentando descobrir quantas pessoas têm sintomas urinários, e quanto isso incomoda. Agradecemos a sua participação ao responder estas perguntas, para sabermos como tem sido o seu incômodo durante as últimas 04 semanas')

Quest1 = int(input(' Quantas vezes você urina ou passa a sonda durante o dia?'))

if(Quest1 <= 6 ):
    print('score 0')
elif(Quest1 <= 8 ):
    print('score 1')
elif (Quest1 <= 10 ):
    print('score 2')
elif (Quest1 <= 12 ):
    print('score 3')
elif (Quest1 == 13):
    print('score 4')
else:
    print( 'mais de 13 vezes; score 4')


print("O quanto isso incomoda você? de 0 a 10. 0(não incomoda) 10 (incomoda muito)")
nun = input(" digite um numero")
print(nun)

Quest2 = int(input('Durante a noite, quantas vezes, em média, você têm que se levantar para urinar ou passar a sonda?'))

if(Quest2 == 1):
    print('score 1')
elif(Quest2 == 2):
    print('score 2')
elif(Quest2 == 3):
    print('score 3')
elif(Quest2 >= 4):
    print('score 4')
else:
    print('Nenhuma vez; score 0')

print("O quanto isso incomoda você? de 0 a 10. 0(não incomoda) 10 (incomoda muito)")
nun = input(" digite um numero")
print(nun)


Quest3 = int(input("Você precisa se apressar para chegar ao banheiro para urinar ou passar a sonda? ( Responda = 1 Poucas Vezes, 2 Às vezes, 3 Na maioria das vezes, 4 sempre)"))

if(Quest3 == 1 ):
    print('score 1')
elif (Quest3 == 2):
    print('score 2')
elif (Quest3 == 3):
    print('score 3')
elif (Quest3 == 4):
    print('score 4')
else:
    print('Nunca;  score 0')

print("O quanto isso incomoda você? de 0 a 10. 0(não incomoda) 10 (incomoda muito)")
nun = input(" digite um numero")
print(nun)

Quest4 = int(input("Você perde urina antes de chegar ao banheiro ou antes de passar a sonda? ( Responda = 1 Poucas Vezes, 2 Às vezes, 3 Na maioria das vezes, 4 sempre)"))

if(Quest4 == 1 ):
    print('score 1')
elif (Quest4 == 2):
    print('score 2')
elif (Quest4 == 3):
    print('score 3')
elif (Quest4 == 4):
    print('score 4')
else:
    print('Nunca;  score 0')

print("O quanto isso incomoda você? de 0 a 10. 0(não incomoda) 10 (incomoda muito)")
nun = input(" digite um numero")
print(nun)

if(Quest1 + Quest2 + Quest3 + Quest4 >= 8 ):
    print("Vamos marcar o seu atendimento?")
else:
    print("Não é necessário marcar um atendimento, mas posso tirar suas dúvidas por email")

print('Parte 2 ')
print('Questões relacionadas aos sinais e sintomas evacuatório/constipação')

Quest1Const = int(input("É necessario realizar esforço defecatório durante mais de 25% dos movimentos intestinais/durante a evacuação ? (responda 0 para não e 1 para sim) "))

if(Quest1Const):
    print('sim')
else:
    print('Não')

Quest2Const = int(input(" Suas Fezes tem a aparência granuladas/bolinhas ou cilíndrica com caroços  em mais de 25% dos movimentos intestinais/durante a evacuação  ? (responda 0 para não e 1 para sim) "))
if(Quest2Const):
    print('sim')
else:
    print('Não')

Quest3Const = int(input(" Você tem a sensação de evacuação incompleta em mais de 25% dos movimentos intestinais/durante a evacuação ? (responda 0 para não e 1 para sim) " ))
if(Quest3Const):
    print('sim')
else:
    print('Não')

Quest4Const = int(input(" Você tem a sensação de bloqueio/obstrução anorrectal em mais de 25% dos movimentos intestinais/durante a evacuação  ? (responda 0 para não e 1 para sim) " ))
if(Quest4Const):
    print('sim')
else:
    print('Não')

Quest5Const = int(input(" É necessario realizar manobras manuais para facilitar mais de 25% dos movimentos intestinais/durante a evacuação como manobras digitais, suporte manual do pavimento pélvico ? (responda 0 para não e 1 para sim) " ))
if(Quest5Const):
    print('sim')
else:
    print('Não')

Quest6Const = int(input(" Você apresenta menos de 3 movimentos intestinais/evacuação  espontâneos por semana ? (responda 0 para não e 1 para sim) " ))
if(Quest6Const):
    print('sim')
else:
    print('Não')

Quest7Const = int(input(" Suas fezes são moldadas raramente presentes sem recurso a laxantes ? (responda 0 para não e 1 para sim) " ))
if(Quest7Const):
    print('sim')
else:
    print('Não')

if(Quest1Const + Quest2Const + Quest3Const + Quest4Const + Quest5Const + Quest6Const + Quest7Const  >= 2 ):
    print("Vamos marcar o seu atendimento?")
else:
    print("Não é necessário marcar um atendimento, mas posso tirar suas dúvidas por email")


print("Fim do questionário")

