"""
Seja o seguinte procedimento cirúrgico:

1 - Procedimento de anestesia: Pode-se utilizar uma diversidade de fármacos para
anestesia os animais, dentre eles Ketamina e xilazina utilizados em conjunto,
halotano (gasoso). Verificar a dosagem correta de acordo com o peso dos animais.

2 - Depois do anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico.
As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal.
Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável
por este movimento. Em seguida verificar a angulação da cabeça do animal, a qual deve estar
sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia
plana.

3 - Limpeza do campo de trabalho: Este procedimento requer o cumprimento de algumas etapas:
Retirada da pelagem que recobre a parte superior da calota craniana, Retirada dos tecidos
moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana.
Por último e não menos importante deve-se limpar a calota craniana de qualquer resto de
“pele” que esteja sobrando utilizando H2O2 10 volumes.

4 - Com o animal em posição e com o campo cirúrgico devidamente limpo, utiliza-se uma pequena
camada de poliacrilato em todo o perímetro externo para evitar sangramentos.

5 - Após este procedimento deve-se escolher um ponto para a fixação de parafusos, de preferência
na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior
profundidade do parafuso. 
Obs: Cuidar para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas
no parafuso.


EscolherAnimal
InserirPeso
Farmaco1+Halotano+Dosagem
Farmaco2+Halotano+Dosagem


"""
animais = ("Rato", "Camundongo", "Sagui")
# farmaco = ("Ketamina", "Xilazina")

animalSelecionado = 0


def anestesia():
    print(animais[animalSelecionado - 1])
    print("\nPara saber o volume de Anestesia:\n")
    print("""Digite o peso do animal em gramas\n""")
    PesodoAnimal = int(input("Digite: "))
    print("Para cada 10 gramas é utilizado 1ml de farmaco")
    if PesodoAnimal / 10 <= 20:
        print("O Farmaco utilizado é Ketamina com ", PesodoAnimal / 10)
    else:
        print("O Farmaco utilizado é Xilazina com ", PesodoAnimal / 10)


def instrucoes1():
    print("Instruções do passo 1\n")
    print(
        """Depois do anestésico ter feito efeito, deve-se posicionar o animal no estereotáxico.
\n"""
    )
    print(
        """As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal.
\n"""
    )
    print(
        """Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável
por este movimento.\n"""
    )
    print(
        """ Em seguida verificar a angulação da cabeça do animal, a qual deve estar
sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia
plana\n"""
    )


def instrucoes2():
    print("Instruções do passo 2\n")
    print(
        """Limpeza do campo de trabalho: Este procedimento requer o cumprimento de algumas etapas:
\n"""
    )
    print(
        """Retirada da pelagem que recobre a parte superior da calota craniana, Retirada dos tecidos moles epiderme,
derme e tecido conjuntivo até alcançar a parte óssea da caixa craniana.
\n"""
    )
    print(
        """Por último e não menos importante deve-se limpar a calota craniana de qualquer resto de “pele” que
esteja sobrando utilizando H2O2 10 volumes\n"""
    )


print("\nBem Vindo!\n")
print("ESTE PROGRAMA É RESPONSÁVEL PELA AUTOMAÇÃO DA CIRURGIA COM ESTEREOTÁXICO\n")

while animalSelecionado != 4:

    print("Para iniciar você deve selecionar um animal:")
    print(
        """
    [1] Rato
    [2] Camundongo
    [3] Sagui
    [4] Sair do Programa\n"""
    )
    animalSelecionado = int(input("Digite:"))
    if animalSelecionado == 4:
        print("Sair do Programa")
    else:
        anestesia()
        instrucoes1()
        instrucoes2()

    animalSelecionado = 4

