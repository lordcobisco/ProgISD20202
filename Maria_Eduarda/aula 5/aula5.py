#Declarando listas
"""lista= ["a","b","c","d","e"]
vetor=["duda"]
listak=["duda","Franklin",1,1.67,lista,vetor]
print(lista)
print(listak)
print(listak[4][0])#pegar uma da lista interna
print(len(lista)) #tamanho
#soma  e multiplicação
print(len(lista+[1]))
print(len(lista+listak))
print(lista*3)
print(len(lista*3))
#In
print("a" in lista)
if ("b" in lista):
    print("Rapaz, apois num tem")
for key,value in enumerate(lista):
    print(key)
    print(value)
#minimo e máximo
outrovetor=[1,2,3,4,5,67]
print(max(outrovetor))
print(min(outrovetor))

#indexacao
print(lista[-1] + lista[-2])
# apend é mais
linguagens=["Java","sql","php","c","sql"]
print(linguagens)
linguagens.append("python") #ADD
print(linguagens)
linguagens.insert(0,'flutter') #insere
print(linguagens)
print(linguagens.pop(1)) #retira um final da lista
linguagens.remove('python') #remove coisas
print(linguagens)
numeros=[1,2,3,4,5]
print(numeros.index(4))

#metodos sort, count, reverse
linguagens.sort()
print(linguagens)
linguagens.reverse()
print(linguagens)
print(linguagens.count('sql'))#conta o número de repetições
linguagens.remove("sql")
print("sql")

#Aliasing e clone
b=[98,99,100]
a=b
print(a is b)
if (a is b):
    print(bin(b[1]))
b.insert(2,87)
print(a)

u=[1,2,3]
t=u[:]
print(t is u)
u.insert(0,8)
print(u)
print(u[1:4])
tup=(1,2,3,4)
vazia= tuple()
print(tup)
print(tup[0:2])

p="duda"
print(p[0:1])
print(p[:2])"""
acumulados=[100,200]
dadosCovid={}
dadosCovid1=dict()
print(dadosCovid1)
dadosCovid={"Brasil":[0,1,acumulados[0],3],"Argentina":[0,5,6,7]}
print(dadosCovid[input('estado buscado')][2])
print(dadosCovid["Brasil"][2])