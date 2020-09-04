#Exemplos executados na Aula 06

listaNome = ['André', 'Felipe', 'Oliveira']

for nome in listaNome:
    print(nome) 


listaNome = ['André', 'Felipe', 'Oliveira']

for nome in listaNome:
    print(nome) 
else:
    print('Todos os nomes foram escritos com sucesso!') #escreve todos os nomes da lista e só depois escreve isso


for key, value in enumerate(['p','y','t','h','o','n']):
    print(key, value) #puxa a posição do vetor e diz qual é o elemento na lista


for i in range(5):
    print(i)


for i in range(9,-2,-1): #vai de 9 até -2, decrementando -1 a cada passo
    print(i)


linguages = ['Python', 'PHP', 'C#','Cobol', 'C++']
tam = len(linguages)
indices = range(tam)
for item in indices:
    print(linguages[item])


lista1 = ['bacon', 'fritas', 'picanha']
lista2 = ['cerveja', 'refri', 'suco']

for alimento,bebida in zip(lista1, lista2): #zip é para juntar as duas listas - é uma palavra reservada
    print(alimento,bebida)


contador = 0
while contador < 5:
    print(contador)
    contador = contador +1

for contador in range(5):
    if(contador>3):
        break
    print(contador)


contador=1 #não pode começar com zero - condição abaixo
while contador<100 and contador >0:
    contador = int(input('Digite um número menor que 100 e maior que zero: ')) #input é o usuário
else:
    print('O número digitado não está na faixa pedida.')


animalambientado=0
while not animalambientado:
    animalambientado = int(input('Informe se o animal está ambientado: ')) 
else:
    print('O animal está ambientado.') #nesse caso digita 0 ou 1.  Enquanto for 0, vai continuar perguntando. Quando 1, dá a mensagem de que está ambientado

for/while
    break
    continue #Break e continue só tem ação dentro de uma estrutura de repetição


tocouNaBarra = 0 #igual a zero = falso
for contador in range(5):
   tocouNaBarra = int(input('O animal tocou em pelo menos 1 das barras'))
    if(tocouNaBarra):
        print('O animal tocou na barra')
        break

    print(contador)