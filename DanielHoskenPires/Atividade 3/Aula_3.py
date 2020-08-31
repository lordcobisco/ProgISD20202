print ("Hello World")
# cerquilha serve para comentar o código na llinha e não será aparecido no programa
# cerquilha não será utilizado pelo programa também
'''essa função serve para comentar o código em blocos e não será aparecido no programa
print ("alguma coisa") 
nada será utilizado pelo programa também '''
# variáveis
varString = "Daniel Hosken Pires"
print (varString)
varInt = 497
print (varInt)
varFloat = 9.95
print (varFloat)
varBool = True
print (varBool)
#identificando tipos de variáveis
varString = "Daniel Hosken Pires"
print (varString)
print (type(varString))
varInt = 497
print (varInt)
print (type(varInt))
varFloat = 9.95
print (varFloat)
print (type(varFloat))
varBool = True
print (varBool)
print (type(varBool))
# comando para importar módulos em Python
# uma opção é importar todo o pacote:
import math
print (math.sqrt(25))
#outra opção é importar apenas determinada função específica do pacote:
from math import sqrt
print (sqrt(25))
#Atribuição e aritméticos
resultadoSoma = 5+5
print (resultadoSoma) #atribuição
print (5+5) #soma e já vem imbutido no pacote padrão
print (2-5) #subtração e já vem imbutido no pacote padrão
print (2*5) #multiplicação e já vem imbutido no pacote padrão
print (10/2) #divisão e já vem imbutido no pacote padrão
print (2**10) #exponencialização e já vem imbutido no pacote padrão
print (21//9) #parte inteira da divisão e já vem imbutido no pacote padrão
print (21%9) #resto da divisão e já vem imbutido no programa  
#operadores compostos
a, b, c = 2, 4, 8
a, b, c = a*2, a+b+c, a*b*c
print (a, b, c)
#operador lógico not: 0 -> 1 e 1-> 0
varLogica = True
print("Valor de 'not varLogica': ", not varLogica)
#operador lógico and
varLogica1 = True
varLogica2 = False
print("Valor de 'varLogica1 e varLogica2': ", varLogica1 and varLogica2)
#operador lógico or
varLogica1 = True
varLogica2 = False
print("Valor de 'varLogica1 e varLogica2': ", varLogica1 or varLogica2)
#expressões lógicas
print (2==2) #igual
print (2!=2) #diferente
print (2>2) #maior
print (2<2) #menor
print (2>=2) #maior ou igual
print (2<=2) #menor ou igual 
#Input e print (básico)
num = input ("Digite um número: ")
print (num)
login = input("login: ")
senha = input("senha: ") 
print ("O usuário informado foi: %s, e a senha digitada foi: %s. " %(login, senha))


