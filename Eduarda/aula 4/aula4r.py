lazy= int(input('tu se acha preguiçoso'))
logic1= int(input('tu se acha inteligente'))
logic= int(input('Apertou o botão 1'))
log= int(input("Apertou o botão 2"))

if (logic1):
    print("Apois tu num é inteligente")
print("Acabou!!")

if (not logic and not log):
    print("Foram add 10 mg de alimento")
elif (not logic and log):
    print("Foram add 20mg de comida")
elif (logic and not log):
    print("Nenhuma comida foi add")
elif ( logic and log):
    print("Foram add 40mg de comida")
else:
    print("Foi add 40mg de comida")


if (lazy and not logic1):
    print("preguiçoso e não inteligente")
elif (not logic1 and not lazy):
    print("Não é preguiçoso e nem inteligente")
elif (logic1 and not lazy):
    print("Você é inteligente")
elif ( logic1 and lazy):
    print("Você é tanto preguiçoso quanto inteligente")

lazy= input('tu se acha preguiçoso')
logic1= input('tu se acha inteligente')
if (lazy=="s" and logic1=="n"):
    print("preguiçoso e não inteligente")
elif (logic1=="n" and lazy=="n"):
    print("Não é preguiçoso e nem inteligente")
elif (logic1=="s" and not lazy=="n"):
    print("Você é inteligente")
elif ( logic1=="s" and lazy=="s"):
    print("Você é tanto preguiçoso quanto inteligente")
num=int(input())
if (num<5):
    print("menor")
print("Acabou!!")

num=int(input())
if (num==1):
    print("menor")
elif(num==2):
    print("Maior")
print("Acabou!!")