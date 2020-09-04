print('Programa de Cirurgia esterotáxica')
print('Anestesie o animal com os segintes medicamento (Verifique a dosagem correta de acordo com o peso do animal')
listaAnestesia = ['Ketamina','xilazina','halotano']
for anestesias in listaAnestesia:
    print(anestesias)

anestisiasOK = (int(input('O anestésico fez efeito?(Se não aperte 0 se sim aperte 1)')))
if(anestisiasOK):
    print('Prossiga a cirurgia!')
else:
    print('Repita a anestesia')

print('Posicione o animal no estereotáxico')
print('Posicione as barras no ouvido externo do animal')
posicaoCabeça = (int(input('A Ângulação da cabeça está sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana?(Se não aperte 0 se sim aperte 1)')))
if(posicaoCabeça):
    print('Prosiga paraproxima fase')
else:
    print('Corrija a ângulação')

print('Limpeza de campo de trabalho')

limpeza = ('Retirar pelagens','Retirar epiderme','Retirar derme','Retirar tecido conjuntivo')
for passos in limpeza:
    print(passos)
    (int(input('Alcançou a calota craniana?(Se não aperte 0 se sim aperte 1)')))
    if(limpeza):
        print('Continue a limpeza')
if not (limpeza):
    print('Prossiga com a cirurgia')

print('Limpe a calota craniana dos resto de pele utilizando H2O2 10 volumes')

posicionamentoCampo =(int(input('O animal está posicionado e com o campo cirúrgico devidamente limpo?(Se não aperte 0 se sim aperte 1)')))
if(posicionamentoCampo):
    print('Utilize uma pequena camada de poliacrilato em todo o perímetro externo para evitarsangramentos.')
if not(posicionamentoCampo):
    print('Posicione e limpe corretamente o animal')

print('Escolha  um ponto para a fixação de parafusos (preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior profundidade do parafuso.)')

escolhaLocalParafuso = (int(input('Escolheu o ponto correto de para fixar os parafusos?(Se não aperte 0 se sim aperte 1)')))
if(escolhaLocalParafuso):
    print('Siga para o próximo passo!')
if not(posicionamentoCampo):
    print('Continue procurando o ponto ideal para os parafusos!')

print('Cuidado para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.')

print('Posicione a agulha (devidamente preparada para o tamanho da cânula e que servirá de suporte para a fixação das cânulas) sobre o bregma')
print('Faça os cálculos de posicionamento AnteroPosterior (AP), LateroLateral (LL) e DorsoVentral (DV). Os valores utilizados para os cálculos são os valores encontrados nas réguas a partir do posicionamento da agulha.')

print(float(input('Digite o valor do posicionamento AnteroPosterio(AP)')))
print(float(input('Digite o valor do posicionamento LateroLateral (LL)')))
print(float(input('Digite o valor do posicionamento DorsoVentral(DV).')))

posicionamento1= (int(input('Inseriu o posicionamento corretamente?(Se não digite 0 se sim digite 1)')))
if(posicionamento1):
    print('Siga para próximo passso')
if not(posicionamento1):
    print('Insira o Posicionamento')

print('A localização dos pontos de inserção das cânulas-guia são:')

ValorAp = {}
ValorAp ["Antero Posterior"] = [6]
print(ValorAp)

valorLl = {}
valorLl ['Latero Lateral'] = [3]
print(valorLl)

valorDV ={}
valorDV ['Dorso Ventral'] = [4]
print(valorDV)

print('Faça um furo ate alcançar as meninges (O ideal é não furar as meninges)')

print('introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (4,00) que foi calculado anteriormente.')

print('drenar qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.')

print('Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejadasem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso.')

print(' Deixe secar até ficar suficientemente rígido.')

print('introduza a cânula-guia previamente confeccionada até o valor DorsoVentral (6,00) que foi calculado anteriormente.')

conclusao = 0
while conclusao:
    conclusao = int(input('Concluiu as etapas anterioes?'))
    print('Siga para finalização da cirurgia')
else:
    print('Termine os passos anteriores')

print('Fazer a finalização do capacete')

print('Cirurgia esterotáxica finalizada com sucesso!')



        